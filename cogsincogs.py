
'''
scratch code attempt at a cognitive model flow for agents

The example agent incorporates a blend of key cognitive frameworks like working memory, long-term declarative memories, associative retrieval, "reasoning" with flows, goal-driven planning and learning from experience. It'll take a user input, parse it through it's framework and print any solutions it found.  

'''


import logging
import json
import random
from numpy import dot
from numpy.linalg import norm
from textblob import TextBlob
from gpt4all import Embed4All, GPT4All

logging.basicConfig(level=logging.INFO)

# Compute the cosine similarity between two vectors
def cosine_similarity(v1, v2):
    return dot(v1, v2) / (norm(v1) * norm(v2))

# Use the Embed4All class to generate embeddings for text
embedder = Embed4All()

class GPTModel:

    def __init__(self, model_path):
        self.model = GPT4All(model_path)
        self.verbose: bool = True,
        # Initialize with a generic prefix; it will be updated during the agent loop
        self.chat_prefix = 'You are a self-aware agent.'
        self.chat_format = '### Instruction:\n{0}\n### Response:\n'

    def construct_dynamic_prefix(self, working_mem):
        """Dynamically construct the chat prefix based on the agent's current state and logic."""
        prefix = 'You are an agent with the following information:\n'
        prefix += 'Observations: ' + ', '.join(working_mem.observations) + '\n'
        prefix += 'Goals: ' + ', '.join(working_mem.goals) + '\n'
        prefix += 'Actions: ' + ', '.join(working_mem.actions) + '\n'
        return prefix

    def update_prefix(self, working_mem):
        """Update the chat prefix when the agent's state changes."""
        self.chat_prefix = self.construct_dynamic_prefix(working_mem)

    def generate_text(self, prompt):
        with self.model.chat_session(self.chat_prefix):
            response = self.model.generate(prompt, temp=0.4, max_tokens=128, repeat_penalty=1.5)
        return response



class WorkingMemory:

    def __init__(self, capacity=3, max_goals=5):
        self.capacity = capacity
        self.max_goals = max_goals  # Maximum number of goals
        self.observations = []
        self.goals = [] 
        self.actions = []
        self.timestamps = []  # To track the time each item is added for decay purposes

    def _decay_items(self):
        """Decay older items if memory exceeds capacity using a FIFO approach."""
        while len(self.observations) > self.capacity:
            if self.observations:
                self.observations.pop(0)
            if self.goals:
                self.goals.pop(0)
            if self.actions:
                self.actions.pop(0)
            if self.timestamps:
                self.timestamps.pop(0)

    def _remove_repeated_goals(self):
        """Remove repeated goals and keep the latest ones."""
        unique_goals = []
        for goal in reversed(self.goals):
            if goal not in unique_goals:
                unique_goals.append(goal)
        self.goals = list(reversed(unique_goals))

    def update(self, new_obs, new_goals, new_actions):
        current_time = len(self.observations)  # For simplicity, using the current length as a timestamp proxy
        self.observations.extend(new_obs)
        self.goals.extend(new_goals)
        self.actions.extend(new_actions)
        self.timestamps.extend([current_time] * len(new_obs))
        
        self._decay_items()
        
        if len(self.goals) > self.max_goals:
            self.goals = self.goals[-self.max_goals:]
        
        self._remove_repeated_goals()

    def retrieve(self, criteria):
        """Retrieve items based on certain criteria. For demonstration, we can filter based on observations."""
        relevant_items = [obs for obs in self.observations if criteria in obs]
        return relevant_items
    
    def display_memory(self):
        """Display the current state of the working memory."""
        return {
            "Observations": self.observations,
            "Goals": self.goals,
            "Actions": self.actions
        }

class EpisodicMemory:

    def __init__(self):
        self.episodes = []
        self.embeddings = []

    def add_episode(self, episode, embedding):
        self.episodes.append(episode)
        self.embeddings.append(embedding)

