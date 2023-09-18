'''
Based on the idea of chujnking info when under the influence of adrelinine here an agent uses sentiment as a switch to have fast concise iterative thoughts or slow speculative wanderings. 
'''

from gpt4all import GPT4All
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import logging

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()


# Logging setup
logging.basicConfig(filename='conversation_log.txt', level=logging.INFO,
                    format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Initialize the GPT4All model
model = GPT4All("orca-mini-3b.ggmlv3.q4_0.bin")

# Initialize histories
state_history = []
chat_history = []

def get_sentiment(text):
    score = sia.polarity_scores(text)["compound"]
    if score > 0.3:
        return "positive"
    elif score < -0.3:
        return "negative"
    else:
        return "neutral"

def get_agent_state(sentiment):
    if sentiment == "positive":
        return "Thoughtful."
    elif sentiment == "negative":
        return "Reactive."
    else:
        return "Calm."

def stop_on_period_callback(token_id, token_string):
    """Stop generation when encountering a period."""
    return '.' not in token_string

def reprompt_and_generate(initial_prompt, max_tokens, temp, reprompts, user_input, stop_on_period=False):
    """Reprompt the model based on the last response and generate expanded ideas."""
    prompt = initial_prompt
    for iteration in range(reprompts):
        if max_tokens <= 50 and stop_on_period:  # Check the flag here
            response = model.generate(prompt, max_tokens=max_tokens, temp=temp, callback=stop_on_period_callback)
            logging.info(f"Agent Response (reprompt iteration {iteration + 1}): {response}")
        else:
            response = model.generate(prompt, max_tokens=max_tokens, temp=temp)
            logging.info(f"Agent Response (reprompt iteration {iteration + 1}): {response}")

        state_history.append(response)
        if iteration == 0:
            prompt = f"Consider the context of this request: '{user_input}' what's the most appropriate response?"
        else:
            prompt = f"Reflecting on previous response: '{response}', how can we delve deeper or refine the response further?"
    return state_history[-1] if state_history else user_input



def format_state_history(state_history, max_tokens=1024):
    """Format state history into a string and truncate if it exceeds max tokens."""
    formatted_history = ""
    for entry in reversed(state_history):
        formatted_entry = f"{entry}\n"
        if len(formatted_history + formatted_entry) > max_tokens:
            break
        formatted_history = formatted_entry + formatted_history
    return formatted_history

def format_chat_history(chat_history, max_tokens=1024):
    """Format chat history into a string and truncate if it exceeds max tokens."""
    formatted_history = ""
    for entry in reversed(chat_history):
        formatted_entry = f"User: {entry['user']}\nBot: {entry['agent']}\n"
        if len(formatted_history + formatted_entry) > max_tokens:
            break
        formatted_history = formatted_entry + formatted_history
    return formatted_history


def generate_response(text):
    sentiment = get_sentiment(text)
    agent_state = get_agent_state(sentiment)
    
    print(f"Agent State: {agent_state}")

    logging.info(f"User Input: {text}")
    logging.info(f"Agent State: {agent_state}")
    logging.info(f"Detected Sentiment: {sentiment}")
    
    # Use state history for recurrent prompts
    state_hist = format_state_history(state_history)
    #prompt_with_state_history = state_hist + text
    prompt_with_state_history = f"Given the {sentiment} sentiment and existing {agent_state} state, when the user says: '{text}', consider previous insight: {state_hist}, respond without questioning."


    # Initial response generation based on sentiment
    if sentiment == "positive":
        initial_response = reprompt_and_generate(prompt_with_state_history, max_tokens=1024, temp=0.7, reprompts=4, user_input=text, stop_on_period=False)
    elif sentiment == "negative":
        initial_response = reprompt_and_generate(prompt_with_state_history, max_tokens=32, temp=0.2, reprompts=8, user_input=text, stop_on_period=True)
    else:
        initial_response = reprompt_and_generate(prompt_with_state_history, max_tokens=512, temp=0.7, reprompts=1, user_input=text, stop_on_period=False)

    # Add the initial response to the chat history
    state_history.append(initial_response)
    chat_history.append({"user": text, "agent": initial_response})
    
    # Summarize the recurrent state history using medium context agent with chat history for broader context
    chat_hist = format_chat_history(chat_history)
    # Summarize the recurrent state history using medium context agent with chat history for broader context
    chat_hist = format_chat_history(chat_history)
    prompt_for_summary = chat_hist + f"Summarise: {state_hist}"
    # Set maximum retry count
    max_retries = 5 

    # Initialize retry count
    retries = 0

    summarized_response = ""

    while len(summarized_response.split()) < 16 and retries < max_retries:

        summarized_response = model.generate(prompt_for_summary, max_tokens=2048, temp=0.7)

        retries += 1

    logging.info(f"Summarized Response after {retries} retries: {summarized_response}")

    if len(summarized_response.split()) < 128:
        logging.info("Length condition not met within max retries")

    return summarized_response

def main():
    print("Starting conversation. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Exiting conversation. Goodbye!")
            break
        response = generate_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()
