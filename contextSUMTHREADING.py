'''Chat Agent Summary Context Encoding:
This method leverages a unique way to compress information by embedding a summary directly into the original response, capitalizing on the spaces within the text. It's a dual-layered approach that provides both the primary response and its associated summary.

1. Encoding:
Objective: To embed the summary into the original response.

Formula:

Count the number of spaces in the original response.
Extract characters from the summary equal to the number of spaces in the response.
Replace each space in the response with a character from the summary. If the summary is shorter than the available spaces, fill the remaining spaces with extracted keywords.
Reverse Encoding: For more obfuscation, the summary can be threaded backward into the response, using a technique reminiscent of the ancient "Boustrophedon" writing style where lines alternate in reading direction.

2. Decoding:
Objective: To retrieve the original response using the provided summary.
Formula:
For each character in the encoded text, if it matches a character from the summary, replace it with a space.
Any "X" characters are also reverted back to spaces.
3. Summary Generation:
Uses a combination of simple truncation and keyword extraction methods to generate a summary.
Initially, it tries to fit as many initial characters from the response as there are spaces available.
If that's too long, it uses the RAKE algorithm to extract keywords from the response.
If the result is still too long, it uses a basic keyword extraction method that favors longer words.
Column Method (Tablets of Dense Text):
This method involves dividing the encoded response into smaller chunks, or "columns." The motivation behind this approach is to create easily digestible segments that can be stored, transmitted, or processed separately.

Objective: To partition the long encoded response into smaller segments.
Formula:
Determine a column_limit which dictates the maximum length of each segment.
Divide the encoded response into segments (columns) based on this limit.
This segmented approach resembles the storage of data in "tablets" of dense text. By doing so, it's easier to manage, retrieve, or process specific parts of the information without the need to handle the entire text. Additionally, if the beginning or end of a text segment is lost (e.g., due to token truncation), the adjacent "tablets" or segments might provide some context due to the encoding method used.

Use Case & Benefits:
Efficiency in Storage: By embedding the summary within the response, you effectively use spaces, which would otherwise not carry meaningful information, to provide an extra layer of context.

Dual Context Retrieval: The embedded summary can be extracted and used to recall or understand the broader context of the discussion, especially useful for chat agents that face token truncation or context loss issues.

Lightweight Encryption: The encoded message has a form of obfuscation which can be decoded by those who understand this specific compression method.

Managing Token Truncation: The column method, combined with the encoding approach, ensures that even if the start or end of a segment is lost, the adjacent segments provide some context, aiding in information retrieval.

In summary, this method offers a blend of compression, encryption, and efficient storage, making it a potentially valuable tool for chat agents or any system that requires context-rich interactions in a limited space.'''
'''
It seems like you're suggesting an alternative approach for the decoding process. Your idea involves extracting keywords from columns of encoded text, removing those keywords from the string, and then attempting to decode in both forward and backward directions if necessary. This approach aims to recover the original response by leveraging the presence or absence of keywords.

Here's a high-level explanation of how this alternative decoding method might work:

Extract Keywords from Columns:

For each column in the encoded response, extract keywords using a keyword extraction algorithm.
Store the extracted keywords for each column.
Remove Keywords:

Remove the extracted keywords from the encoded text to obtain a string without those keywords.
Decoding Attempt - Forward Direction:

Attempt to decode the string in the forward direction using the summary.
If successful, you have recovered the original response.
Decoding Attempt - Backward Direction:

If the forward decoding attempt fails, attempt to decode the string in the backward direction using the summary.
If successful, you have recovered the original response.'''
'''
Simple explanation:
 You have an idea for a chat agent that can talk to people and remember the context of the conversation. To do this, you use a special method that makes the chat agents messages shorter and smarter. You make the chat agent say the main idea of the message in a few words, and then you hide those words in the rest of the message by replacing some spaces with them. This way, you can save space and keep the context of the conversation. You also divide the chat agents messages into smaller parts, so that they are easier to store and process. You call this method chat agent summary context encoding.

Intermediate explanation:
 You have developed a novel method for compressing, encrypting, and storing information for chat agents. Your method leverages a unique way of embedding a summary directly into the original response, capitalizing on the spaces within the text. Its a dual-layered approach that provides both the primary response and its associated summary. You also use a column method that partitions the long encoded response into smaller segments, or “columns.” This segmented approach resembles the storage of data in “tablets” of dense text. By doing so, you can achieve efficiency in storage, dual context retrieval, lightweight encryption, and managing token truncation. You call this method chat agent summary context encoding.

Advanced explanation:
You have designed and implemented a chat agent summary context encoding method that offers a blend of compression, encryption, and efficient storage for chat agents or any system that requires context-rich interactions in a limited space. Your method consists of three main components: encoding, decoding, and summary generation. The encoding component embeds the summary into the original response by replacing each space in the response with a character from the summary. If the summary is shorter than the available spaces, it fills the remaining spaces with extracted keywords. The encoding component also uses a reverse encoding technique for more obfuscation, which threads the summary backward into the response. The decoding component retrieves the original response using the provided summary by replacing each character in the encoded text that matches a character from the summary with a space. The summary generation component uses a combination of simple truncation and keyword extraction methods to generate a summary. It initially tries to fit as many initial characters from the response as there are spaces available. If thats too long, it uses the RAKE algorithm to extract keywords from the response. If the result is still too long, it uses a basic keyword extraction method that favors longer words. The column method partitions the long encoded response into smaller segments based on a column limit. It also adds markers and column indices to each segment for easier identification and retrieval. You call this method chat agent summary context encoding.'''

