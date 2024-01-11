
'''
.json schema of conversations.json found in your downloaded openai .zip

Title: The title of the conversation or topic.
Create Time: A timestamp for when the conversation was created.
Update Time: A timestamp for the last update to the conversation.
Mapping: This is a complex object that maps unique identifiers to specific messages or interactions within the conversation. Each entry in this mapping includes:
ID: A unique identifier for the interaction.
Message: An object representing the message, which includes:
ID: The message's unique identifier.
Author: Information about the author of the message, including their role (user, assistant, system), name, and any metadata.
Create Time: Timestamp for when the message was created.
Update Time: Timestamp for the last update to the message.
Content: The content of the message, including content type (e.g., text) and the actual message parts.
Status: The status of the message (e.g., finished successfully).
End Turn: Indicates if the message ends the turn.
Weight: Could be related to the importance or impact of the message.
Metadata: Additional information about the message.
Recipient: Who the message is intended for (e.g., all participants).
Parent: The ID of the parent message or interaction, if any.
Children: An array of IDs for any child messages or interactions.
Moderation Results: Information about any moderation actions taken during the conversation.
Current Node: The ID of the current or last interaction in the conversation.
Plugin IDs: IDs for any plugins used during the conversation.
Conversation ID: A unique identifier for the entire conversation.
Conversation Template ID: The ID for the template used for the conversation, if applicable.
Gizmo ID: ID for any gizmo or special feature used in the conversation.
Is Archived: Indicates whether the conversation is archived.
Safe URLs: A list of URLs marked safe during the conversation.
ID: A redundant field, probably the same as the conversation ID, for unique identification.
'''
import json
from gpt4all import Embed4All
from typing import List
import pickle
import numpy as np
import os
import datetime

def cosine_similarity(vec_a: List[float], vec_b: List[float]) -> float:
    """
    Calculate the cosine similarity between two vectors.
    Args:
        vec_a (List[float]): First vector.
        vec_b (List[float]): Second vector.
    Returns:
        float: Cosine similarity between vec_a and vec_b.
    """
    vec_a = np.array(vec_a)
    vec_b = np.array(vec_b)
    return np.dot(vec_a, vec_b) / (np.linalg.norm(vec_a) * np.linalg.norm(vec_b))

def extract_text_from_conversation(conversation_list: list) -> List[dict]:
    """
    Extracts text messages along with selected metadata from the list of conversation data.
    Args:
        conversation_list (list): The list of conversation data.
    Returns:
        List[dict]: A list of dictionaries with text and metadata.
    """
    extracted_data = []
    for conversation in conversation_list:
        mapping = conversation.get('mapping', {})
        for _, interaction in mapping.items():
            message_data = interaction.get('message', {})
            if message_data and message_data.get('content', {}).get('content_type') == 'text':
                parts = message_data.get('content', {}).get('parts', [])
                text = ' '.join(parts).strip()
                author_role = message_data.get("author", {}).get("role", "N/A")
                create_time = message_data.get("create_time")
                if text:  # Add to extracted_data only if text is non-empty
                    extracted_data.append({"role": author_role, "text": text, "create_time": create_time})
    return extracted_data

def chunk_text(text: str, chunk_size: int) -> List[str]:
    """
    Splits the text into smaller chunks.
    Args:
        text (str): The text to be chunked.
        chunk_size (int): The maximum size of each chunk.
    Returns:
        List[str]: A list of text chunks.
    """
    words = text.split()
    chunks = [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks


def generate_embeddings_and_save(data: List[dict], embedder: Embed4All, file_path: str, chunk_size: int):
    """
    Generates embeddings for a list of texts and metadata using the provided embedder and saves them incrementally.
    Args:
        data (List[dict]): A list of dictionaries with text and metadata.
        embedder (Embed4All): The embedding model to use.
        file_path (str): Path to the pickle file to save embeddings.
    """
    with open(file_path, 'wb') as f:
        for item in data:
            text = item.get("text", "")
            if text:
                for chunk in chunk_text(text, chunk_size):
                    embedding = embedder.embed(chunk)
                    item["embedding"] = embedding  # Add the embedding to the dictionary
                    pickle.dump(item, f)  # Save the dictionary including the embedding


def main():
    # Load conversation data from JSON file
    with open('conversations.json', 'r') as file:
        conversation_data = json.load(file)

    # Extract texts and metadata from the conversation
    extracted_data = extract_text_from_conversation(conversation_data)

    # Generate a unique filename with timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    extracted_data_file = f'extracted_conversation_data_{timestamp}.json'

    # Save the extracted data to a new JSON file
    with open(extracted_data_file, 'w') as file:
        json.dump(extracted_data, file, indent=4)

    print(f"Extracted data saved to '{extracted_data_file}'.")

    # Path to the embeddings file
    embeddings_file = 'embeddings.pkl'

    # Define the chunk size
    chunk_size = 100  # For example, 100 words per chunk

    # Check if embeddings file exists
    if not os.path.exists(embeddings_file):
        print("Generating new embeddings and saving them incrementally...")
        embedder = Embed4All()
        generate_embeddings_and_save(extracted_data, embedder, embeddings_file, chunk_size)
    else:
        print(f"Embeddings file '{embeddings_file}' already exists.")

    # User query loop
    while True:
        # Get user query
        user_query = input("Enter your query (or type 'exit' to quit): ")
        if user_query.lower() == 'exit':
            break

        # Initialize the Embed4All model
        embedder = Embed4All()

        # Generate embedding for the user query
        query_embedding = embedder.embed(user_query)

        # Open the embeddings file and calculate cosine similarities
        max_similarity = -1
        best_match = None
        with open(embeddings_file, 'rb') as f:
            try:
                while True:
                    item = pickle.load(f)
                    conversation_embedding = item.get("embedding", [])
                    similarity = cosine_similarity(query_embedding, conversation_embedding)
                    if similarity > max_similarity:
                        max_similarity = similarity
                        best_match = item
            except EOFError:
                # End of file reached
                pass

        if best_match:
            print(f"Best match role: {best_match['role']}, Create Time: {best_match['create_time']}\nText: {best_match['text']}\nSimilarity: {max_similarity}")
        else:
            print("No matching conversation found.")

if __name__ == "__main__":
    main()
