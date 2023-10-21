from pytube import YouTube
import json
import openai
import numpy as np
import pandas as pd
import os
from youtube_transcript_api import YouTubeTranscriptApi
from gpt4all import GPT4All, Embed4All
from gtts import gTTS
import time
from pydub import AudioSegment


# sort of insync tts of the transcript, for saving an mp3 to listen along side instead of video audio. 🤷‍♂️
# commented out in the mainloop 'cause it takes ages to glue the track together
def transcript_to_audio(transcript_path, output_folder, total_duration_seconds):
    with open(transcript_path, 'r') as file:
        transcript_data = json.load(file)
    
    # Create a list to hold all the audio segments
    audio_segments = []
    
    # Convert each segment of text to audio
    previous_end_time = 0  # Initialize end time of the previous segment
    
    for index, entry in enumerate(transcript_data):
        # Calculate the silence duration needed before this segment
        silence_duration = (entry["start"] - previous_end_time) * 1000  # Convert to milliseconds
        silence = AudioSegment.silent(duration=silence_duration)
        audio_segments.append(silence)
        
        text = entry["content"]
        tts = gTTS(text=text, lang='en')  # Convert text to speech
        
        # Save to a temporary file
        temp_file = f"{output_folder}/temp_{entry['start']}.mp3"
        tts.save(temp_file)
        audio_segments.append(AudioSegment.from_mp3(temp_file))
        
        previous_end_time = entry["end"]  # Update the end time
        
        # Remove the temporary audio file after appending it to the audio_segments list
        os.remove(temp_file)
        
        # To avoid hitting the rate limit, consider adding a sleep
        time.sleep(0.5)
    
    # Add silence for the remaining duration after the last segment
    remaining_silence_duration = (total_duration_seconds - previous_end_time) * 1000
    audio_segments.append(AudioSegment.silent(duration=remaining_silence_duration))
    
    # Concatenate all audio segments into a single audio file using pydub
    combined_audio = sum(audio_segments)
    
    final_audio_file = f"{output_folder}/transcript_audio.mp3"
    combined_audio.export(final_audio_file, format="mp3")
    
    print(f"Transcript audio saved to {final_audio_file}")



model = "mistral trismegistus"

OPENAI_ENGINE = "model"
OPENAI_API_KEY = 'not needed for a local LLM'
openai.api_key = OPENAI_API_KEY
openai.api_base = "http://localhost:4892/v1"
#openai.api_base = "https://api.openai.com/v1"

def download_video(video_url, output_folder):
    yt = YouTube(video_url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    video_duration = yt.length  # This gives the video duration in seconds
    stream.download(output_path=output_folder)
    return video_duration  # Return the duration for further processing

def extract_transcript(video_url, output_folder):
    # Ensure the output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    video_id = video_url.split("v=")[1].split("&")[0]  # Extract video ID from URL
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        data = []
        all_content = []  # List to store all the content
        for entry in transcript:
            data_entry = {
                "start": entry["start"],
                "end": entry["start"] + entry["duration"],
                "content": entry["text"]
            }
            data.append(data_entry)
            all_content.append(entry["text"])  # Append content to the list

        with open(f"{output_folder}/transcript.json", "w") as file:
            json.dump(data, file, indent=4)

        # Write only the content to a separate document
        with open(f"{output_folder}/content_only.txt", "w") as file:
            file.write(' '.join(all_content))  # Join content with a space and write to file

    except Exception as e:
        print(f"Error fetching transcript: {e}")


def embed_transcript(transcript_path, output_folder):
    with open(transcript_path, 'r') as file:
        transcript_data = json.load(file)
    
    embedder = Embed4All()  # Initialize the Embed4All model
    sentences = [entry["content"] for entry in transcript_data]
    embeddings = []

    for sentence in sentences:
        embedding = embedder.embed(sentence.strip())
        embeddings.append(embedding)

    df = pd.DataFrame({
        "text": sentences,
        "embedding": embeddings
    })
    df.to_csv(f"{output_folder}/word_embeddings.csv", index=False)


def distances_from_embeddings(query_embedding, embeddings, distance_metric='cosine'):
    if distance_metric == 'cosine':
        # Convert series to list of arrays and then stack them to form a 2D array
        embeddings = np.vstack(embeddings.tolist())
        
        # Normalize both query and embeddings for cosine similarity
        query_embedding = query_embedding / np.linalg.norm(query_embedding)
        embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)
        distances = -np.dot(embeddings, query_embedding)  # Using negative because we will sort ascending
    else:
        raise ValueError(f"Unsupported distance metric: {distance_metric}")
    return distances

def get_embedding_text(api_key, prompt, embeddings_path):  
    embedder = Embed4All()  # Initialize the Embed4All model
    q_embedding = embedder.embed(prompt.strip())
    df = pd.read_csv(embeddings_path, index_col=0)
    df['embedding'] = df['embedding'].apply(eval).apply(np.array)

    df['distances'] = distances_from_embeddings(q_embedding, df['embedding'].values, distance_metric='cosine')
    returns = []
    for i, row in df.sort_values('distances', ascending=True).head(25).iterrows():
        returns.append(row.name)

    #return "\n".join([f"{i+1}. {segment} " for i, segment in enumerate(returns)])
    return " ... ".join(returns)  # Using "/" to separate segments