class SemanticMemory:

    def __init__(self):
        self.facts = []
        self.embeddings = []

    def add_fact(self, fact, embedding):
        self.facts.append(fact)
        self.embeddings.append(embedding)
    
    def load_from_txt(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                # Remove any newline characters and extra spaces
                line = line.strip()
                if line:  # Only process non-empty lines
                    embedding = embedder.embed(line)
                    self.add_fact(line, embedding)

def construct_working_memory_prompt(working_mem, words_per_chunk=10):
    chunked_observations = chunk_memories_by_words(working_mem.observations, words_per_chunk=words_per_chunk)
    prompt = "Recent Observations: " + '; '.join(chunked_observations)
    prompt += "\nRecent Goals: " + ', '.join(working_mem.goals)
    prompt += "\nRecent Actions: " + ', '.join(working_mem.actions)
    return prompt

def construct_episodic_memory_prompt(episodic_mem, max_chunks=None):
    chunked_episodes = chunk_memories(episodic_mem.episodes, chunk_size=3, max_chunks=max_chunks)
    prompt = "Past Events: " + '; '.join([', '.join(chunk) for chunk in chunked_episodes])
    return prompt

def construct_semantic_memory_prompt(semantic_mem, max_chunks=None):
    chunked_facts = chunk_memories(semantic_mem.facts, chunk_size=3, max_chunks=max_chunks)
    prompt = "Known Facts: " + '; '.join([', '.join(chunk) for chunk in chunked_facts])
    return prompt

def construct_prompt(working_mem):
    """Constructs a comprehensive prompt based on the working memory's observations and goals.

    Args:
    - working_mem (WorkingMemory): The working memory object containing observations and goals.

    Returns:
    - str: A verbose prompt.
    """

    # Initialize an empty prompt string
    prompt = ""

    # Extract the observations and goals from working memory
    observations = working_mem.observations
    goals = working_mem.goals

    # Construct the observations part of the prompt
    if observations:
        if len(observations) == 1:
            prompt += f"Latest observation: {observations[0]}.\n"
        else:
            prompt += "Recent observations include:\n"
            for idx, obs in enumerate(observations, 1):
                prompt += f"{idx}. {obs}\n"
    else:
        prompt += "No recent observations.\n"

    # Construct the goals part of the prompt
    if goals:
        if len(goals) == 1:
            prompt += f"Primary goal: {goals[0]}.\n"
        else:
            prompt += "Current goals are:\n"
            for idx, goal in enumerate(goals, 1):
                prompt += f"{idx}. {goal}\n"
    else:
        prompt += "No active goals at the moment.\n"

    return prompt


def parse_response(response, working_mem):
    # Parse response and update working memory
    # Instead of adding the entire response as an action, we'll check if it's not already in observations
    if response not in working_mem.observations:
        working_mem.update(new_obs=[], new_goals=[], new_actions=[response]) 

def reasoning(working_mem, lang_model):
    prompt = construct_prompt(working_mem)
    response = lang_model.generate_text(prompt)
    
    # Analyze the sentiment of the response
    sentiment = get_sentiment(response)
    
    # Use the sentiment for further decision-making or logging
    print(f"Model's Response: {response} (Sentiment: {sentiment})")
    
    parse_response(response, working_mem)

def retrieval(working_mem, long_term_mem, max_chunks=2):
    if isinstance(long_term_mem, EpisodicMemory):
        prompt = construct_episodic_memory_prompt(long_term_mem, max_chunks=max_chunks)
        current_embedding = embedder.embed(prompt)
    elif isinstance(long_term_mem, SemanticMemory):
        prompt = construct_semantic_memory_prompt(long_term_mem, max_chunks=max_chunks)
        current_embedding = embedder.embed(prompt)
    else:
        current_embedding = embedder.embed(construct_working_memory_prompt(working_mem))
    relevant_mem = get_relevant_memories(current_embedding, long_term_mem)
    working_mem.update(relevant_mem, [], [])

def get_sentiment(text):
    """Get the sentiment of a given text using TextBlob.
    
    Args:
    - text (str): The text to analyze.
    
    Returns:
    - str: Either "positive", "negative", or "neutral".
    """
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "positive"
    elif analysis.sentiment.polarity < 0:
        return "negative"
    else:
        return "neutral"

def chunk_memories(memories, chunk_size=3, max_chunks=None):
    """Breaks down a list of memories into chunks."""
    chunks = [memories[i:i+chunk_size] for i in range(0, len(memories), chunk_size)]
    
    if max_chunks:
        return chunks[-max_chunks:]
    return chunks

def chunk_memories_by_words(memories, words_per_chunk=10):
    """Breaks down a list of memories into chunks by words."""
    all_words = ' '.join(memories).split()  # Flatten all memories into a list of words
    chunks = [' '.join(all_words[i:i+words_per_chunk]) for i in range(0, len(all_words), words_per_chunk)]
    return chunks

# Find the memory that is most similar to the current context
def get_relevant_memories(current_embedding, long_term_mem):
    similarities = [cosine_similarity(current_embedding, emb) for emb in long_term_mem.embeddings]
    if not similarities:
        return []
    most_similar_idx = similarities.index(max(similarities))
    return [long_term_mem.episodes[most_similar_idx]]

def serialize_memories(memory_class):
    serialized_data = [{"memory": mem, "embedding": emb.tolist()} for mem, emb in zip(memory_class.episodes, memory_class.embeddings)]
    return json.dumps(serialized_data)

def learning(working_mem, long_term_mem):
    new_experience = construct_prompt(working_mem)
    embedding = embedder.embed(new_experience)
    long_term_mem.add_episode(new_experience, embedding)


def propose_actions(working_mem):

  actions = ["Ask for Clarification", "Retrieve Relevant Memory", "Propose Solution"]

  # Ranking logic
  if len(working_mem.observations) < 2:
    # Not enough context yet, ask for clarification
    actions = ["Ask for Clarification"] + actions

  if not working_mem.goals: 
    # No goals, need to gather more info
    actions = ["Ask for Clarification"] + actions

  if working_mem.actions and working_mem.actions[-1] == "Propose Solution":
    # Don't want to propose a solution twice in a row
    actions.remove("Propose Solution") 
    actions.append("Propose Solution")

  # Log for debugging
  #logging.info("Proposed actions: %s", actions)

  return actions

def evaluate_actions(actions, working_mem):
    values = {}
    
    # Get the embedding of the most recent observation (user input)
    recent_observation = working_mem.observations[-1] if working_mem.observations else ""
    obs_embedding = embedder.embed(recent_observation) if recent_observation else None
    
    # Determine the sentiment of the recent response
    sentiment = get_sentiment(recent_observation) if recent_observation else "neutral"
    
    for action in actions:
        # Compute the embedding for each proposed action
        action_embedding = embedder.embed(action)
        
        # Compute the cosine similarity between the observation and action embeddings
        similarity_score = cosine_similarity(obs_embedding, action_embedding) if obs_embedding else 0
        
        # Assign values to actions based on the similarity score
        values[action] = similarity_score
        
        # Adjust values based on sentiment
        if sentiment == "positive":
            values[action] += 0.1  # Adding a positive bias
        elif sentiment == "negative":
            values[action] -= 0.1  # Adding a negative bias
        # Neutral sentiment doesn't adjust the score

    return values



def select_action(values):
  best_action = max(values, key=values.get) 
  return best_action

def planning(working_mem, actions):
    # Propose actions based on the current state of the working memory
    proposed = propose_actions(working_mem)

    # Evaluate the proposed actions
    values = evaluate_actions(proposed, working_mem)

    # Log the proposed actions and their values (optional but can be useful for debugging and refining logic)
    logging.info(f"Proposed Actions: {proposed}")
    logging.info(f"Evaluated Values: {values}")
    logging.info(f"Best Action: {select_action(values)}")

    # Select the best action based on the evaluated values
    best_action = select_action(values)

    # Feedback loop: if the same action is being repeated, consider asking for clarification or seeking more information
    if working_mem.actions and best_action == working_mem.actions[-1]:
        logging.info("Same action proposed consecutively. Consider revising the logic or seeking more information.")
        # Optional: change the action to something else, like "Ask for Clarification"

    return best_action


def ask_for_clarification():
    return "Can you please provide more details or clarify your last statement?"

def retrieve_relevant_memory(working_mem, episodic_mem, semantic_mem):
    # Get the most recent observation
    obs = working_mem.observations[-1] if working_mem.observations else ""
    
    # For demonstration, let's try to retrieve from the episodic memory first
    memories = episodic_mem.retrieve(obs)
    if memories:
        return "Based on previous events, I recall: " + memories[0]
    
    # If nothing in episodic memory, try semantic memory
    facts = semantic_mem.retrieve(obs)
    if facts:
        return "According to what I know: " + facts[0]
    
    return "I couldn't find relevant information in my memory."

def propose_solution(working_mem):
    # For demonstration, let's use the last observation to generate a solution
    obs = working_mem.observations[-1] if working_mem.observations else ""
    # This can be replaced with more sophisticated logic, e.g., using an expert system or rule-based engine.
    return f"Based on what you said about '{obs}', I suggest ..."

def execute_action(action, working_mem, episodic_mem, semantic_mem, lang_model):

  if action == "Ask for Clarification":
    new_prompt = "Could you please elaborate on " + working_mem.observations[-1]
    new_response = lang_model.generate_text(new_prompt)
    working_mem.update([], [], [new_response])
    return new_response

  elif action == "Retrieve Relevant Memory":
    memory = retrieve_relevant_memory(working_mem, episodic_mem, semantic_mem)
    new_prompt = "Related to what you said, I recall " + memory
    new_response = lang_model.generate_text(new_prompt)  
    working_mem.update([], [], [new_response])
    return new_response

  elif action == "Propose Solution":
    solution = propose_solution(working_mem)
    new_prompt = "I suggest " + solution + " as a possible solution. What do you think?"
    new_response = lang_model.generate_text(new_prompt)
    working_mem.update([], [], [new_response])
    return new_response
  
  else:
    return "I'm not sure what to do next."


def extract_goals_from_observation(obs):
    """Extract potential goals (topics) from an observation using noun phrase chunking."""
    
    blob = TextBlob(obs)
    goals = blob.noun_phrases
    
    return goals

def get_observation_and_goals():
    """Prompt the user for input and extract potential goals."""
    obs = input("Please provide an observation: ") 
    goals = extract_goals_from_observation(obs)
    return obs, goals

def agent_loop(lang_model, max_iterations=10):
  
    working_mem = WorkingMemory()
    episodic_mem = EpisodicMemory()
    semantic_mem = SemanticMemory()

    iteration_count = 0
    solutions = []  # List to store proposed solutions

    # First, get an observation from the user
    obs, goals = get_observation_and_goals()
    working_mem.update([obs], goals, [])

    while iteration_count < max_iterations:
        
        # If not the first iteration, use the agent's last response as the next observation
        if iteration_count > 0:
            if working_mem.actions:
                obs = working_mem.actions[-1]
            else:
                obs = "No recent actions."  # or any other default value you'd like to use

            goals = extract_goals_from_observation(obs)
            working_mem.update([obs], goals, [])

        retrieval(working_mem, episodic_mem, max_chunks=1)
        retrieval(working_mem, semantic_mem, max_chunks=1)

        lang_model.update_prefix(working_mem)
        reasoning(working_mem, lang_model)
        
        action = planning(working_mem, actions=[])

        response = execute_action(action, working_mem, episodic_mem, semantic_mem, lang_model)

        # Store the solution if the response is a proposed solution
        if action == "Propose Solution":
            solutions.append(response)

        learning(working_mem, episodic_mem)
        
        iteration_count += 1

    # Print all proposed solutions after finishing the loop
    print("\nAll Solutions Proposed by the Agent:")
    for idx, solution in enumerate(solutions, 1):
        print(f"{idx}. {solution}")


semantic_memory = SemanticMemory()
semantic_memory.load_from_txt("file.txt")
model_path = 'C://AI_MODELS//llama2_7b_chat_uncensored.ggmlv3.q4_0.bin'
lang_model = GPTModel(model_path)
# Run the agent loop for 10 iterations for demonstration purposes
agent_loop(lang_model, max_iterations=3)


'''
Cognition is a complex and multidimensional phenomenon that involves various mental processes such as perception, attention, memory, reasoning, problem-solving, and language.

If we use the WAIS as an example, we could represent cognition as a four-dimensional vector with the four index scores as its components. For instance, if a person has a Verbal Comprehension score of 110, a Perceptual Reasoning score of 95, a Working Memory score of 105, and a Processing Speed score of 90, their cognition vector would be (110, 95, 105, 90). To find the cosine of the angle between two cognition vectors, we would need to use the formula:

cosθ=∥u∥∥v∥u⋅v​

import numpy as np

def calculate_cosine_similarity(vector1, vector2):
    """Calculate cosine similarity between two vectors."""
    dot_product = np.dot(vector1, vector2)
    magnitude1 = np.linalg.norm(vector1)
    magnitude2 = np.linalg.norm(vector2)
    
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0  # Handle division by zero
    
    similarity = dot_product / (magnitude1 * magnitude2)
    return similarity

def analyze_similarity(similarity):
    """Analyze the cosine similarity value."""
    if similarity == 1:
        return "Perfect similarity. The vectors are identical."
    elif similarity >= 0.9:
        return "Very high similarity. The vectors are highly similar."
    elif similarity >= 0.7:
        return "High similarity. The vectors are somewhat similar."
    elif similarity >= 0.5:
        return "Moderate similarity. The vectors have some similarity."
    elif similarity >= 0.3:
        return "Low similarity. The vectors are dissimilar."
    elif similarity >= 0.1:
        return "Very low similarity. The vectors are highly dissimilar."
    else:
        return "Perfect dissimilarity. The vectors are orthogonal (completely dissimilar)."

# Input cognition vectors (replace with your values)
vector1 = np.array([110, 95, 105, 90])
vector2 = np.array([100, 100, 100, 100])

# Calculate cosine similarity
cosine_similarity = calculate_cosine_similarity(vector1, vector2)

# Analyze the similarity
analysis_result = analyze_similarity(cosine_similarity)

# Print the results
print(f"Cosine Similarity: {cosine_similarity:.2f}")
print(f"Analysis: {analysis_result}")

'''
