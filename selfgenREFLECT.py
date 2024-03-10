'''
## selfgenREFLECT Flow

- asks for a text file to train the Word2Vec model
- prepares the corpus for including in reflection stage as thoughts
- user input is processed by the first agent
- user input becomes title and response is content
- calls gensturct to provide 'user' 'assistant' output
- tries to save that to json

'''

import json
from gensim.models import Word2Vec
from openai import OpenAI
import pickle
import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import spacy
import numpy as np
import ollama

# Load the SpaCy model for English
nlp = spacy.load("en_core_web_sm")

# Assuming the modified OpenAI class exists as before
client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama',
)

class CustomConversationalAgent:
    def __init__(self, default_model="mistral:instruct", w2v_model_path='w2v_model.pkl', save_file='conversation_history.json'):
        self.default_model = default_model  # Store the default model
        self.current_model = default_model  # Reflects the model currently in use, allows dynamic switching
        #self.genstruct_model = "genstruct"  # Name of the new model for enhanced responses

        self.w2v_model_path = w2v_model_path
        self.save_file = save_file
        self.load_history()
        if os.path.exists(w2v_model_path):
            self.w2v_model = self.load_w2v_model(w2v_model_path)
        else:
            self.w2v_model = None

    def ask(self, user_input):
        self.current_model = self.default_model  # Ensure using the default model for initial response

        # FIXED SYSTEM PROMPT
        system_prompt = "Summarise this concept without preample: "
        self.history.append({"role": "system", "content": system_prompt})

        self.history.append({"role": "user", "content": user_input})

        # LIMIT HISTORY
        if len(self.history) > 2:
            self.history.pop(0)

        response = client.chat.completions.create(
            model=self.current_model,
            temperature=0.5,
            max_tokens=1024,
            top_p=1.5,
            messages=self.history
        )
        assistant_response = response.choices[0].message.content
        self.history.append({"role": "assistant", "content": assistant_response})
        self.save_history()

        return assistant_response


    def prepare_corpus_sentences(self, corpus_path='corpus.txt'):
        """Prepare corpus sentences for similarity comparisons."""
        self.corpus_sentences = []
        with open(corpus_path, 'r', encoding='utf-8') as file:
            corpus_text = file.read()
        
        # Use SpaCy for sentence tokenization and preprocessing
        doc = nlp(corpus_text)
        for sent in doc.sents:
            processed_sentence = ' '.join([token.text.lower() for token in sent if not token.is_punct and not token.is_stop])
            self.corpus_sentences.append(processed_sentence)

    def sentence_vector(self, sentence):
        """Compute the average vector for a sentence."""
        words = sentence.split()
        word_vectors = [self.w2v_model.wv[word] for word in words if word in self.w2v_model.wv.key_to_index]
        if not word_vectors:
            return np.zeros(self.w2v_model.vector_size)
        sentence_vector = np.mean(word_vectors, axis=0)
        return sentence_vector

    def process_with_genstruct(self, title, content):
        persistent_file_path = 'genstruct_outputs.json'
        structured_response = None  # Default response

        # Constructing the prompt for Ollama's generate mode
        genstruct_prompt = f"[[[Title]]]\n {title}\n[[[Content]]]\n {content}\nThe following is an interaction between a user and an AI assistant that is related to the above text.\n[[[User]]]\n"

        try:
            # Using Ollama's generate function instead of the previous client.chat.completions.create
            response = ollama.generate(model='genstruct', prompt=genstruct_prompt)
            gen_text = response['response']  # Extracting the generated text
            
            structured_response = {
                "title": title,
                "content": content,
                "response": gen_text  # Storing the generated response directly
            }

        except Exception as e:
            structured_response = {"error": f"An error occurred: {e}"}

        # Update the persistent JSON storage with the new structure
        try:
            if os.path.exists(persistent_file_path):
                with open(persistent_file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
            else:
                data = {}

            data_key = f"Title: {title} | Content: {content}"
            if data_key not in data:
                data[data_key] = []
            data[data_key].append(structured_response)

            with open(persistent_file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"Failed to update {persistent_file_path}: {e}")

        return structured_response



    def reflect_and_enhance(self):
        if not hasattr(self, 'corpus_sentences'):
            print("Corpus sentences not prepared. Please run prepare_corpus_sentences.")
            return "Reflection not available."

        last_response = self.history[-1]['content'] if self.history and self.history[-1]['role'] == 'assistant' else None
        if not last_response:
            return "I don't have anything to reflect on yet."

        last_response_vector = self.sentence_vector(last_response)
        similarities = []
        for sentence in self.corpus_sentences:
            sentence_vec = self.sentence_vector(sentence)
            similarity = cosine_similarity([last_response_vector], [sentence_vec])[0][0]
            similarities.append((sentence, similarity))

        top_matches = sorted(similarities, key=lambda x: x[1], reverse=True)[:5]
        top_sentences = [match[0] for match in top_matches]

        title = next((item['content'] for item in reversed(self.history) if item['role'] == 'user'), "No recent user input found.")
        content = f"{last_response}\n\n These are your immediate thoughts on the content:\n {' '.join(top_sentences)}."

        # Now, correctly passing both title and content to process_with_genstruct
        enhanced_response = self.process_with_genstruct(title, content)

        return enhanced_response or "Unable to enhance response due to processing error."



    def save_history(self):
        with open(self.save_file, 'w') as f:
            json.dump(self.history, f, indent=4)

    def load_history(self):
        try:
            with open(self.save_file, 'r') as f:
                self.history = json.load(f)
        except FileNotFoundError:
            self.history = []

    def load_w2v_model(self, path):
        with open(path, 'rb') as f:
            w2v_model = pickle.load(f)
        return w2v_model


def sentence_vector(sentence, model):
    """Compute the average vector for a sentence."""
    words = sentence.split()
    word_vectors = [model.wv[word] for word in words if word in model.wv.key_to_index]
    if not word_vectors:  # If no words in the sentence are in the model
        return np.zeros(model.vector_size)
    sentence_vector = np.mean(word_vectors, axis=0)
    return sentence_vector


def train_and_save_w2v_model(text_file_path, model_save_path='w2v_model.pkl'):
    # Read and preprocess text data
    with open(text_file_path, 'r') as file:
        text = file.read()
    sentences = [sentence.split() for sentence in text.split('\n')]
    
    # Train Word2Vec model
    w2v_model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)
    
    # Save trained model
    with open(model_save_path, 'wb') as model_file:
        pickle.dump(w2v_model, model_file)
    print(f"Word2Vec model trained and saved to {model_save_path}")