def chunk_content(file_path, chunk_size=64):
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Split the content into words and chunk them
    words = content.split()
    chunks = [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
    
    return chunks

def convert_to_srt(transcript_path, output_folder):
    with open(transcript_path, 'r') as file:
        transcript_data = json.load(file)

    srt_content = ""
    for idx, entry in enumerate(transcript_data, start=1):
        start_time = seconds_to_srt_time(entry["start"])
        
        # Check if this is the last subtitle entry or not
        if idx < len(transcript_data):
            # Make sure the end time doesn't overlap with the next subtitle's start time
            next_entry_start_time = transcript_data[idx]["start"]
            end_time = seconds_to_srt_time(min(entry["end"], next_entry_start_time - 0.1))
        else:
            end_time = seconds_to_srt_time(entry["end"])
        
        text = entry["content"].replace("\n", " ")  # Ensure no line breaks in subtitle text
        srt_content += f"{idx}\n{start_time} --> {end_time}\n{text}\n\n"

    with open(f"{output_folder}/transcript.srt", "w") as srt_file:
        srt_file.write(srt_content)


def seconds_to_srt_time(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    milliseconds = (seconds % 1) * 1000
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02},{int(milliseconds):03}"

def hhmmss_to_seconds(timestamp):
    # Check if the timestamp has the expected length
    if len(timestamp) != 6:
        raise ValueError("Timestamp should be in the format hhmmss.")
    
    # Check if all characters in the timestamp are digits
    if not timestamp.isdigit():
        raise ValueError("Timestamp should only contain numerical values.")
    
    hours, minutes, seconds = map(int, [timestamp[:2], timestamp[2:4], timestamp[4:]])
    return hours * 3600 + minutes * 60 + seconds

def search_transcript(api_key, query, content_path, embeddings_path, top_n=3):  
    embedder = Embed4All()  # Initialize the Embed4All model
    q_embedding = embedder.embed(query.strip())
    
    # Chunk the content
    chunks = chunk_content(content_path)
    chunk_embeddings = [embedder.embed(chunk) for chunk in chunks]

    df = pd.DataFrame({
        "text_chunk": chunks,
        "embedding": chunk_embeddings
    })

    df['distances'] = distances_from_embeddings(q_embedding, df['embedding'].values, distance_metric='cosine')
    closest_segments = df.sort_values('distances', ascending=True).head(top_n)['text_chunk'].tolist()

    return closest_segments


def chat_with_transcript(api_key, user_input, embeddings_path):
    def generate_response(api_key, prompt):
        one_shot_prompt = f'''Based on the given context, answer the question: {prompt}'''

        print(f"Input Prompt for Agent: {one_shot_prompt}")
        completions = openai.Completion.create(
            model=model,
            prompt=one_shot_prompt,
            max_tokens=1024,
            n=1,
            temperature=0.2,
            stop=["\n\n"]
        )
        message = completions.choices[0].text
        return message

    text_embedding = get_embedding_text(api_key, user_input, embeddings_path)  # Use the main function
    user_input_embedding = f'Using this context: "{text_embedding}", answer the following question: \n{user_input}'

    response = generate_response(api_key, user_input_embedding)
    #print(f"Response from Agent: {response}")
    return response.strip()

if __name__ == '__main__':
    project_name = input("Enter the project name: ")
    output_folder = os.path.join(os.getcwd(), project_name)
    embeddings_path = f"{output_folder}/word_embeddings.csv"  # Define this here for consistency
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created new project folder named '{project_name}'.")
        video_url = input("Enter the YouTube video URL: ")

        # Extract the transcript and convert it to .srt format
        extract_transcript(video_url, output_folder)
        transcript_path = f"{output_folder}/transcript.json"
        convert_to_srt(transcript_path, output_folder)

        # Embed the transcript
        embed_transcript(transcript_path, output_folder)
        
        # Download the video and get its duration
        video_duration = download_video(video_url, output_folder)
        
        # Convert the transcript to audio
        #transcript_to_audio(transcript_path, output_folder, video_duration)
    
    else:
        print(f"Found existing project folder named '{project_name}'.")
        if not os.path.exists(embeddings_path):
            print("No embeddings found in the project folder.")
            video_url = input("Enter the YouTube video URL: ")

            # Extract the transcript and convert it to .srt format
            extract_transcript(video_url, output_folder)
            transcript_path = f"{output_folder}/transcript.json"
            convert_to_srt(transcript_path, output_folder)

            # Embed the transcript
            embed_transcript(transcript_path, output_folder)
            # Convert the transcript to audio
            transcript_to_audio(transcript_path, output_folder)
            download_video(video_url, output_folder)
        else:
            print("Embeddings already exist in the specified folder.")


while True:
    question = input("Ask me something about the video, 'search <your query>' to search (or type 'exit' to quit): ")

    if question.lower() == 'exit':
        break
    elif question.lower().startswith('search '):
        search_query = question.split('search ', 1)[1]
        results = search_transcript(OPENAI_API_KEY, search_query, f"{output_folder}/content_only.txt", embeddings_path)
        print("Top search results from the transcript:")
        for idx, segment in enumerate(results, start=1):
            print(f"{idx}. {segment}")

    else:
        answer = chat_with_transcript(OPENAI_API_KEY, question, embeddings_path)
        print(f"Answer: {answer}")

