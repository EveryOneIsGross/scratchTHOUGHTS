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

def configure_api():
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def create_model():
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8000,
        "response_mime_type": "text/plain",
        "stop_sequences": ["</reconstructed_conversation>"]
    }
    
    return genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        system_instruction="""You are an expert in conversation analysis, natural language processing, and linguistic forensics. Your task is to meticulously reconstruct a structured conversation from raw, unpunctuated text, providing a comprehensive and detailed analysis. Follow these steps carefully:

Here is the raw text input:

<raw_text>
{{RAW_TEXT}}
</raw_text>

Analyze the text and reconstruct the conversation following these steps:

1. Identify distinct speakers through analysis of speech patterns, context clues, linguistic markers, and tone shifts. Explain your reasoning for each speaker identification.

2. Separate the text into individual utterances, assigning each to the appropriate speaker. Discuss any challenges encountered and how you resolved them.

3. Add punctuation and formatting to improve readability, including capitalization, appropriate ending punctuation, and necessary internal punctuation. Explain your choices for complex or ambiguous cases.

4. Format the conversation using this structure:

   Speaker 1: [Utterance]
   Speaker 2: [Utterance]
   Speaker 1: [Utterance]
   ...

   Provide a brief analysis of each utterance's content, tone, and relevance to the overall conversation.

5. Use generic labels like 'Speaker 1', 'Speaker 2', etc., if speaker identities are unclear. Explain your labeling choices and any hypotheses about speakers' roles or relationships based on context.

6. If the text is a monologue, format it into logical paragraphs, analyzing the flow of ideas and explaining your paragraph breaks.

7. Improve the structure and clarity while preserving original meaning and intent. Describe significant changes and your rationale.

8. For ambiguities in speaker changes or utterance boundaries, make your best judgment based on context. Explain your decision-making process and note uncertainties.

9. Analyze the overall conversation structure, including topic progression, turn-taking patterns, rhetorical devices, and emotional undertones.

10. Identify and explain idiomatic expressions, colloquialisms, or cultural references.

11. Comment on the register and formality level of the conversation.

12. Hypothesize about the conversation's setting or medium based on linguistic cues.

13. Highlight any particularly interesting or unusual features of the conversation.

After completing your analysis and reconstruction, provide a TLDR (Too Long; Didn't Read) summary of the conversation, capturing its main points and overall tone in a concise paragraph.

Present your output in the following format:

<analysis>
[Your detailed analysis following the steps above]
</analysis>

<tldr>
[A concise summary of the main points and tone of the conversation]
</tldr>

<reconstructed_conversation>
[The fully expressed reconstructed and formatted conversation]
</reconstructed_conversation>

Additional guidelines:
- If your response is cut short, continue your analysis in the next message without reintroducing XML tags that have already been opened.
- Ensure all XML tags are properly closed before starting a new section.
- If you need to think through any part of the analysis, use <scratchpad> tags to show your thought process.
- Be thorough in your analysis, but avoid repetition or unnecessary verbosity.
- If the raw text is particularly long or complex, you may break down your analysis into smaller sections, clearly labeling each part.

Remember, your goal is to provide a comprehensive, insightful, and well-structured analysis of the conversation, making it as clear and understandable as possible for the reader."""
    )

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
        if "</reconstructed_conversation>" in response.text:
            print("Reconstruction complete. Stopping generation.")
            break

        attempts += 1
        if attempts >= max_attempts:
            print(f"Maximum attempts ({max_attempts}) reached without finding </reconstructed_conversation>.")
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
