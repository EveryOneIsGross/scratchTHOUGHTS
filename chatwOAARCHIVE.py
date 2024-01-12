
'''
DOWNLOAD YOUR OPENAI ARCHIVE EXCTRACT 'conversations.json'
GROUND A LOCAL AGENT WITH RETRIVAL ON YOUR OLD CHATS FROM GPT4

The following script embeds your conversations.json file and allows you to search for conversations by keyword.
It also allows you to summarize a conversation using a LLM. 

### 1. **Initialization and Imports**
- Import necessary libraries like `json`, `numpy`, `pickle`, and modules from `gpt4all` and `openai`.
- Initialize the `Embed4All` model, which is likely used for generating text embeddings.
- Set up the OpenAI API key and base URL for calling OpenAI's API services.

### 2. **Defining Utility Functions**
- `cosine_similarity`: Computes the cosine similarity between two vectors. Used in comparing the similarity between text embeddings.
- `extract_text_from_conversation`: Extracts text from a structured conversation list, storing details like title, role, and text of each message.
- `get_conversations_by_title`: Retrieves all conversations from a file that match a given title.
- `chunk_text`: Breaks down a text into smaller chunks of a specified size. This is useful for processing large texts in manageable segments.
- `chunk_and_condense_text`: A more complex function that chunks the text, computes embeddings, finds chunks most similar to a given query, and returns a condensed version of text focusing on these relevant chunks.
- `generate_embeddings_and_save`: Generates embeddings for text data and saves them into a file. This is likely used for preparing data for efficient similarity searches later.

### 3. **Agent Call Function**
- `call_agent`: This function seems to be a wrapper around OpenAI's API, sending a text to the API and receiving a processed response, likely a summary or analysis of the text.

### 4. **Main Workflow (`main` function)**
- The script reads a JSON file containing conversation data.
- Extracts useful information from this data using `extract_text_from_conversation`.
- Checks for an existing embeddings file, and if not present, generates and saves embeddings using `generate_embeddings_and_save`.
- Enters an interactive loop where the user can input queries and select roles to search conversations.
- For each query, the script:
  - Computes the query's embedding.
  - Searches through saved conversation embeddings for the most similar conversation using cosine similarity.
  - Presents the user with options to see all conversations with the same title or summarize the conversation.
- If the user chooses to see all conversations with the same title, the script aggregates these conversations and updates `current_context`.
- If the user opts for summarization:
  - The script uses `chunk_and_condense_text` to process either the current conversation context or the original matched conversation, based on the user's previous choice.
  - The processed text is then sent to `call_agent` for summarization.
- The summarized text or agent's response is then displayed to the user.

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
    vec_a = np.array(vec_a)
    vec_b = np.array(vec_b)
    return np.dot(vec_a, vec_b) / (np.linalg.norm(vec_a) * np.linalg.norm(vec_b))

def extract_text_from_conversation(conversation_list: list) -> List[dict]:
    extracted_data = []
    for conversation in conversation_list:
        title = conversation.get('title', 'No Title')
        mapping = conversation.get('mapping', {})
        for _, interaction in mapping.items():
            message_data = interaction.get('message', {})
            if message_data and message_data.get('content', {}).get('content_type') == 'text':
                parts = message_data.get('content', {}).get('parts', [])
                text = ' '.join(parts).strip()
                author_role = message_data.get("author", {}).get("role", "N/A")
                if text:
                    extracted_data.append({
                        "title": title,
                        "role": author_role, 
                        "text": text
                    })
    return extracted_data

def get_conversations_by_title(title: str, file_path: str) -> List[dict]:
    conversations = []
    with open(file_path, 'rb') as f:
        try:
            while True:
                item = pickle.load(f)
                if item['title'] == title:
                    conversations.append(item)
        except EOFError:
            pass
    return conversations

def chunk_text(text: str, chunk_size: int) -> List[str]:
    words = text.split()
    chunks = [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

def chunk_and_condense_text(text: str, query: str, chunk_size: int, n_chunks: int) -> str:

    words = text.split()
    total_chunks = len(words) // chunk_size

    if total_chunks <= 2 * n_chunks:
        return text

    chunks = [' '.join(words[i * chunk_size:(i + 1) * chunk_size]) for i in range(total_chunks)]
    chunk_embeddings = [embedder.embed(chunk) for chunk in chunks]
    query_embedding = embedder.embed(query)
    
    similarities = [cosine_similarity(query_embedding, chunk_emb) for chunk_emb in chunk_embeddings]
    sorted_indices = np.argsort(similarities)[::-1]  # Descending order
    best_match_indices = sorted_indices[:n_chunks]  # Take top n_chunks
    
    mid_index = len(best_match_indices) // 2
    start_index = max(0, mid_index - n_chunks // 2)
    end_index = min(len(chunks), start_index + n_chunks)
    
    relevant_chunks = [chunks[i] for i in range(start_index, end_index)]
    condensed_text = ' ... '.join(relevant_chunks)

    return condensed_text


def generate_embeddings_and_save(data: List[dict], file_path: str, chunk_size: int):
    with open(file_path, 'wb') as f:
        for item in data:
            text = item.get("text", "")
            if text:
                for chunk in chunk_text(text, chunk_size):
                    embedding = embedder.embed(chunk)
                    item["embedding"] = embedding
                    pickle.dump(item, f)

def call_agent(text: str, max_tokens: int = 4000) -> str:
    agent_instruction = "The following is a response from a previous conversation. Explain and summarise this text as best you can: \n\n"
    prompt = agent_instruction + text
    try:
        response = openai.Completion.create(
            model=MODEL,
            prompt=prompt,
            max_tokens=max_tokens,
            temp = 0.8,
            repeat_penalty = 1.1
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error in calling Agent: {e}")
        return ""

# Add a global variable to hold the current context
fullthread_context = None

def main():
    global fullthread_context
    with open('conversations.json', 'r') as file:
        conversation_data = json.load(file)
    extracted_data = extract_text_from_conversation(conversation_data)
    embeddings_file = 'embeddings.pkl'
    chunk_size = 100

    if not os.path.exists(embeddings_file):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        extracted_data_file = f'extracted_conversation_data_{timestamp}.json'
        with open(extracted_data_file, 'w') as file:
            json.dump(extracted_data, file, indent=4)
        print(f"Extracted data saved to '{extracted_data_file}'.")
        generate_embeddings_and_save(extracted_data, embeddings_file, chunk_size)
    else:
        print(f"Embeddings file '{embeddings_file}' already exists.")

    while True:
        user_query = input("Enter your query (or type 'exit' to quit): ")
        if user_query.lower() == 'exit':
            break
        user_role = input("Enter the role to search (user, assistant, tool, or all): ").lower()
        if user_role not in ['user', 'assistant', 'tool', 'all']:
            print("Invalid role. Please enter 'user', 'assistant', 'tool', or 'all'.")
            continue
        query_embedding = embedder.embed(user_query)
        max_similarity = -1
        best_match = None
        with open(embeddings_file, 'rb') as f:
            try:
                while True:
                    item = pickle.load(f)
                    if user_role != 'all' and item.get('role') != user_role:
                        continue
                    conversation_embedding = item.get("embedding", [])
                    similarity = cosine_similarity(query_embedding, conversation_embedding)
                    if similarity > max_similarity:
                        max_similarity = similarity
                        best_match = item
            except EOFError:
                pass

        if best_match:
            print(f"Title: {best_match['title']}\nRole: {best_match['role']}, \nText: {best_match['text']}\nSimilarity: {max_similarity}")
            retrieve_all = input(f"Do you want to see all conversations with the title '{best_match['title']}'? (yes/no): ").lower()
            if retrieve_all == 'yes':
                all_conversations_text = []
                all_conversations = get_conversations_by_title(best_match['title'], embeddings_file)
                for conversation in all_conversations:
                    all_conversations_text.append(conversation['text'])
                    print(f"\nTitle: {conversation['title']}\nRole: {conversation['role']}, \nText: {conversation['text']}")
                # Update the current context
                fullthread_context = ' '.join(all_conversations_text)
            summarize = input("Do you want to summarize this conversation? (yes/no): ").lower()
            if summarize == 'yes':
                if fullthread_context:
                    processed_text = chunk_and_condense_text(fullthread_context, user_query, chunk_size, 10)
                else:
                    processed_text = chunk_and_condense_text(best_match['text'], user_query, chunk_size, 3)
                agent_response = call_agent(processed_text)
                print(f"Agent response: {agent_response}")
            else:
                print("Summarization skipped.")


if __name__ == "__main__":
    main()


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

    
