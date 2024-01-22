import gensim
from gensim.models import Word2Vec
import numpy as np
import smart_open

# Define constants
CHUNK_SIZE = 16
TOP_K = 1

# Function to calculate cosine similarity for vector search
def cosine_similarity(vec_a, vec_b):
    epsilon = 1e-10
    if np.any(np.isnan(vec_a)) or np.any(np.isnan(vec_b)):
        return -1  # Return a low similarity for invalid vectors
    return np.dot(vec_a, vec_b) / (np.linalg.norm(vec_a) * np.linalg.norm(vec_b) + epsilon)

# Function to read and preprocess text into chunks
def read_and_preprocess(file_path, chunk_size=CHUNK_SIZE):
    with smart_open.smart_open(file_path, encoding="utf-8") as f:
        chunk = []
        for line in f:
            words = gensim.utils.simple_preprocess(line)
            chunk.extend(words)
            if len(chunk) >= chunk_size:
                yield chunk
                chunk = []

# Function to train Word2Vec model on the document
def train_word2vec(corpus):
    return Word2Vec(sentences=corpus, vector_size=100, window=5, min_count=1, workers=4)

# Function to get vector representation of a sentence
def get_sentence_vector(model, sentence):
    words = gensim.utils.simple_preprocess(sentence)
    word_vectors = [model.wv[word] for word in words if word in model.wv]
    if not word_vectors:  # Check for empty word_vectors
        return np.zeros(model.vector_size)
    return np.mean(word_vectors, axis=0)

# Function to find the most relevant chunk given an input string and file path
def find_most_relevant_chunk(input_sentence, file_path):
    corpus = list(read_and_preprocess(file_path))
    model = train_word2vec(corpus)

    user_vector = get_sentence_vector(model, input_sentence)
    corpus_vectors = [get_sentence_vector(model, ' '.join(chunk)) for chunk in corpus]

    cosine_results = sorted([(i, cosine_similarity(user_vector, doc_vector)) 
                             for i, doc_vector in enumerate(corpus_vectors)], 
                             key=lambda x: x[1], reverse=True)[:TOP_K]

    return ' '.join(corpus[cosine_results[0][0]])

# Example Usage
file_path = 'SOMETHING.txt'  # Replace with your file path
input_sentence = "Your input string here"
output_chunk = find_most_relevant_chunk(input_sentence, file_path)
print(output_chunk)
