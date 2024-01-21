'''
This script is designed to perform combined semantic and keyword searches on a text file. It processes the text, trains a Word2Vec model to understand the semantics, and then allows you to search the text using both semantic similarity and keyword frequency. Below is a detailed guide on how to use this script and an explanation of its functions, inputs, and outputs.

### How to Use the Script

1. **Prepare a Text File**: Have a .txt file ready with the content you want to analyze.

2. **Run the Script**: Execute the script in a Python environment. Ensure that all required libraries (`gensim`, `numpy`, `scipy`, and `smart_open`) are installed.

3. **Input File Path and Chunk Size**:
   - When prompted, enter the path to your text file.
   - Enter the chunk size (default is 16). This is the number of words per chunk for processing the text.

4. **Enter Search Queries**:
   - Input a query for combined semantic and keyword search.
   - The script will return the most relevant chunks of text based on your query.
   - To exit, type 'exit'.

### Functions in the Script

1. **read_and_preprocess(file_path, chunk_size)**
   - **Inputs**: Path to your text file, chunk size.
   - **Process**: Reads the text file, tokenizes, and splits it into chunks.
   - **Output**: Yields chunks of text as lists of words.

2. **get_or_train_word2vec(corpus, model_path)**
   - **Inputs**: Corpus (processed text chunks), path for saving/loading the model.
   - **Process**: Trains or loads a Word2Vec model.
   - **Output**: A Word2Vec model.

3. **get_sentence_vector(model, sentence)**
   - **Inputs**: Word2Vec model, a sentence (or chunk).
   - **Process**: Converts the sentence to a vector.
   - **Output**: A vector representing the sentence.

4. **semantic_search(model, query, corpus, top_k)**
   - **Inputs**: Word2Vec model, search query, corpus, number of top results (top_k).
   - **Process**: Finds the chunks most semantically similar to the query.
   - **Output**: Top k chunks with their semantic similarity scores.

5. **keyword_search(corpus, keyword, top_k)**
   - **Inputs**: Corpus, keyword, number of top results (top_k).
   - **Process**: Searches for the keyword in each chunk and counts occurrences.
   - **Output**: Top k chunks with their keyword frequency.

6. **combined_search(model, query, corpus, top_k)**
   - **Inputs**: Word2Vec model, search query, corpus, number of top results (top_k).
   - **Process**: Combines results from semantic and keyword searches.
   - **Output**: Top k chunks based on combined semantic similarity and keyword frequency.

7. **main()**
   - **Process**: The main function to run the script interactively.
   - **Outputs**: Results of the combined search for each query.

### Inputs and Outputs

- **Inputs**: Text file path, chunk size, search queries.
- **Intermediate Outputs**: Processed text chunks, Word2Vec model, individual search results.
- **Final Output**: Combined search results based on semantic similarity and keyword frequency for each query.

### Example Usage

Suppose you have a text file `data.txt` about environmental science. You want to find relevant sections about "climate change".

1. Run the script.
2. Enter `data.txt` when prompted for the file path.
3. Enter `16` for chunk size.
4. Enter `climate change` as your query.
5. Review the returned chunks of text that discuss climate change, both semantically and in terms of keyword occurrence.
6. Type 'exit' to end the script.

This script is particularly useful for researchers and analysts working with large text datasets, as it allows for nuanced text search combining both semantic context and specific keyword relevance.
'''

import gensim
from gensim.models import Word2Vec
import smart_open
import numpy as np
from scipy.spatial.distance import cosine
import os
import pickle

# Function to read and preprocess text into chunks
def read_and_preprocess(file_path, chunk_size=16):
    with smart_open.open(file_path, encoding="utf-8") as f:
        chunk = []
        for line in f:
            words = gensim.utils.simple_preprocess(line)
            chunk.extend(words)
            while len(chunk) >= chunk_size:
                yield chunk[:chunk_size]
                chunk = chunk[chunk_size:]

# Function to train or load Word2Vec model
def get_or_train_word2vec(corpus, model_path='word2vec.model'):
    if os.path.exists(model_path):
        model = Word2Vec.load(model_path)
    else:
        model = Word2Vec(sentences=corpus, vector_size=100, window=5, min_count=1, workers=4)
        model.save(model_path)
    return model

# Function to get vector representation of a sentence
def get_sentence_vector(model, sentence):
    words = gensim.utils.simple_preprocess(sentence)
    word_vectors = [model.wv[word] for word in words if word in model.wv]
    return np.mean(word_vectors, axis=0) if word_vectors else np.zeros(model.vector_size)

# Semantic search function
def semantic_search(model, query, corpus, top_k=10):
    query_vector = get_sentence_vector(model, query)
    distances = [(sentence, cosine(query_vector, get_sentence_vector(model, ' '.join(sentence))))
                 for sentence in corpus]
    return sorted(distances, key=lambda x: x[1])[:top_k]

# Keyword search function
def keyword_search(corpus, keyword, top_k=10):
    keyword_results = []
    for sentence in corpus:
        sentence_str = ' '.join(sentence)
        if keyword in sentence_str:
            count = sentence_str.count(keyword)
            keyword_results.append((sentence, count))
    return sorted(keyword_results, key=lambda x: x[1], reverse=True)[:top_k]

# Combined search function
def combined_search(model, query, corpus, top_k=10):
    semantic_results = semantic_search(model, query, corpus, top_k)
    keyword_results = keyword_search(corpus, query, top_k)

    combined_scores = {}
    for sentence, _ in semantic_results:
        sentence_str = ' '.join(sentence)
        combined_scores[sentence_str] = combined_scores.get(sentence_str, 0) + 1
    for sentence, _ in keyword_results:
        sentence_str = ' '.join(sentence)
        combined_scores[sentence_str] = combined_scores.get(sentence_str, 0) + 1

    sorted_combined = sorted(combined_scores.items(), key=lambda x: x[1], reverse=True)
    return [(sentence, score) for sentence, score in sorted_combined][:top_k]

def main():
    file_path = input("Enter the path of your text file: ")
    chunk_size = int(input("Enter chunk size (default 16): ") or "16")

    corpus_path = 'corpus.pkl'
    model_path = 'word2vec.model'

    # Load or process the corpus
    if os.path.exists(corpus_path):
        with open(corpus_path, 'rb') as file:
            corpus = pickle.load(file)
    else:
        corpus = list(read_and_preprocess(file_path, chunk_size))
        with open(corpus_path, 'wb') as file:
            pickle.dump(corpus, file)

    # Load or train the Word2Vec model
    if os.path.exists(model_path):
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
    else:
        model = get_or_train_word2vec(corpus, model_path)
        with open(model_path, 'wb') as file:
            pickle.dump(model, file)

    while True:
        query = input("Enter a query for combined semantic and keyword search (or type 'exit' to quit): ")
        if query.lower() == 'exit':
            break
        results = combined_search(model, query, corpus, top_k=10)
        print(f"Top {len(results)} results for '{query}':")
        for sentence, score in results:
            print(f"\"{sentence}\" - Score: {score}")
        print("\n")

if __name__ == "__main__":
    main()