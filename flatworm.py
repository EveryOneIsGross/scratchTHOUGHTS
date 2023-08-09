'''
   ______
  / o  o \\
 /        \\
/          \\
|          |
|          |
\          /
 \        /
  \______/
'''

import pickle
import numpy as np
from gpt4all import GPT4All
from sentence_transformers import SentenceTransformer

# Load the sentence transformer model
model_st = SentenceTransformer('distilbert-base-nli-mean-tokens')

# Load the GPT4All model
model_gpt = GPT4All("orca-mini-3b.ggmlv3.q4_0.bin")

# Function to compute sentence embeddings
def get_embedding(sentence):
    return model_st.encode([sentence])

# Function to compute euclidean distance between two embeddings
def compute_euclidean_distance(embedding1, embedding2):
    return np.linalg.norm(embedding1 - embedding2)

def gpt4all_generate(query, max_tokens, temp=1.0, top_k=50, top_p=0.95): 
    return model_gpt.generate(prompt=query, max_tokens=max_tokens, temp=temp, top_k=top_k, top_p=top_p, streaming=False)

def stress_test_gpt4all(query, token_limit=1, similarity_threshold=0.7, max_attempts=10):
    temperature_effects = {}
    failed_responses = []
    
    for temp in np.linspace(0, 1, max_attempts):  # Loop over temperatures
        full_response = gpt4all_generate(query, token_limit*5, temp)  # Generate a slightly longer response
        truncated_response = full_response[:token_limit]  # Truncate the response
        
        embedding_query = get_embedding(query)
        embedding_full_response = get_embedding(full_response)
        embedding_truncated_response = get_embedding(truncated_response)
        
        distance_full = compute_euclidean_distance(embedding_query, embedding_full_response)
        distance_truncated = compute_euclidean_distance(embedding_query, embedding_truncated_response)
        
        temperature_effects[f"Temp {temp:.2f}"] = {
            'full_response': full_response,
            'truncated_response': truncated_response,
            'distance_full': distance_full,
            'distance_truncated': distance_truncated
        }

        print(f"Temperature = {temp:.2f}, Full Response = '{full_response}', Distance = {distance_full:.2f}")
        print(f"Temperature = {temp:.2f}, Truncated Response = '{truncated_response}', Distance = {distance_truncated:.2f}")
        
        if distance_truncated > similarity_threshold:
            failed_responses.append({'response': truncated_response, 'distance': distance_truncated})

    results = {
        'query': query,
        'temperature_effects': temperature_effects,
        'failed_responses': failed_responses
    }
    
    return results

# Running the stress test and saving results
while True:
    user_query = input("Enter your query (or type 'exit' to quit): ")
    if user_query.lower() == 'exit':
        break

    max_attempts = int(input("Enter the maximum number of attempts (e.g., 10): "))
    results = stress_test_gpt4all(user_query, max_attempts=max_attempts)

    # Save results to a pickle file
    with open('stress_test_results.pkl', 'ab') as file:
        pickle.dump(results, file)

    print("\nResults saved to 'stress_test_results.pkl'.")


import pickle
from gpt4all import GPT4All
import numpy as np
from sentence_transformers import SentenceTransformer
from sentence_transformers import util
from numpy import dot
from numpy.linalg import norm




# Load the sentence transformer model
model_st = SentenceTransformer('distilbert-base-nli-mean-tokens')

# Load the GPT4All model
model_gpt = GPT4All("C://AI_MODELS//llama2_7b_chat_uncensored.ggmlv3.q4_0.bin")

# Load the results from the pickle file
results = []
with open('stress_test_results.pkl', 'rb') as file:
    while True:
        try:
            data = pickle.load(file)
            results.append(data)
        except EOFError:
            break

def get_embedding(sentence):
    tensor_output = model_st.encode([sentence])[0]
    return tensor_output



def cosine_similarity(v1, v2):
    return dot(v1, v2) / (norm(v1) * norm(v2))

def get_response_from_gpt4all(query, max_tokens=100):
    tokens = []
    for token in model_gpt.generate(query, max_tokens=max_tokens, streaming=True):
        tokens.append(token)
    return ''.join(tokens)

# Shortened context
context = """
We've been starving agents of tokens.
"""

def get_enhanced_query(user_query):
    user_embedding = get_embedding(user_query)
    
    # Get the most relevant result based on cosine similarity
    most_relevant_result.get('final_response', 'No response available')

    
    # Simplified context
    enhanced_query = f"User's question: {user_query}\n\nContext: We've been stress testing the GPT4All model. In a related test, we asked '{most_relevant_result['query']}' and the model responded with '{most_relevant_result['final_response']}'. What's the best answer to the user's query based on this?"
    
    return enhanced_query


# Check if all results have the 'query' key
for i, result in enumerate(results):
    if 'query' not in result:
        print(f"Result at index {i} is missing the 'query' key: {result}")

# If all is fine, then compute embeddings
result_embeddings = [get_embedding(result['query']) for result in results if 'query' in result]


def find_most_relevant_result(user_query_embedding):
    similarities = [util.pytorch_cos_sim(user_query_embedding, result_embedding).numpy()[0][0] for result_embedding in result_embeddings]
    most_relevant_index = np.argmax(similarities)
    return results[most_relevant_index]


# Conversational loop
print("You can ask questions about the stress test results. Type 'exit' to end the conversation.")
while True:
    user_query = input("Your question: ")
    
    if user_query.lower() == 'exit':
        break
    
    user_query_embedding = get_embedding(user_query)
    most_relevant_result = find_most_relevant_result(user_query_embedding)
    
    # Create an enhanced prompt with context and the most relevant result
    enhanced_query = f"User's question: {user_query}\n\nContext: We've been stress testing the GPT4All model. In a related test, we asked '{most_relevant_result['query']}' and the model responded with '{most_relevant_result.get('final_response', 'No response available')}'. What's the best answer to the user's query based on this?"

    
    response = get_response_from_gpt4all(enhanced_query, max_tokens=2000)
    
    print("Response:", response)
