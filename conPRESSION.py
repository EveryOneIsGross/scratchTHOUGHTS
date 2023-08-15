
'''a novel noise-tolerant compression/recovery method for piping truncation protected context into agents'''
import gpt4all
import json
from rake_nltk import Rake
import string

# Global markers for encoding
marker_start = "[["
marker_end = "]]"


# Initialize models
model = gpt4all.GPT4All("orca-mini-3b.ggmlv3.q4_0.bin")
r = Rake(min_length=1, max_length=3)  # Adjust keyword extraction parameters

def strip_punctuation(text):
    """Removes punctuation from the text."""
    return text.translate(str.maketrans('', '', string.punctuation))

def encode(text, summary, reverse=False):
    """Encodes a summary into the spaces of a given text."""
    summary = strip_punctuation(summary)
    encoded = list(text)
    summary_chars = list(summary)[:text.count(" ")]
    space_indices = [i for i, char in enumerate(encoded) if char == " "]
    if reverse:
        summary_chars = summary_chars[::-1]
        space_indices = space_indices[::-1]

    for idx in space_indices:
        encoded[idx] = summary_chars.pop(0) if summary_chars else " "

    return ''.join(encoded)

def basic_keyword_extraction(text):
    keywords = [word for word in text.split() if len(word) > 3]
    return ' '.join(keywords)

def decode(encoded_response, marker_start, marker_end):
    """Decodes a summary and keywords from the encoded response."""
    # Split the encoded response into columns using markers
    columns = [col[len(marker_start)+4:-len(marker_end)] for col in encoded_response]
    
    # Extract keywords using the basic_keyword_extraction function
    extracted_keywords = [basic_keyword_extraction(col) for col in columns]
    
    # Create a list of "extracted encoded keywords"
    keyword_list = []
    for col, keyword in zip(columns, extracted_keywords):
        for word in keyword.split():
            # Check for punctuation next to the keyword and append it
            index = col.find(word)
            punctuation_before = "" if index == 0 or col[index-1].isalnum() else col[index-1]
            punctuation_after = "" if index+len(word) == len(col) or col[index+len(word)].isalnum() else col[index+len(word)]
            keyword_list.append(punctuation_before + word + punctuation_after)
    
    # Write the keywords to a new string
    keyword_string = ' '.join(keyword_list)
    
    # Remove the list of "extracted encoded keywords" from the "Encoded Response"
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

def chat_agent():
    context = ""
    summary = ""  
    column_limit = 80

    response_agent = ChatAgentResponse(model)
    summary_agent = ChatAgentSummary(model)

    while True:
        user_input = input("User: ")
        decoded_context = decode(context, marker_start, marker_end)

        
        response = response_agent.generate_response(user_input, decoded_context)
        summary = strip_punctuation(summary_agent.generate_summary(response))

        print("\nPre-encoded Response:", response)
        print("Pre-encoded Summary:", summary)

        encoded_response = encode(response, summary)
        encoded_lines = [f"{marker_start}{index:03}-{encoded_response[i:i+column_limit]}{marker_end}"
                         for index, i in enumerate(range(0, len(encoded_response), column_limit))]

        encoded_input = encode(user_input, summary)
        encoded_summary = encode(summary, summary)
        
        data = {
            "User": encoded_input,
            "Response": encoded_response,
            "Summary": encoded_summary,
            "Encoded Response": encoded_lines,
            "Decoded Summary": decode(encoded_summary, marker_start, marker_end)

        }

        print(json.dumps(data, indent=4))
        context = ''.join([chunk[len(marker_start)+4:-len(marker_end)] for chunk in encoded_lines])

if __name__ == "__main__":
    chat_agent()
