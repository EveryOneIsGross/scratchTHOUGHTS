
'''
The following script embeds your conversations.json file and allows you to search for conversations by keyword. It also allows you to summarize a conversation using the "OpenAI" API.

This is the schema of the conversations.json file found in your downloaded OPENAI archive.

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
import openai

# Initialize the Embed4All model once at the start
embedder = Embed4All()

# Initialize the OpenAI API key and base URL
OPENAI_API_KEY = 'NULL'
openai.api_key = OPENAI_API_KEY
openai.api_base = "http://localhost:4891/v1"
MODEL = 'whatever'

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
    Extracts text messages along with selected metadata and the title from the list of conversation data.
    Args:
        conversation_list (list): The list of conversation data.
    Returns:
        List[dict]: A list of dictionaries with text, metadata, and title.
    """
    extracted_data = []
    for conversation in conversation_list:
        title = conversation.get('title', 'No Title')  # Extract the title, default to 'No Title' if not found
        mapping = conversation.get('mapping', {})
        for _, interaction in mapping.items():
            message_data = interaction.get('message', {})
            if message_data and message_data.get('content', {}).get('content_type') == 'text':
                parts = message_data.get('content', {}).get('parts', [])
                text = ' '.join(parts).strip()
                author_role = message_data.get("author", {}).get("role", "N/A")
                if text:  # Add to extracted_data only if text is non-empty
                    extracted_data.append({
                        "title": title,
                        "role": author_role, 
                        "text": text
                    })
    return extracted_data

def get_conversations_by_title(title: str, file_path: str) -> List[dict]:
    """
    Retrieves all conversations with the given title from the saved embeddings.
    Args:
        title (str): The title of the conversations to retrieve.
        file_path (str): Path to the pickle file containing embeddings.
    Returns:
        List[dict]: A list of dictionaries containing conversations with the given title.
    """
    conversations = []
    with open(file_path, 'rb') as f:
        try:
            while True:
                item = pickle.load(f)
                if item['title'] == title:
                    conversations.append(item)
        except EOFError:
            # End of file reached
            pass
    return conversations

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

def chunk_and_condense_text(text: str, chunk_size: int, n_chunks: int) -> str:
    """
    Splits the text into chunks, keeps the first and last n chunks, and adds '...' in the middle.

    Args:
        text (str): The text to be processed.
        chunk_size (int): The size of each chunk in words.
        n_chunks (int): The number of chunks to keep at the start and end.

    Returns:
        str: The condensed text.
    """
    words = text.split()
    total_chunks = len(words) // chunk_size

    if total_chunks <= 2 * n_chunks:
        # If the total number of chunks is less than or equal to twice the number of chunks to keep,
        # return the whole text without truncation.
        return text

    # Split the text into chunks
    chunks = [' '.join(words[i * chunk_size:(i + 1) * chunk_size]) for i in range(total_chunks)]

    # Keep the first and last n chunks
    start_chunks = chunks[:n_chunks]
    end_chunks = chunks[-n_chunks:]

    # Combine the chunks with '...' in the middle
    condensed_text = ' '.join(start_chunks) + ' ... ' + ' '.join(end_chunks)

    return condensed_text


def generate_embeddings_and_save(data: List[dict], file_path: str, chunk_size: int):
    """
    Generates embeddings for a list of texts and metadata using the provided embedder and saves them incrementally.
    Args:
        data (List[dict]): A list of dictionaries with text and metadata.
        file_path (str): Path to the pickle file to save embeddings.
        chunk_size (int): The size of each text chunk.
    """
    with open(file_path, 'wb') as f:
        for item in data:
            text = item.get("text", "")
            if text:
                for chunk in chunk_text(text, chunk_size):
                    embedding = embedder.embed(chunk)  # Use the globally initialized embedder
                    item["embedding"] = embedding
                    pickle.dump(item, f)



def call_agent(text: str, max_tokens: int = 4000) -> str:
    """
    Calls the OpenAI Agent API with a given text and returns the response.
    Args:
        text (str): The text to send to the agent.
        max_tokens (int): The maximum number of tokens to generate.
    Returns:
        str: The text generated by the agent.
    """
    agent_instruction = "The following is a response from a previous conversation. Explain and summarise this text as best you can: \n\n"
    prompt = agent_instruction + text

    try:
        response = openai.Completion.create(
            model=MODEL,  # Replace with the actual model name
            prompt=prompt,
            max_tokens=max_tokens,
            temp = 0.8,
            repeat_penalty = 1.1
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error in calling Agent: {e}")
        return ""



def main():
    # Load conversation data from JSON file
    with open('conversations.json', 'r') as file:
        conversation_data = json.load(file)

    # Extract texts and metadata from the conversation
    extracted_data = extract_text_from_conversation(conversation_data)

    # Path to the embeddings file
    embeddings_file = 'embeddings.pkl'

    # Define the chunk size
    chunk_size = 100  # For example, 100 words per chunk

    # Check if embeddings file exists
    if not os.path.exists(embeddings_file):
        print("Generating new embeddings and saving them incrementally...")

        # Generate a unique filename with timestamp for extracted data
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        extracted_data_file = f'extracted_conversation_data_{timestamp}.json'

        # Save the extracted data to a new JSON file
        with open(extracted_data_file, 'w') as file:
            json.dump(extracted_data, file, indent=4)
        print(f"Extracted data saved to '{extracted_data_file}'.")

        # Generate and save new embeddings
        generate_embeddings_and_save(extracted_data, embeddings_file, chunk_size)
    else:
        print(f"Embeddings file '{embeddings_file}' already exists.")

    # User query loop
    while True:
        # Get user query and role
        user_query = input("Enter your query (or type 'exit' to quit): ")
        if user_query.lower() == 'exit':
            break
        
        user_role = input("Enter the role to search (user, assistant, tool, or all): ").lower()
        if user_role not in ['user', 'assistant', 'tool', 'all']:
            print("Invalid role. Please enter 'user', 'assistant', 'tool', or 'all'.")
            continue

        # Generate embedding for the user query
        query_embedding = embedder.embed(user_query)

        # Open the embeddings file and calculate cosine similarities
        max_similarity = -1
        best_match = None
        with open(embeddings_file, 'rb') as f:
            try:
                while True:
                    item = pickle.load(f)
                    # Filter by role if specified (other than 'all')
                    if user_role != 'all' and item.get('role') != user_role:
                        continue

                    conversation_embedding = item.get("embedding", [])
                    similarity = cosine_similarity(query_embedding, conversation_embedding)
                    if similarity > max_similarity:
                        max_similarity = similarity
                        best_match = item
            except EOFError:
                # End of file reached
                pass

        if best_match:
            print(f"Title: {best_match['title']}\nRole: {best_match['role']}, \nText: {best_match['text']}\nSimilarity: {max_similarity}")

            # Prompt to retrieve all conversations with the same title
            retrieve_all = input(f"Do you want to see all conversations with the title '{best_match['title']}'? (yes/no): ").lower()
            if retrieve_all == 'yes':
                all_conversations = get_conversations_by_title(best_match['title'], embeddings_file)
                for conversation in all_conversations:
                    print(f"\nTitle: {conversation['title']}\nRole: {conversation['role']}, \nText: {conversation['text']}")

            # Ask if the user wants to summarize
            summarize = input("Do you want to summarize this conversation? (yes/no): ").lower()
            if summarize == 'yes':
                # Process text for LLM input
                processed_text = chunk_and_condense_text(best_match['text'], chunk_size=100, n_chunks=3)
                agent_response = call_agent(processed_text)
                print(f"Agent response: {agent_response}")
            else:
                print("Summarization skipped.")
        else:
            print("No matching conversation found.")

if __name__ == "__main__":
    main()

    
