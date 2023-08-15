
'''a novel noise-tolerant compression/recovery method for piping truncation protected context into agents'''
import gpt4all
import json
from rake_nltk import Rake
import string
import math
import json


# Global markers for encoding
marker_start = "[["
marker_end = "]]"
recorded_data = []


# Initialize models
model = gpt4all.GPT4All("orca-mini-3b.ggmlv3.q4_0.bin")
r = Rake(min_length=1, max_length=3)  # Adjust keyword extraction parameters

def strip_punctuation(text):
    """Removes punctuation from the text."""
    return text.translate(str.maketrans('', '', string.punctuation))

def encode(text, summary):
    if not summary:
        return text
    encoded = list(text)
    space_indices = [i for i, char in enumerate(encoded) if char == " "]
    for idx, space_idx in enumerate(space_indices):
        char_to_insert = summary[idx % len(summary)]
        encoded[space_idx] = char_to_insert
    return ''.join(encoded)

def basic_keyword_extraction(text):
    keywords = [word for word in text.split() if len(word) > 3]
    return ' '.join(keywords)

def decode(encoded_response, marker_start, marker_end):
    columns = [col[len(marker_start)+4:-len(marker_end)] for col in encoded_response]
    extracted_keywords = [basic_keyword_extraction(col) for col in columns]
    keyword_list = []
    for col, keyword in zip(columns, extracted_keywords):
        for word in keyword.split():
            index = col.find(word)
            punctuation_before = "" if index == 0 or col[index-1].isalnum() else col[index-1]
            punctuation_after = "" if index+len(word) == len(col) or col[index+len(word)].isalnum() else col[index+len(word)]
            keyword_list.append(punctuation_before + word + punctuation_after)
    keyword_string = ' '.join(keyword_list)
    for keyword in keyword_list:
        encoded_response = encoded_response.replace(keyword, '', 1)
    decoded_summary = ''.join(encoded_response)
    return keyword_string, decoded_summary

class ChatAgentResponse:
    def __init__(self, model):
        self.model = model

    def generate_response(self, prompt, context=""):
        full_prompt = f"{context} {prompt}" if context else prompt
        tokens = [token for token in model.generate(full_prompt, max_tokens=200, streaming=True)]
        return ''.join(tokens)

class ChatAgentSummary:
    def __init__(self, model):
        self.model = model

    def generate_summary(self, response):
        summary = ' '.join(response.split()[:response.count(" ")])
        if len(summary) > response.count(" "):
            summary = rake_keyword_extraction(response).replace(" ", "")
        return summary

def rake_keyword_extraction(text):
    r.extract_keywords_from_text(text)
    keywords = r.get_ranked_phrases()
    return ''.join(keywords)

def pad_encoded_response(encoded_response):
    """Pad the encoded response to achieve a square slab shape."""
    total_chars = len(encoded_response)
    n = math.ceil(math.sqrt(total_chars))  # Determine the side length
    required_chars = n * n
    padding_needed = required_chars - total_chars
    return encoded_response + '.' * padding_needed  # Padding with dots


def find_nearest_square_factors_for_length(length):
    """Find two factors of the given length that are closest to each other."""
    for i in range(int(length**0.5), 0, -1):
        if length % i == 0:
            return i, length // i
    return 1, length  # Shouldn't happen, but just in case

def determine_column_limit_based_on_spaces_and_length(encoded_response):
    """Determine the optimal column limit based on the number of spaces and total length."""
    num_spaces = encoded_response.count(" ")
    total_length = len(encoded_response)
    
    width, height = find_nearest_square_factors_for_length(total_length)
    
    # To decide which one (width or height) to use for the column limit, 
    # choose the one that's closer to the square root of total_length.
    if abs(width - total_length**0.5) < abs(height - total_length**0.5):
        return width
    else:
        return height

def chat_agent():
    context = ""
    summary = ""  

    response_agent = ChatAgentResponse(model)
    summary_agent = ChatAgentSummary(model)

    while True:
        user_input = input("User: ")
        
        # Only decode if context is not empty
        if context:
            decoded_context, _ = decode(context, marker_start, marker_end)
        else:
            decoded_context = ""

        response = response_agent.generate_response(user_input, decoded_context)
        summary = strip_punctuation(summary_agent.generate_summary(response))

        print("\nPre-encoded Response:", response)
        print("Pre-encoded Summary:", summary)

        encoded_response = encode(response, summary)
        padded_encoded_response = pad_encoded_response(encoded_response)
        column_limit = determine_column_limit_based_on_spaces_and_length(padded_encoded_response)
        
        # Split the padded encoded response based on the determined column size
        encoded_lines = [f"[[{column_limit}x{column_limit}-{index:03}]-{padded_encoded_response[i:i+column_limit]}{marker_end}"
                         for index, i in enumerate(range(0, len(padded_encoded_response), column_limit))]

        encoded_input = encode(user_input, summary)
        encoded_summary = encode(summary, summary)
        
        data = {
            "User": encoded_input,
            "Response": padded_encoded_response,
            "Summary": encoded_summary,
            "Encoded Response": encoded_lines,
            "Decoded Summary": decode(encoded_summary, marker_start, marker_end)
        }
        recorded_data.append(data)
        with open("recorded_data.json", "w") as json_file:
            json.dump(recorded_data, json_file, indent=4)


        print(json.dumps(data, indent=4))
        
        # Update the context with the actual response
        context = response



if __name__ == "__main__":
    chat_agent()
