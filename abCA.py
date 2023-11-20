"""
Script ranks steps of the Abrameln Rites based on user input and distributes them over a grid for running CA over producing generative ritual instructions.
Riffing on ancient magical practice as computation, written frameworks for real life problem solving, or oral spells one can rationalise with etc.
"""
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import imageio.v2 as imageio
import os
import datetime
from gpt4all import GPT4All, Embed4All

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
def generate_embeddings(texts):
    embedder = Embed4All()
    embeddings = [embedder.embed(text) for text in texts]
    return embeddings

def compute_similarity_scores(input_embedding, description_embeddings):
    return [cosine_similarity([input_embedding], [desc_emb])[0][0] for desc_emb in description_embeddings]

def ca_step_2d(grid, rule):
    new_grid = np.empty_like(grid)
    grid_height, grid_width = grid.shape

    for row in range(grid_height):
        for col in range(grid_width):
            # Extract state and description from each neighboring cell
            state_above, _ = grid[(row - 1) % grid_height, col]
            state_left, _ = grid[row, (col - 1) % grid_width]
            state_center, description = grid[row, col] # Keep the description from the center cell
            state_right, _ = grid[row, (col + 1) % grid_width]
            state_below, _ = grid[(row + 1) % grid_height, col]

            # Calculating the pattern with wrapping for both rows and columns
            pattern = (state_above << 3) + (state_left << 2) + (state_center << 1) + state_right + state_below
            new_state = rule[pattern % len(rule)]

            # Update the new grid with the new state and the original description
            new_grid[row, col] = [new_state, description]

    return new_grid


# Define the Wolfram's Rule
def get_wolfram_rule(rule_number):
    return [int(x) for x in format(rule_number, '08b')]

def initialize_grid_with_descriptions(descriptions, similarity_scores, grid_size, rank_descriptions=True):
    # Rank descriptions based on similarity if required
    if rank_descriptions:
        ranked_descriptions = [desc for _, desc in sorted(zip(similarity_scores, descriptions), reverse=True)]
    else:
        ranked_descriptions = descriptions

    # Initialize the grid
    ca_grid = np.empty((grid_size, grid_size), dtype=object)

    # Populate the grid with descriptions
    for i in range(grid_size * grid_size):
        row, col = divmod(i, grid_size)
        # Use modulo to loop through the ranked_descriptions
        ca_grid[row, col] = [1, ranked_descriptions[i % len(ranked_descriptions)]] if i < len(ranked_descriptions) else [0, ranked_descriptions[i % len(ranked_descriptions)]]

    return ca_grid


def save_grid_state_as_image(grid, filename):
    # Extract the state (0 or 1) from each cell for visualization
    state_grid = np.array([[cell[0] for cell in row] for row in grid])
    plt.imshow(state_grid, cmap='binary')
    plt.axis('off')
    plt.savefig(filename)
    plt.close()

def run_and_save_ca_2d(input_text, descriptions, rule_number, grid_size, ca_steps):
    ca_rule = get_wolfram_rule(rule_number)
    ca_grid = initialize_grid_with_descriptions(descriptions, input_text, grid_size, rank_choice.lower() == 'yes')

    filenames = []
    all_ritual_steps = []

    # Record the rule number and input text at the start of the file
    all_ritual_steps.append(f"Input Text: '{input_text}'\n")
    all_ritual_steps.append(f"Rule Number: {rule_number}\n\n")

    for step in range(ca_steps):
        # Ensure that descriptions are converted to strings, and use a placeholder for None
        grid_state = "\n".join([" ".join([str(cell[1]) if cell[0] == 1 else '.' for cell in row]) for row in ca_grid])
        all_ritual_steps.append(f"Step {step + 1}:\n{grid_state}\n\n")

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


# Main execution
if __name__ == "__main__":
    user_input = input("Enter a sentence related to the Abramelin Ritual: ")
    rule_number = int(input("Enter a Wolfram CA rule number (0-255): "))
    grid_size = int(input("Enter the grid size: "))
    ca_steps = int(input("Enter the number of CA steps: "))
    rank_choice = input("Rank descriptions based on similarity? (yes/no): ")

    # Embeddings and similarity calculation (only once)
    all_texts = [user_input] + ritual_descriptions
    all_embeddings = generate_embeddings(all_texts)
    input_embedding = all_embeddings[0]
    description_embeddings = all_embeddings[1:]
    similarity_scores = compute_similarity_scores(input_embedding, description_embeddings)

    # Initialize grid with descriptions based on user choice
    rank_descriptions = rank_choice.lower() == 'yes'
    ca_grid = initialize_grid_with_descriptions(ritual_descriptions, similarity_scores, grid_size, rank_descriptions)

    # Run and save CA
    ca_rule = get_wolfram_rule(rule_number)
    run_and_save_ca_2d(user_input, ritual_descriptions, rule_number, grid_size, ca_steps)


