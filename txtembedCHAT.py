import os
import pickle
import json
from datetime import datetime
from gpt4all import GPT4All, Embed4All
from sklearn.metrics.pairwise import cosine_similarity
from rake_nltk import Rake
from textblob import TextBlob
from gensim import corpora, models

# Global variable to store context
context_history = []

guiding_prompt = "I am a Q&A bot with knowledge from the embedded text. Based on this knowledge, "



def get_text_input():
    """Get text input from the user either from a .txt file or directly."""
    choice = input("Do you want to input a .txt file or directly type the text? (Enter 'file' or 'text'): ")

    if choice == 'file':
        file_path = input("Enter the path to your .txt file: ")
        with open(file_path, 'r') as f:
            return f.read()
    elif choice == 'text':
        return input("Enter your text: ")
    else:
        print("Invalid choice. Please enter 'file' or 'text'.")
        return get_text_input()

def chunk_text(text, max_length):
    """Chunk the text into smaller pieces of max_length."""
    return [text[i:i+max_length] for i in range(0, len(text), max_length)]

def get_most_similar_texts(query, embeddings, texts, top_n=2):
    """Find the most similar texts based on cosine similarity."""
    embedder = Embed4All()
    query_embedding = embedder.embed(query)
    
    # Calculate cosine similarities
    similarities = [cosine_similarity([query_embedding], [emb])[0][0] for emb in embeddings]
    
    # Get indices of top N most similar texts
    top_indices = sorted(range(len(similarities)), key=lambda i: similarities[i], reverse=True)[:top_n]
    
    return [texts[i] for i in top_indices]

def simple_search(query, texts):
    """Search through the texts for the user's query and return matching results."""
    results = [text for text in texts if query.lower() in text.lower()]
    return results

def update_context(user_input, response, max_length=5):
    global context_history
    context_history.append((user_input, response))
    if len(context_history) > max_length:
        context_history.pop(0)


# Extract main topics from the conversation history
def extract_topics():
    global context_history
    texts = [input + " " + response for input, response in context_history]
    texts = [text.split() for text in texts]
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    ldamodel = models.LdaModel(corpus, num_topics=3, id2word=dictionary, passes=15)
    topics = ldamodel.print_topics(num_words=3)
    return topics


def main():
    # Check if there's an existing embedding
    if os.path.exists("embedding.pkl"):
        with open("embedding.pkl", 'rb') as f:
            embeddings = pickle.load(f)
        choice = input("An existing embedding was found. Do you want to start a new one or continue with the last? (Enter 'new' or 'continue'): ")
        if choice == 'new':
            text = get_text_input()
            # Chunk the text
            chunks = chunk_text(text, 1000)
            
            # Save the original text chunks
            with open("texts.pkl", 'wb') as f:
                pickle.dump(chunks, f)
            
            embeddings = []
            embedder = Embed4All()
            for chunk in chunks:
                embedding = embedder.embed(chunk)
                embeddings.append(embedding)
            with open("embedding.pkl", 'wb') as f:
                pickle.dump(embeddings, f)
        elif choice == 'continue':
            with open("embedding.pkl", 'rb') as f:
                embeddings = pickle.load(f)

    else:
        text = get_text_input()
        chunks = chunk_text(text, 1000)
        
        # Save the original text chunks
        with open("texts.pkl", 'wb') as f:
            pickle.dump(chunks, f)
        
        embeddings = []
        embedder = Embed4All()
        for chunk in chunks:
            embedding = embedder.embed(chunk)
            embeddings.append(embedding)
        with open("embedding.pkl", 'wb') as f:
            pickle.dump(embeddings, f)

    # Load the original texts (chunks)
    with open("texts.pkl", 'rb') as f:
        texts = pickle.load(f)

    # Initialize RAKE for keyword extraction
    rake = Rake()

    # JSON structure for recording conversation
    conversation_log = []

    # Start chatbot conversation using the embedding as knowledge base
    model = GPT4All(model_name='orca-mini-3b.ggmlv3.q4_0.bin')
    with model.chat_session():
        while True:
            user_input = input("You: ")
            if user_input.lower().startswith("search:"):
                # Extract the actual search query from the user's input
                search_query = user_input[len("search:"):].strip()
                search_results = simple_search(search_query, texts)
                
                # Display the search results
                if search_results:
                    response_content = "\n".join(search_results)
                    print(f"Search Results:\n{response_content}")
                else:
                    response_content = "No results found for your search query."
                    print(response_content)
            else:
                if user_input.lower() in ['exit', 'quit']:
                    break

            # Extract keywords from user input
            rake.extract_keywords_from_text(user_input)
            keywords = rake.get_ranked_phrases()

            # Sentiment analysis
            blob = TextBlob(user_input)
            sentiment = blob.sentiment.polarity

            # Get the most similar texts based on user input
            context_texts = get_most_similar_texts(user_input, embeddings, texts)
            context = " ".join(context_texts)

            # Construct the full prompt
            full_prompt = guiding_prompt + context + " " + user_input

            response = model.generate(prompt=full_prompt, temp=0)
            if isinstance(response, dict) and 'content' in response:
                print(f"Chatbot: {response['content']}")
                response_content = response['content']
            else:
                print(f"Chatbot: {response}")
                response_content = response
            
            # Update context after generating a response
            update_context(user_input, response_content)

            # Record to JSON

            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            entry = {
                "timestamp": timestamp,
                "user_input": user_input,
                "keywords": keywords,
                "sentiment": "positive" if sentiment > 0 else "negative" if sentiment < 0 else "neutral",
                "response": response_content
            }
            conversation_log.append(entry)


    # Save conversation log to JSON file
    with open("conversation_log.json", "w") as f:
        json.dump(conversation_log, f, indent=4)

if __name__ == "__main__":
    main()
