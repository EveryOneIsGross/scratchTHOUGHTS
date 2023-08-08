import openai
import json
import numpy as np
from sentence_transformers import SentenceTransformer

# Set up the OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Load the sentence transformer model
model = SentenceTransformer('distilbert-base-nli-mean-tokens')

# Function to compute sentence embeddings
def get_embedding(sentence):
    return model.encode([sentence])

# Function to compute euclidean distance between two embeddings
def compute_euclidean_distance(embedding1, embedding2):
    return np.linalg.norm(embedding1 - embedding2)

# Function to get a response from OpenAI's DaVinci engine with a token limit and a temperature
def openai_api_call(query, token_limit, temperature):
    response = openai.Completion.create(
      engine="davinci",
      prompt=query,
      max_tokens=token_limit,
      temperature=temperature
    )
    return response.choices[0].text.strip()

def stress_test_openai(query, token_limit=4, similarity_threshold=0.7, initial_temperature=0.5, max_attempts=10):
    iteration = 0
    distance = float('inf')
    failed_responses = []
    temperature = initial_temperature

    while distance > similarity_threshold and iteration < max_attempts:
        iteration += 1
        response = openai_api_call(query, token_limit, temperature)
        embedding_query = get_embedding(query)
        embedding_response = get_embedding(response)
        distance = compute_euclidean_distance(embedding_query, embedding_response)

        # Adjust temperature based on distance
        if distance > 0.8:
            temperature += 0.1  # increase randomness if very dissimilar
        elif distance < 0.2:
            temperature -= 0.1  # decrease randomness if very similar
        temperature = min(1, max(0, temperature))  # Ensure temperature is between 0 and 1

        print(f"Iteration {iteration}: Response = '{response}', Distance = {distance:.2f}, Temperature = {temperature:.2f}")
        if distance > similarity_threshold:
            failed_responses.append({'response': response, 'distance': distance})

    result = {
        "query": query,
        "final_response": response,
        "final_distance": distance,
        "failed_responses": failed_responses
    }

    return result

# Loop to continually take user input and run the stress test
while True:
    user_query = input("Enter your query (or type 'exit' to quit): ")
    if user_query.lower() == 'exit':
        break

    max_attempts = int(input("Enter the maximum number of attempts (e.g., 10): "))
    result = stress_test_openai(user_query, max_attempts=max_attempts)
    print("\nResults:", json.dumps(result, indent=4))

    # Save results to a JSON file
    with open('stress_test_results.json', 'a') as file:
        json.dump(result, file, indent=4)
        file.write("\n")
    print("\nResults saved to 'stress_test_results.json'.")
