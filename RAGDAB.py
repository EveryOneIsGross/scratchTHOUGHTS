"""
RAGDAB: Retrieval-Augmented Generation Dynamically Adjusted emBEDDINGS

- Reads and preprocesses a text file into a corpus, breaking down the text into manageable chunks.
- Utilizes Word2Vec from gensim to create word embeddings, converting sentences in the corpus into vector representations.
- Allows users to perform cosine similarity searches in the corpus using their query, returning the most relevant sentences.
- Enables users to interactively fine-tune the model by providing feedback to increase or decrease the relevance of certain phrases or words in the corpus. This feedback modifies the corpus and retrains the Word2Vec model, making the tool adapt to user inputs over time.
- Utilizes the OpenAI API to generate new sentence contexts for phrases specified by the user, enhancing the diversity and relevance of the corpus.

Usage:
The script runs in an interactive mode, prompting the user to input a file path for the text corpus, perform searches using queries, and provide feedback for model fine-tuning. The script continually updates the Word2Vec model based on user inputs, refining the relevance of search results over time.

Dependencies:
- gensim
- nltk
- numpy
- scipy
- smart_open
- openai
"""


import gensim
from gensim.models import Word2Vec
import smart_open
import numpy as np
from scipy.spatial.distance import cosine
import nltk
from nltk.tokenize import word_tokenize
import openai

nltk.download('punkt')

# Parameters
CHUNK_SIZE = 16
TOP_K = 5

openai.api_base = "http://localhost:4891/v1"
OPENAI_API_KEY = "your-openai-api-key"  # Replace with your OpenAI API key
openai.api_key = OPENAI_API_KEY

# Functions
def read_and_preprocess(file_path, chunk_size=CHUNK_SIZE):
    with smart_open.smart_open(file_path, encoding="utf-8") as f:
        chunk = []
        for line in f:
            words = gensim.utils.simple_preprocess(line)
            chunk.extend(words)
            while len(chunk) >= chunk_size:
                yield chunk[:chunk_size]
                chunk = chunk[chunk_size:]

def train_word2vec(corpus):
    return Word2Vec(sentences=corpus, vector_size=100, window=5, min_count=1, workers=4)

def get_sentence_vector(model, sentence):
    words = gensim.utils.simple_preprocess(sentence)
    word_vectors = [model.wv[word] for word in words if word in model.wv]
    return np.mean(word_vectors, axis=0) if word_vectors else np.zeros(model.vector_size)

def cosine_search(model, query, corpus, top_k=TOP_K):
    query_vector = get_sentence_vector(model, query)
    distances = [(sentence, cosine(query_vector, get_sentence_vector(model, ' '.join(sentence))))
                 for sentence in corpus]
    return sorted(distances, key=lambda x: x[1])[:top_k]


def create_diverse_contexts(phrase, num_sentences=5):
    try:
        response = openai.Completion.create(
            model="davinci",
            prompt=f"Create {num_sentences} diverse and meaningful sentences that include the phrase '{phrase}':\n1. ",
            max_tokens=150,
            n=1,
            stop="\n"
        )
        sentences = response['choices'][0]['text'].strip().split('\n')
        return [sentence.split() for sentence in sentences if sentence]
    except Exception as e:
        print(f"Error during OpenAI API call: {e}")
        return []

def increase_relevance(corpus, phrase, increase_factor=10):
    new_contexts = create_diverse_contexts(phrase, increase_factor)
    return corpus + new_contexts

def update_corpus(corpus, phrase, action):
    if action == 'decrease':
        return [sentence for sentence in corpus if ' '.join(sentence).find(phrase) == -1]
    elif action == 'increase':
        return increase_relevance(corpus, phrase)
    return corpus

def main():
    file_path = input("Enter the path to your text file: ")
    corpus = list(read_and_preprocess(file_path))

    model = train_word2vec(corpus)

    while True:
        query = input("Enter your search query (or type 'exit' to quit): ")
        if query.lower() == 'exit':
            break

        results = cosine_search(model, query, corpus)
        for sentence, distance in results:
            print(f"{' '.join(sentence)} - Score: {distance}")

        feedback = input("Enter the word or phrase to update weights for (or type 'none' to skip): ")
        if feedback.lower() == 'none':
            continue

        action = input("Enter the action ('increase' or 'decrease'): ")
        corpus = update_corpus(corpus, feedback, action)
        model.train(corpus, total_examples=len(corpus), epochs=model.epochs)

        print("Model updated based on your feedback.")

if __name__ == "__main__":
    main()