def main():
    print("Welcome to the Conversational Agent. Type 'quit' to exit.")

    # Ask user for the text file to train the Word2Vec model
    while True:
        print("\n---\nEnter the path to the .txt file for training the Word2Vec model (e.g., 'path/to/your/file.txt'): ", end="")
        text_file_path = input().strip()

        if os.path.isfile(text_file_path):
            train_and_save_w2v_model(text_file_path)
            break
        else:
            print(f"File '{text_file_path}' not found. Please enter a valid file path.")

    # Instantiate the conversational agent
    agent = CustomConversationalAgent()

    # Ensure that the corpus is also prepared for reflection
    corpus_path = text_file_path
    agent.prepare_corpus_sentences(corpus_path)

    # Continue with the conversational loop
    while True:
        print("\n---\nYou: ", end="")
        user_input = input().strip()
        if user_input.lower() == 'quit' or user_input.lower() == 'exit':
            print("\nExiting conversation. Goodbye!")
            break

        # Get the direct response from the agent
        direct_response = agent.ask(user_input)
        print("\nAssistant's Initial Response:\n" + direct_response + "\n")

        # Generate the enhanced response
        enhanced_response = agent.reflect_and_enhance()

        # Handle and format the enhanced response directly
        if enhanced_response:
            if isinstance(enhanced_response, list) or isinstance(enhanced_response, dict):
                formatted_response = json.dumps(enhanced_response, indent=4)
            else:
                formatted_response = enhanced_response
        else:
            formatted_response = "Unable to enhance response due to processing error or invalid response format."

        print("\nEnhanced Response:\n" + formatted_response)

if __name__ == "__main__":
    main()
