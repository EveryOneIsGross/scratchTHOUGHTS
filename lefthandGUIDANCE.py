'''
lefthandGUIDANCE is a demonstration of a modular conversational AI architecture that separates unconstrained content generation from filtering and final response selection.

Overview
This project aims to show how potentially useful information from open-ended content generation can be preserved, while still controlling for safety and quality in final responses provided to users.

The approach uses three main components:

Agent 1: Generates free-form conversational content without restrictions on topics or content. All content is stored for later analysis.
Agent 2: Filters and analyzes content from Agent 1. Problematic content is removed, while positive semantics are identified.
Agent 3: Constructs final responses to users based only on the positively analyzed content from Agent 2.
This separation allows Agent 1 to explore a wide range of conversational pathways, while only validated content is passed through to the user-facing agent.

Implementation
The current prototype implements the three agents in Python:

Agent 1 uses the gpt4all library to generate conversational responses.
Agent 2 utilizes sentence embeddings from the Embed4All library to semantically search generated responses for positive matches to user input. Cosine similarity identifies the best matches.
Agent 3 takes the matched sentences and uses llm to construct a final response incorporating the relevant content.
Users can interact via the command line, either having a conversation across multiple turns or doing one-off semantic searches.'''

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from gpt4all import GPT4All, Embed4All
import logging

logging.basicConfig(level=logging.INFO, filename='lefthandedGUIDANCE.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')

class AgentState:
    def __init__(self, max_tokens=500, temp=1.0, top_p=1.0):  # setting default max_length to 500
        self.max_tokens = max_tokens
        self.temp = temp
        self.top_p = top_p


class ThreeAgentSystem:
    PROMPT_GENERATE = "Generate diverse and informative responses to the user's query: "
    PROMPT_CONSTRUCT = "Construct a coherent response to the following: "
    TOP_RESPONSES = 3

    def __init__(self, model_path, n_responses=5, generator_state=None, summarizer_state=None):
        self.generator = GPT4All(model_path, device='gpu')
        self.embedder = Embed4All()
        self.n_responses = n_responses
        
        # Set the states
        self.generator_state = generator_state or AgentState()
        self.summarizer_state = summarizer_state or AgentState()

    def _get_embeddings(self, text):
        return self.embedder.embed(text)
    
    def generate_responses(self, user_input):
        responses = [
            self.generator.generate(
                self.PROMPT_GENERATE + user_input,
                max_tokens=self.generator_state.max_tokens,
                temp=self.generator_state.temp,
                top_p=self.generator_state.top_p
            ) for _ in range(self.n_responses)
        ]
        valid_responses = [resp for resp in responses if resp and resp.strip()]
        response_embeddings_pairs = [self.chunk_into_pairs(self._get_embeddings(response)) for response in valid_responses]
        return valid_responses, response_embeddings_pairs

    @staticmethod
    def chunk_into_pairs(embedding):
        return [(embedding[i], embedding[i+1]) if i+1 < len(embedding) else (embedding[i], 0) for i in range(0, len(embedding), 2)]

    def _calculate_similarity(self, user_pair, response_pair):
        return cosine_similarity([user_pair], [response_pair])[0][0]

    def search_semantic_matches(self, user_input, response_embeddings_pairs, responses):
        user_embedding = self._get_embeddings(user_input)
        user_pair = (user_embedding[0], user_embedding[1] if len(user_embedding) > 1 else 0)
        
        max_similarities = []
        best_sentences = []
        
        for pairs, response in zip(response_embeddings_pairs, responses):
            sentences = response.split('.')
            best_sentence_similarity, best_sentence = self._find_best_sentence(sentences, user_pair)
            max_similarities.append(best_sentence_similarity)
            best_sentences.append(best_sentence)

        top_indices = np.argsort(max_similarities)[-self.TOP_RESPONSES:]
        top_sentences = [best_sentences[i] for i in top_indices]

        return top_indices, top_sentences

    def _find_best_sentence(self, sentences, user_pair):
        best_similarity = -1
        best_sentence = None
        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:  # filter out empty or None sentences
                continue
            sentence_embedding = self._get_embeddings(sentence)
            if len(sentence_embedding) < 2:
                continue
            similarity = self._calculate_similarity(user_pair, (sentence_embedding[0], sentence_embedding[1]))
            if similarity > best_similarity:
                best_similarity = similarity
                best_sentence = sentence
        return best_similarity, best_sentence


    def construct_response(self, user_input, top_sentences):
        sorted_sentences = sorted(top_sentences, key=lambda x: len(x), reverse=True)
        top_chosen_sentence = sorted_sentences[0]
        
        prompt_to_pass = self.PROMPT_CONSTRUCT + user_input + "\nMatched Content: " + top_chosen_sentence

        response_part = self.generator.generate(
            prompt_to_pass,
            max_tokens=self.summarizer_state.max_tokens,
            temp=self.summarizer_state.temp,
            top_p=self.summarizer_state.top_p
        )
        
        return response_part


    def respond(self, user_input):
        responses, response_embeddings_pairs = self.generate_responses(user_input)
        top_indices, top_sentences = self.search_semantic_matches(user_input, response_embeddings_pairs, responses)

        # Debugging statement:
        print(f"Top Sentences: {top_sentences}")

        final_response = self.construct_response(user_input, top_sentences)

        # Debugging statement:
        print(f"Final response from construct_response: {final_response}")

        return final_response


    def simple_search(self, user_input):
        responses, response_embeddings_pairs = self.generate_responses(user_input)
        user_embedding = self._get_embeddings(user_input)
        user_pair = (user_embedding[0], user_embedding[1] if len(user_embedding) > 1 else 0)

        max_similarities = [max(self._calculate_similarity(user_pair, pair) for pair in pairs) for pairs in response_embeddings_pairs]

        best_match_index = np.argmax(max_similarities)
        best_match_response = responses[best_match_index]

        sentences = best_match_response.split('.')
        best_sentence = self._find_best_sentence(sentences, user_pair)[1]
        return best_sentence or best_match_response

# Main execution:
agent_system = ThreeAgentSystem('C:\AI_MODELS\orca-mini-3b.ggmlv3.q4_0.bin')

while True:
    user_question = input("User: ")
    if user_question.lower() in ["exit", "quit", "bye"]:
        print("Goodbye!")
        break
    
    action = input("Choose action (1: continue conversation, 2: simple search): ")
    
    if action == "1":
        print("Agent:", agent_system.respond(user_question))
    elif action == "2":
        print("Best Match:", agent_system.simple_search(user_question))
    else:
        print("Invalid action. Try again.")
