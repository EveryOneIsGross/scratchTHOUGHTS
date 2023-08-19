import pyttsx3
from ebooklib import epub
import json
import os
import threading
import queue
import pickle
import re
from gpt4all import GPT4All, Embed4All

# Delimiter to separate embeddings in the string
EMBEDDING_DELIMITER = ','
# Global list to store embeddings

embeddings = []
selected_voice = None
voices = []  # Add this global declaration
# Add a global flag at the beginning of your code
program_running = True


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

    # User selects a voice
    
    voice_selection = int(input("Enter the number of the voice you want to use: "))
    while voice_selection < 0 or voice_selection >= len(voices):
        print("Invalid selection. Please choose a number from the list.")
        voice_selection = int(input("Enter the number of the voice you want to use: "))
    selected_voice = voice_selection
    selected_voice_id = voices[voice_selection].id
    engine.setProperty('voice', selected_voice_id)

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


def read_chunks(text, chunk_size=150):
    """Divide the text into chunks."""
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def extract_text_from_epub(file_path):
    """Extract text content from an epub file."""
    book = epub.read_epub(file_path)
    content = []
    for item in book.items:
        if isinstance(item, epub.EpubHtml):
            content.append(item.content.decode('utf-8'))
    return ' '.join(content)

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


# Global list to store spoken chunks
spoken_chunks = []

def chat_with_agent():
    """Use the last 4 spoken chunks to converse with the agent and return its response."""
    model = GPT4All("C://AI_MODELS//openorca-platypus2-13b.ggmlv3.q4_1.bin")
    # Get all the chunks
    # input_text = "Summarise what we have covered: " + ' '.join(spoken_chunks)
    # Get the last 4 chunks or fewer if there are less than 2
    input_text_chunks = spoken_chunks[-2:]
    input_text = "Summarise what we have covered: " + ' '.join(input_text_chunks)
    
    response = model.generate(input_text, max_tokens=1500)
    return response

def speak_chunk(engine, chunk, q):
    """Speak the chunk using the engine, embed it, and handle user inputs."""
    
    # Remove HTML tags from the chunk
    clean_chunk = remove_html_tags(chunk)
    
    print("\nReading Chunk:", clean_chunk)  # Display the cleaned chunk content
    
    # Embed the chunk after speaking
    embedding = embed_text(clean_chunk)
    embeddings.append(embedding)
    
    engine.say(clean_chunk)
    engine.runAndWait()

    # Store the spoken chunk
    spoken_chunks.append(clean_chunk)

    # Check if there's any input from the user
    if not q.empty():
        return q.get()
    return None



def save_embeddings(embeddings, filename):
    """Save embeddings to a pickle file."""
    with open(filename, 'wb') as file:
        pickle.dump(embeddings, file)

def load_embeddings(filename):
    """Load embeddings from a pickle file."""
    with open(filename, 'rb') as file:
        embeddings = pickle.load(file)
    return embeddings

def embed_text(text):
    """Embed the given text using Embed4All and return the embedding."""
    embedder = Embed4All()
    return EMBEDDING_DELIMITER.join(map(str, embedder.embed(text)))

def main(engine):
    global voices
    global program_running
    # Initialize TTS engine

    # Get file path from user
    file_path = input("Enter the path to the txt or epub file: ")

    # Extract text based on file extension
    if file_path.endswith('.epub'):
        text = extract_text_from_epub(file_path)
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

    print("Type a number to jump to a segment or type 'exit' to quit.")
    q = queue.Queue()
    t = threading.Thread(target=get_input, args=(q,))
    t.start()

    while i < len(loaded_chunks):
        print(f"\nSegment Number: {i}")  # Display the segment number
        user_input = speak_chunk(engine, loaded_chunks[i], q)
        # Save embeddings to a pickle file
        save_embeddings(embeddings, embeddings_filename)
        if user_input == "exit":
            print("\nExiting program.")
            save_embeddings(embeddings, embeddings_filename)  # Save embeddings before exiting
            
            # Set the flag to False to stop the get_input thread
            program_running = False

            # Join the thread to ensure it terminates
            t.join()
            
            return

        elif user_input == "chat":
            response = chat_with_agent()
            
            # Print the agent's response first
            print("\nAgent's response:", response)
            
            # Then set the engine to a different voice for the chat response
            if selected_voice == 0:
                engine.setProperty('voice', voices[1].id)
            else:
                engine.setProperty('voice', voices[0].id)

            # Read the response out loud
            engine.say(response)
            engine.runAndWait()

            # Revert back to the user's chosen voice for the next chunk
            engine.setProperty('voice', voices[selected_voice].id)
        elif user_input and user_input.isdigit():
            i = int(user_input)
            if i >= len(loaded_chunks):
                print(f"Invalid segment number. There are only {len(loaded_chunks)} segments.")
                i = len(loaded_chunks) - 1
        else:
            i += 1

if __name__ == "__main__":
    main(engine)
