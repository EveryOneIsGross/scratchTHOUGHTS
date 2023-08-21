import pyttsx3
from ebooklib import epub
import json
import os
import threading
import queue
import pickle
import re
from gpt4all import GPT4All, Embed4All
import PyPDF2
from collections import deque
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from elevenlabs import generate, play, set_api_key
import os
os.environ['PATH'] += os.pathsep + 'c:/ffmpeg/bin/'

# Initialize the embedding model at the beginning of the script
embedder = Embed4All()
# Delimiter to separate embeddings in the string
EMBEDDING_DELIMITER = ','
# Global list to store embeddings
embeddings = []
selected_voice = None
voices = []  # Add this global declaration
# Add a global flag at the beginning of your code
program_running = True
# Global list to store chat responses
chat_responses = []


# Splash screen and introduction
def splash_intro():

    print("_|_|_________|_|________|_|/_____|_|__|_|__\\/__|")
    print("_|_|_________|_|________|_|_(____|_|__|_|_\\__/_|")
    print("_|_'__\\_/__`_|_'__\\_/___\\_|\____\\|_|__|_|_|\\/|_|")
    print("_|_|_)_|_(_|_|_|_)_|____/_|____)_|_|__|_|_|__|_|")
    print("_|_.__/_\\__,_|_.__/_\\___|_|_____/_\\____/|_|__|_|")

    print("\n")
    print("Instructions:")
    print("- You'll be prompted to choose a voice for reading.")
    print("- Provide the path to your txt, epub, or pdf file.")
    print("- Define the desired chunk size for reading.")
    print("- Interact with the reader by typing commands like 'search', 'chat', or 'exit'.")
    print("- Enter a number to jump to a specific segment.")
    print("- Typing 'chat' will prompt the local llm to summarize the last spoken chunk.")
    print("\n")

# Call the splash and intro function at the beginning
splash_intro()


def adjust_voice_settings(engine):
    global selected_voice, voices
    """
    Allow the user to adjust pyttsx3 voice settings.
    """

    # List available voices
    voices = engine.getProperty('voices')
    print("Available voices:")
    for index, voice in enumerate(voices):
        print(f"{index}. Name: {voice.name}, Languages: {voice.languages}")

    # Add ElevenLabs as an additional option
    print(f"{len(voices)}. ElevenLabs TTS API")

    voice_selection = int(input("Enter the number of the voice you want to use: "))
    while voice_selection < 0 or voice_selection > len(voices):  # <-- Adjusted this condition
        print("Invalid selection. Please choose a number from the list.")
        voice_selection = int(input("Enter the number of the voice you want to use: "))

    selected_voice = voice_selection
    if voice_selection < len(voices):  # If it's not ElevenLabs TTS API
        selected_voice_id = voices[voice_selection].id
        engine.setProperty('voice', selected_voice_id)
    else:
        # Prompt the user for the ElevenLabs API key
        elevenlabs_api_key = input("Enter your ElevenLabs API key: ").strip()
        set_api_key(elevenlabs_api_key)

    # User sets the volume
    #volume = float(input("Enter volume (0.0 to 1.0, where 1.0 is the loudest): "))
    #while volume < 0.0 or volume > 1.0:
    #    print("Invalid volume. Please enter a value between 0.0 and 1.0.")
    #    volume = float(input("Enter volume (0.0 to 1.0): "))
    #
    #engine.setProperty('volume', volume)

    # User sets the speech rate
    rate = int(input("Enter speech rate (words per minute, e.g., 150): "))
    while rate <= 0:
        print("Invalid rate. Please enter a positive value.")
        rate = int(input("Enter speech rate (words per minute): "))

    engine.setProperty('rate', rate)

    print("Voice settings adjusted!")


# Example usage:
engine = pyttsx3.init()
adjust_voice_settings(engine)
spoken_chunks = []

def speak_chunk(engine, chunk, q):
    """Speak the chunk using the engine, embed it, and handle user inputs."""
    
    # Remove HTML tags from the chunk
    clean_chunk = remove_html_tags(chunk)
    print("\nReading Chunk:", clean_chunk)  # Display the cleaned chunk content
    
    # If ElevenLabs TTS API is selected
    if selected_voice == len(voices):
        try:
            audio = generate(text=clean_chunk, voice="Bella", model="eleven_monolingual_v1")
            play(audio)
        except Exception as e:  # Catch errors from ElevenLabs
            print(f"Error using ElevenLabs: {e}")
            print("Reverting to an alternative voice.")
            
            # Revert to the first available pyttsx3 voice as an example
            engine.setProperty('voice', voices[0].id)
            engine.say(clean_chunk)
            engine.runAndWait()
    else:
        engine.say(clean_chunk)
        engine.runAndWait()
    
    # Embed the chunk after speaking
    embedding = embed_text(clean_chunk, embedder)
    
    # Store the spoken chunk
    spoken_chunks.append(clean_chunk)

    # Check if there's any input from the user
    if not q.empty():
        return q.get()
    return None


