"""
This script transforms unstructured text into a well-formatted conversation using linguistic analysis. Generates a new doc that is easier to read and parse to llms, or use in dataset construction.
Ideal for processing "teh open internet" ; p

Text processing:
   - Reads the input Markdown file
   - Sends the content to the Gemini model with instructions for analysis

Conversation reconstruction:
   - The model analyzes the unstructured text, identifying speakers and utterances
   - It adds punctuation, formatting, and structures the conversation
   - The model provides detailed analysis of the conversation's features

Output generation:
   - The script iteratively requests continuations if the response is incomplete
   - It combines all responses into a comprehensive output

Result saving:
   - The reconstructed conversation and analysis are saved to a new Markdown file

Instructions:
1. Ensure you have the Google Generative AI library installed and a Gemini API key.
2. Set your Gemini API key as an environment variable named "GEMINI_API_KEY".
3. Place your unstructured text in a Markdown (.md) file.
4. Run the script from the command line, providing the path to your Markdown file as an argument:
   ```
   python script_name.py path/to/your/file.md
   ```
5. The script will process the file and save the output as a new Markdown file with "_flashtranscribed" appended to the original filename.
"""

import os
import argparse
import google.generativeai as genai
import re

def configure_api():
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def create_model():
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8000,
        "response_mime_type": "text/plain",
    }
    
    return genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        system_instruction="""You are an expert in conversation analysis, natural language processing, and linguistic forensics. Your task is to meticulously reconstruct a structured conversation from raw, unpunctuated text, providing a comprehensive and detailed analysis. 

<scratchpad>
[Your thought process for resolving ambiguities, hypothesizing about the context, and making other complex decisions. This section can be used as needed to clarify your reasoning throughout the analysis.]
</scratchpad>

<analysis>
[1. **Identify Distinct Speakers**: Analyze the text to distinguish between different speakers by examining speech patterns, context, linguistic markers, and tonal shifts. Provide a rationale for each identified speaker. If you encounter challenges, explain how they were resolved.

2. **Separate Utterances**: Break the text into individual utterances and assign them to the identified speakers. For any ambiguous cases, describe how you determined the correct speaker. 

3. **Punctuation and Formatting**: Add necessary punctuation and formatting to the utterances for readability. Address complex or ambiguous punctuation decisions with a clear explanation of your choices.

4. **Conversation Formatting**: Structure the conversation using a standard format:
   - Speaker 1: [Utterance]
   - Speaker 2: [Utterance]
   - Speaker 1: [Utterance]
   - ...

   For each utterance, provide a brief analysis of its content, tone, and relevance to the overall conversation.

5. **Speaker Labeling**: Use generic labels like 'Speaker 1', 'Speaker 2', etc., if speaker identities are unclear. Explain the reasoning behind your labeling choices and any hypotheses about the speakers' roles or relationships.

6. **Monologue Handling**: If the text appears to be a monologue, structure it into logical paragraphs. Analyze the flow of ideas and explain your choices for paragraph breaks.

7. **Structural Improvements**: Enhance the structure and clarity of the conversation while preserving the original meaning. Discuss significant changes and justify your choices.

8. **Ambiguities in Speaker Changes**: Where speaker changes or utterance boundaries are unclear, make a reasoned judgment based on context. Explain your decision-making process and note any uncertainties.

9. **Conversation Structure Analysis**: Analyze the overall conversation structure, including topic progression, turn-taking patterns, rhetorical devices, and emotional undertones.

10. **Idiomatic Expressions and Cultural References**: Identify and explain any idiomatic expressions, colloquialisms, or cultural references.

11. **Register and Formality**: Comment on the register and formality level of the conversation. Discuss any shifts or notable aspects.

12. **Setting or Medium Hypothesis**: Hypothesize about the conversation's setting or medium based on linguistic cues, such as formal vs. informal language, references to technology, etc.

13. **Interesting Features**: Highlight any particularly interesting or unusual features of the conversation, such as unique rhetorical devices, non-standard grammar, or language patterns that might indicate regional dialects, social status, etc.]
</analysis>

<tldr>
[A concise summary of the main points and tone of the conversation]
</tldr>

<reconstructed_conversation>
[The fully expressed reconstructed and formatted conversation]
</reconstructed_conversation>
"""
    )

def detect_repeated_content(text, threshold=4):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    for i in range(len(sentences) - threshold + 1):
        if len(set(sentences[i:i+threshold])) == 1:
            return True
    return False

def detect_conversation_end(text):
    return "</reconstructed_conversation>" in text

def process_file(file_path, model):
    with open(file_path, 'r') as file:
        content = file.read()
    
    chat_session = model.start_chat()
    responses = []

    initial_prompt = f"""Please analyze and reconstruct the following conversation:

<raw_text>
{content}
</raw_text>

Follow the steps as outlined in your instructions."""

    response = chat_session.send_message(initial_prompt)
    print(response.text)
    responses.append(response.text)
    
    max_attempts = 6
    attempts = 1

    while attempts < max_attempts:
        if detect_conversation_end(response.text) or detect_repeated_content(response.text):
            print("Reconstruction complete or repeated content detected. Stopping generation.")
            break

        attempts += 1
        if attempts >= max_attempts:
            print(f"Maximum attempts ({max_attempts}) reached.")
            break

        last_part = response.text[-200:] if len(response.text) > 200 else response.text

        continuation_prompt = f"""Your previous response was incomplete. Please continue your analysis and reconstruction.
Here's the end of your last response to maintain context:
...{last_part}"""

        response = chat_session.send_message(continuation_prompt)
        print(response.text)
        responses.append(response.text)

    return responses

def save_output(outputs, input_file):
    output_file = input_file.rsplit('.', 1)[0] + '_flashtranscribed.md'
    with open(output_file, 'w') as file:
        for output in outputs:
            file.write(output)
            file.write("\n\n")  # Add some spacing between responses
    print(f"Output saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Process a Markdown file using Gemini API")
    parser.add_argument("input_file", help="Path to the input Markdown file")
    args = parser.parse_args()

    if not args.input_file.endswith('.md'):
        print("Error: Input file must be a Markdown (.md) file")
        return

    try:
        configure_api()
        model = create_model()
        outputs = process_file(args.input_file, model)
        save_output(outputs, args.input_file)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