import gpt4all
import json
from rake_nltk import Rake
from collections import Counter

model = gpt4all.GPT4All("orca-mini-3b.ggmlv3.q4_0.bin")
r = Rake()

def encode(text, summary, reverse=False):
    encoded = list(text)
    spaces_to_fill = text.count(" ")
    summary_chars = list(summary)[:spaces_to_fill]
    
    if reverse:
        summary_chars = summary_chars[::-1]
        space_indices = [i for i, char in enumerate(encoded) if char == " "][::-1]
    else:
        space_indices = [i for i, char in enumerate(encoded) if char == " "]
    
    for i in range(spaces_to_fill):
        if summary_chars:
            encoded[space_indices[i]] = summary_chars.pop(0)
        else:
            keyword_fill = basic_keyword_extraction(text).replace(" ", "")
            while keyword_fill and i < len(space_indices):
                encoded[space_indices[i]] = keyword_fill[0]
                keyword_fill = keyword_fill[1:]
                i += 1

    return ''.join(encoded)

def decode(encoded_text, summary):
    decoded = list(encoded_text)
    summary_chars = list(summary)
    additional_keywords = basic_keyword_extraction(encoded_text).replace(" ", "")

    for i, char in enumerate(decoded):
        if char in summary_chars:
            decoded[i] = " "
            summary_chars.remove(char)
        elif char in additional_keywords and not summary_chars:
            decoded[i] = " "
            additional_keywords = additional_keywords.replace(char, "", 1)

    return ''.join(decoded)



class ChatAgentResponse:
    def __init__(self, model):
        self.model = model

    def generate_response(self, prompt, context=""):
        full_prompt = context + " " + prompt if context else prompt
        tokens = []
        for token in model.generate(full_prompt, max_tokens=200, streaming=True):
            tokens.append(token)
        return ''.join(tokens)

class ChatAgentSummary:
    def __init__(self, model):
        self.model = model

    def generate_summary(self, response):
        available_spaces = response.count(" ")
        summary = ''.join(response.split()[:available_spaces])
        if len(summary) > available_spaces:
            summary = rake_keyword_extraction(response).replace(" ", "")
            if len(summary) > available_spaces:
                summary = basic_keyword_extraction(response).replace(" ", "")
        return summary[:available_spaces]

def rake_keyword_extraction(text):
    r.extract_keywords_from_text(text)
    keywords = r.get_ranked_phrases()
    return ''.join(keywords)

def chat_agent():
    context = ""
    summary = ""  # Initialize summary here
    column_limit = 80
    reverse_encoding = False  # Initialize reverse_encoding here

    response_agent = ChatAgentResponse(model)
    summary_agent = ChatAgentSummary(model)

    while True:
        user_input = input("User: ")
        decoded_context = decode(context, summary)  # Use the previous iteration's summary here
        
        response = response_agent.generate_response(user_input, decoded_context)
        summary = summary_agent.generate_summary(response)

        # Print pre-encoded response and summary
        print("\nPre-encoded Response:", response)
        print("Pre-encoded Summary:", summary)

        # Toggle reverse encoding for each iteration
        reverse_encoding = not reverse_encoding

        encoded_response = encode(response, summary, reverse_encoding)
        reverse_encoding = not reverse_encoding

        encoded_lines = [encoded_response[i:i+column_limit] for i in range(0, len(encoded_response), column_limit)]

        # Add the markers and column indices
        marker_start = "[["
        marker_end = "]]"
        for index, chunk in enumerate(encoded_lines):
            encoded_lines[index] = f"{marker_start}{index:03}-{chunk}{marker_end}"

        encoded_input = encode(user_input, summary)
        encoded_summary = encode(summary, summary)
        encoded_decoded_response = encode(decode(encoded_response, summary), summary)
        encoded_decoded_summary = encode(decode(encoded_summary, summary), summary)

        data = {
            "User": encoded_input,
            "Response": encoded_response,
            "Summary": encoded_summary,
            "Encoded Response": encoded_lines,
            "Decoded Response": encoded_decoded_response,
            "Decoded Summary": encoded_decoded_summary
        }

        print(json.dumps(data, indent=4))
        
        # Update the context - stripping the markers and indices
        context = ''.join([chunk[len(marker_start)+4:-len(marker_end)] for chunk in encoded_lines])


def basic_keyword_extraction(text):
    keywords = [word for word in text.split() if len(word) > 3]
    return ' '.join(keywords)

if __name__ == "__main__":
    chat_agent()