def read_chunks(text, max_chunk_size=150):
    """Divide the text into chunks at every '.\n' or based on max_chunk_size."""
    
    # Split the text at every '.\n'
    preliminary_chunks = text.split('.\n')

    # Check if any of the preliminary chunks exceed the max_chunk_size
    # and further divide them if necessary.
    chunks = []
    for pre_chunk in preliminary_chunks:
        while len(pre_chunk) > max_chunk_size:
            pos = pre_chunk.rfind(' ', 0, max_chunk_size)
            if pos == -1:
                pos = max_chunk_size
            chunks.append(pre_chunk[:pos])
            pre_chunk = pre_chunk[pos:].lstrip()
        chunks.append(pre_chunk)

    return chunks


def extract_text_from_epub(file_path):
    """Extract text content from an epub file."""
    book = epub.read_epub(file_path)
    content = []
    for item in book.items:
        if isinstance(item, epub.EpubHtml):
            content.append(item.content.decode('utf-8'))
    return ' '.join(content)

def extract_text_from_pdf(file_path):
    """Extract text content from a PDF file."""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = [page.extract_text() for page in reader.pages]
    return ' '.join(text)

def save_to_json(filename, chunks):
    """Save chunks to a JSON file."""
    json_filename = os.path.splitext(filename)[0] + '.json'
    with open(json_filename, 'w') as file:
        json.dump({"chunks": chunks}, file)
    return json_filename

def load_from_json(json_filename):
    """Load chunks from a JSON file."""
    with open(json_filename, 'r') as file:
        data = json.load(file)
    return data["chunks"]

def get_input(q):
    """Get user input and put it into a queue."""
    try:
        while program_running:  # Check the flag before waiting for input
            line = input()
            q.put(line)
    except:
        pass


def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


def chat_with_agent():
    """Obtain a concise summary of the last spoken chunks using an AI model."""
    
    # Initialize the AI model
    model = GPT4All("C://AI_MODELS//orca-mini-3b.ggmlv3.q4_0.bin")
    
    # Extract the recent chunks to be summarized
    input_text_chunks = spoken_chunks[-1:]  # Getting the last spoken chunk
    print("\nInput text chunks:", input_text_chunks)
    # Construct the prompt with clear instructions for the AI model
    input_text = (
        "### System:\n"
        "You are an assistant that summarises spoken text. Summarise: \n\n"
        "### User:\n" + 
        ' '.join(input_text_chunks)
    )
    
    # Generate the summary response
    response = model.generate(input_text, max_tokens=1200, temp=0.7)
    # Append the response to the chat_responses list
    chat_responses.append(response)
    
    # Print the agent's response first
    print("\nAgent's response:", response)
    
    # Store the original voice ID
    original_voice_id = engine.getProperty('voice')
    
    # Switch to an alternate local voice for the agent
    if original_voice_id == voices[0].id:
        engine.setProperty('voice', voices[1].id)  # Switching to voice 1
    else:
        engine.setProperty('voice', voices[0].id)  # Switching to voice 0
    
    # Read the response out loud
    engine.say(response)
    engine.runAndWait()

    # Restore the original voice
    engine.setProperty('voice', original_voice_id)

    return response






def save_embeddings(embeddings, filename):
    """Save embeddings to a pickle file."""
    with open(filename, 'wb') as file:
        pickle.dump(embeddings, file)

def load_embeddings(filename):
    """Load embeddings from a pickle file."""
    with open(filename, 'rb') as file:
        embeddings = pickle.load(file)
    return embeddings

def embed_text(text, embedder):
    """Embed the given text using Embed4All and return the embedding."""
    return EMBEDDING_DELIMITER.join(map(str, embedder.embed(text)))

