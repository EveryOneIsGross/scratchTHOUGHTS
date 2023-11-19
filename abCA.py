"""
Script ranks steps of the Abrameln Rites based on user input and distributes them over a grid for running CA over producing generative ritual instructions.
Riffing on ancient magical practice as computation, written frameworks for real life problem solving, or oral spells one can rationalise with etc.
"""

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import imageio
import os
import datetime

similarity_threshold = 0.5

# Abramelin Ritual descriptions
ritual_descriptions = [
    "Create a sacred space.",
    "Perform daily prayers and meditations for spiritual purification.",
    "Maintain strict dietary restrictions.",
    "Construct a magic circle.",
    "Prepare consecrated tools such as a wand and robe.",
    "Obtain a holy oil for anointing.",
    "Invoke guardian angels for protection.",
    "Begin daily invocations to contact the Holy Guardian Angel (HGA).",
    "Record dreams and visions in a diary.",
    "Seek guidance and wisdom from the HGA.",
    "Perform daily rituals to establish a strong connection.",
    "Meditate on the symbolism of the magic squares (representing CA rules).",
    "The ritual may last for several months.",
    "Continue daily practices with dedication and discipline.",
    "When guidance is received or the goal is achieved, thank the HGA.",
    "Gradually close the magical circle.",
    "Reflect on the experience and integrate insights into daily life."
]

# Function to map descriptions to a vector
def map_descriptions_to_vector(descriptions, input_text):
    vectors = []
    for description in descriptions:
        vector = np.zeros(len(descriptions), dtype=float)
        for word in description.split():
            if word in input_text.split():
                vector[descriptions.index(description)] += 1
        vectors.append(vector)
    return vectors

# Function to initialize the grid with each cell representing a different description
def initialize_grid(descriptions, input_text, grid_width, grid_height):
    input_vector = map_descriptions_to_vector(descriptions, input_text)
    similarity_scores = [cosine_similarity([input_vector[0]], [map_descriptions_to_vector(descriptions, desc)[0]])[0][0] for desc in descriptions]

    ca_grid = np.zeros((grid_height, grid_width), dtype=int)
    for row in range(grid_height):
        for col in range(grid_width):
            desc_index = (row * grid_width + col) % len(descriptions)
            # Activate cell if corresponding description has high similarity
            ca_grid[row, col] = 1 if similarity_scores[desc_index] > similarity_threshold else 0

    return ca_grid

def ca_step_2d(grid, rule):
    new_grid = np.zeros_like(grid)
    grid_height, grid_width = grid.shape

    for row in range(grid_height - 1):  # Evolve from top to bottom
        for col in range(grid_width):
            # Using modulo for wrapping around the grid
            left = grid[row, (col - 1) % grid_width]
            center = grid[row, col]
            right = grid[row, (col + 1) % grid_width]

            # Calculating the pattern with wrapping
            pattern = 4 * left + 2 * center + right
            new_grid[row + 1, col] = rule[7 - pattern]

    return new_grid


# Define the Wolfram's Rule
def get_wolfram_rule(rule_number):
    return [int(x) for x in format(rule_number, '08b')]

# Function to initialize the grid with each cell representing a different description
def initialize_grid_with_descriptions(descriptions, input_text, grid_size):
    input_vector = map_descriptions_to_vector(descriptions, input_text)
    similarity_scores = [cosine_similarity([input_vector[0]], [map_descriptions_to_vector(descriptions, desc)[0]])[0][0] for desc in descriptions]

    ca_grid = np.zeros((grid_size, grid_size), dtype=int)

    # Initialize the grid with descriptions based on similarity
    for row in range(grid_size):
        for col in range(grid_size):
            desc_index = (row * grid_size + col) % len(descriptions)
            ca_grid[row, col] = 1 if similarity_scores[desc_index] > similarity_threshold else 0

    # Introduce an initial active cell in the middle of the first row
    ca_grid[0, grid_size // 2] = 1

    return ca_grid

# Save grid state as an image
def save_grid_state_as_image(grid, filename):
    plt.imshow(grid, cmap='binary')
    plt.axis('off')
    plt.savefig(filename)
    plt.close()

# Run and save the CA evolution
def run_and_save_ca_2d(input_text, descriptions, rule_number, grid_size, ca_steps):
    ca_rule = get_wolfram_rule(rule_number)
    ca_grid = initialize_grid_with_descriptions(descriptions, input_text, grid_size)

    filenames = []
    all_ritual_steps = []

    # Record the rule number and input text at the start of the file
    all_ritual_steps.append(f"Input Text: '{input_text}'\n")
    all_ritual_steps.append(f"Rule Number: {rule_number}\n\n")

    for step in range(ca_steps):
        # Record active descriptions
        active_sentences = [descriptions[(row * grid_size + col) % len(descriptions)] for row in range(grid_size) for col in range(grid_size) if ca_grid[row, col] == 1]
        all_ritual_steps.append(f"Step {step + 1}: " + ", ".join(active_sentences) + "\n")

        filename = f"ca_step_{step}.png"
        save_grid_state_as_image(ca_grid, filename)
        filenames.append(filename)

        ca_grid = ca_step_2d(ca_grid, ca_rule)

    # Save steps to text file and create GIF
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    txt_filename = f"ritual_evolution_{timestamp}.txt"
    gif_filename = f"ca_evolution_{timestamp}.gif"
    with open(txt_filename, "w") as file:
        file.writelines(all_ritual_steps)
    with imageio.get_writer(gif_filename, mode='I') as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)
            os.remove(filename)

    print(f"CA evolution saved to '{gif_filename}'")
    print(f"Ritual evolution saved to '{txt_filename}'")

if __name__ == "__main__":
    user_input = input("Enter a sentence related to the Abramelin Ritual: ")
    rule_number = int(input("Enter a Wolfram CA rule number (0-255): "))
    grid_size = int(input("Enter the grid size: "))
    ca_steps = int(input("Enter the number of CA steps: "))
    run_and_save_ca_2d(user_input, ritual_descriptions, rule_number, grid_size, ca_steps)