def main(engine):
    global voices, program_running, embeddings
    playback_queue = deque()



    def search_chunks(query, chunks, full_text_embedding, embedder):
        """Search for chunks using cosine similarity and return the index of the top match."""
        query_embedding = embed_text(query, embedder)
        similarities = []

        # Calculate cosine similarity for each chunk
        for chunk in chunks:
            chunk_embedding = embed_text(chunk, embedder)
            similarity = cosine_similarity(
                np.array(query_embedding.split(EMBEDDING_DELIMITER)).reshape(1, -1),
                np.array(chunk_embedding.split(EMBEDDING_DELIMITER)).reshape(1, -1)
            )
            similarities.append(similarity[0][0])

        # Get the index of the top match
        top_match = np.argmax(similarities)
        return [top_match]


        # Get file path from user
    file_path = input("Enter the path to the txt, epub, or pdf file: ")

    # Extract text based on file extension
    if file_path.endswith('.epub'):
        text = extract_text_from_epub(file_path)
    elif file_path.endswith('.pdf'):
        text = extract_text_from_pdf(file_path)
    else:
        with open(file_path, 'r') as file:
            text = file.read()

    # Let the user define the chunk size
    chunk_size = int(input("Enter the desired chunk size (e.g., 150): "))
    while chunk_size <= 0:
        print("Invalid chunk size. Please enter a positive value.")
        chunk_size = int(input("Enter the desired chunk size: "))

    # Divide the text into chunks
    chunks = read_chunks(text, chunk_size)

    # Clean the extracted text of any potential HTML tags
    text = remove_html_tags(text)
    full_text_embedding = embed_text(text, embedder)

    # Save chunks to a JSON file
    json_filename = save_to_json(file_path, chunks)
    print(f"Saved chunks to {json_filename}")

    # Load chunks from the JSON file
    loaded_chunks = load_from_json(json_filename)
    
    # Load or initialize embeddings
    embeddings_filename = os.path.splitext(json_filename)[0] + '_embeddings.pkl'
    if os.path.exists(embeddings_filename):
        embeddings = load_embeddings(embeddings_filename)
    else:
        embeddings = []

    # Prompt for segment before playback
    segment = input(f"Enter a segment number (0-{len(loaded_chunks)-1}) or press Enter to start from the beginning: ").strip()
    i = 0 if not segment else int(segment)

    print("Type a number to jump to a segment, 'search QUERY' to search, or type 'exit' to quit.")
    q = queue.Queue()
    t = threading.Thread(target=get_input, args=(q,))
    t.start()

    while i < len(loaded_chunks) or playback_queue:
        print(f"\nSegment Number: {i}")  # Display the segment number before determining next chunk

        # Determine the next chunk to play
        if playback_queue:
            i = playback_queue.popleft()
        elif i >= len(loaded_chunks):
            break

        user_input = speak_chunk(engine, loaded_chunks[i], q)
        save_embeddings(embeddings, embeddings_filename)

        if user_input == "exit":
            print("\nExiting program.")
            save_embeddings(embeddings, embeddings_filename)
            program_running = False
            t.join()
            return file_path, chunk_size, i

        if user_input and user_input.startswith("search "):
            query = user_input[len("search "):]
            matches = search_chunks(query, loaded_chunks, full_text_embedding, embedder)


            if matches:
                playback_queue.extend([match - 1 for match in matches])

                print(f"Found a match in segment {matches[0]}. Adding to playback queue.")
            else:
                print("No matches found.")

        elif user_input == "chat":
            chat_with_agent()
            

            
        elif user_input and user_input.isdigit():
            i = int(user_input) - 1  # Subtract 1 to counteract the increment at the end of the loop
            if i >= len(loaded_chunks) or i < 0:
                print(f"Invalid segment number. There are only {len(loaded_chunks)} segments.")
                i = max(0, min(len(loaded_chunks) - 1, i))  # Clamp it between 0 and the last segment

        i += 1  # Increment the segment number at the end of the loop


def print_summary(file_path, chunk_size, i):
    """Print a summary of the book read, chat responses, and other details."""
    print("\n===== SUMMARY =====")
    # Summary of the book read
    print(f"\nBook Path: {file_path}")
    
    # Chat responses
    print("\nChat Responses:")
    for idx, response in enumerate(chat_responses, 1):  # Start the enumeration from 1
        print(f"{idx}. {response}")
    
    # Chunk size and last segment listened
    print(f"\nChunk Size: {chunk_size}")
    print(f"Last Segment Listened: {i}")



if __name__ == "__main__":
    try:
        file_path, chunk_size, i = main(engine)
    finally:
        # Always print the summary, even if there was an error or exception.
        print_summary(file_path, chunk_size, i)
