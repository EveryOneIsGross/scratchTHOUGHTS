'''Carefully read the input string character-by-character, referring to the provided glossary to understand what each symbol represents in terms of programming constructs.

Mentally parse the input string into a coherent sequence of programming logic based on the glossary translation.

Visually map out on paper how that sequence would expand by applying the defined rules. For example:

A loop symbol means repeat the contained sequence
A condition symbol means there will be two branching paths
Variables and returns mean certain symbols will propagate
Etc.
Manually draw out the grid showing how the pattern expands by applying the rules to each construct.

For each row, iterate through the previous row applying rules based on the symbol:

Loop symbols cause their contents to repeat
Conditionals branch into two paths
Returns lead to stitches propagating backwards
Variables copy stitches diagonally
Mentally keep track of scope, nesting, and scale of the patterns

Fill in the grid for as many generations as desired by applying rules

Transcribe the final grid back into a string encoding the pattern

This manual process would require meticulous care, attention to detail, and methodical application of the rules. But a human could plausibly replicate the program's output given time and effort. '''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from mpl_toolkits.mplot3d import Axes3D
import os
import time
import uuid
import imageio
from PIL import Image

def resize_images(images, width, height):
    resized_images = []
    for image_path in images:
        img = Image.open(image_path)
        img_resized = img.resize((width, height))
        resized_images.append(img_resized)
    return resized_images


def print_intro():
    print("Welcome to the Needlework Pattern Creator!")
    print("Create beautiful needlework patterns based on user-defined initial states and rules.\n")
    print("Glossary of Stitches:")
    print("∞: Chain Stitch (C) - Represents a loop or iteration in programming.")
    print("×: Cross Stitch (X) - Represents a decision point or condition in programming.")
    print("–: Running Stitch (R) - Represents a simple statement or instruction in programming.")
    print("•: Knot Stitch (K) - Represents a variable or a data point in programming.")
    print("↑: Import Stitch (I) - Represents an import statement in programming.")
    print("↓: Return Stitch (T) - Represents a return statement in programming.")
    print("§: Structure Stitch (S) - Represents a class definition in programming.")
    print(".: Empty Space (E) - Represents a space with no stitch.")
    print("\nEnter the initial state as a string of stitches and observe how it evolves to create intricate needlework patterns.\n")


    


def initialize_grid(grid_size, initial_state):
    grid = np.full((grid_size, grid_size), 'E', dtype='<U1')
    effective_state = (initial_state[:grid_size] + 'E' * grid_size)[:grid_size]
    grid[0, :len(effective_state)] = list(effective_state)
    return grid

def apply_rules(grid):
    new_grid = grid.copy()
    grid_size = len(grid)
    for i in range(grid_size):
        for j in range(grid_size):
            # Get the values of the neighboring cells
            # Use modulo arithmetic to wrap around the edges of the grid
            left = grid[i, (j - 1) % grid_size]
            right = grid[i, (j + 1) % grid_size]
            top = grid[(i - 1) % grid_size, j]
            bottom = grid[(i + 1) % grid_size, j]
            top_left = grid[(i - 1) % grid_size, (j - 1) % grid_size]
            top_right = grid[(i - 1) % grid_size, (j + 1) % grid_size]
            bottom_left = grid[(i + 1) % grid_size, (j - 1) % grid_size]
            bottom_right = grid[(i + 1) % grid_size, (j + 1) % grid_size]

            # Apply some rules based on the values of the neighboring cells
            # You can modify these rules as you like to create different patterns
            if left == 'C' or right == 'C':
                new_grid[i, j] = 'X'
            elif top == 'X' or bottom == 'X':
                new_grid[i, j] = 'R'
            elif top_left == 'R' or bottom_right == 'R':
                new_grid[i, j] = 'C'
            elif top_right == 'K' or bottom_left == 'K':
                new_grid[i, j] = 'K'
            elif left == 'I' or right == 'I':
                new_grid[i, j] = 'T'
            elif top == 'T' or bottom == 'T':
                new_grid[i, j] = 'I'
            elif top_left == 'S' or bottom_right == 'S':
                new_grid[i, j] = 'R'
    return new_grid


def visualize_grid_with_color(grid, file_name):
    fig, ax = plt.subplots(figsize=(6, 6))  # Ensure that the figure size is consistent for all images
    grid_size = len(grid)
    ax.set_xlim(0, grid_size)
    ax.set_ylim(0, grid_size)
    ax.axis('off')
    
    # Ensure that the figure size remains consistent, which is important for creating GIFs
    ax.set_aspect('equal', adjustable='box')
    
    glyph_colors = {'C': 'blue', 'X': 'red', 'R': 'green', 'K': 'black', 'I': 'purple', 'T': 'orange', 'S': 'brown', 'E': 'white'}
    for i in range(grid_size):
        for j in range(grid_size):
            glyph = grid[i, j]
            color = glyph_colors.get(glyph, 'white')
            rect = patches.Rectangle((j, grid_size - i - 1), 1, 1, linewidth=1, edgecolor='none', facecolor=color)
            ax.add_patch(rect)
            if glyph != 'E':
                ax.text(j + 0.5, grid_size - i - 0.5, glyph, color='black', ha='center', va='center', fontsize=12, family='monospace')
    plt.savefig(file_name, bbox_inches='tight')
    plt.close(fig)  # Close the figure to release the memory

def generate_explanations(grid):
    explanation_mapping = {'C': 'A loop or iteration is initiated.', 'X': 'A decision point or condition is checked.',
                           'R': 'A simple statement or instruction is executed.', 'K': 'A variable or a data point is encountered.',
                           'I': 'A module or library is imported.', 'T': 'A value is returned.', 'S': 'A class definition is structured.', 'E': 'An empty space, no operation is performed here.'}
    explanations = []
    grid_size = len(grid)
    for i in range(grid_size):
        row_explanations = []
        for j in range(grid_size):
            glyph = grid[i, j]
            explanation = explanation_mapping.get(glyph, 'Unknown operation.')
            row_explanations.append(explanation)
        explanations.append(' '.join(row_explanations))
    return explanations

def print_explanations(grid):
    explanations = generate_explanations(grid)
    for i, explanation in enumerate(explanations):
        print(f"Line {i + 1}: {explanation}")


def save_to_file(grid_size, initial_state, generations, explanations_list, file_name):
    with open(file_name, 'w') as file:
        file.write(f"Grid Size: {grid_size}\n")
        file.write(f"Initial State: {initial_state}\n\n")
        
        for gen_num, (generation, explanation) in enumerate(zip(generations, explanations_list)):
            file.write(f"Generation {gen_num}:\n")
            
            # Writing each generation as a continuous grid
            for row in generation:
                file.write(' '.join(row) + '\n')
            file.write('\n')
            
            # Writing the translation labeled per generation
            file.write("Translation:\n")
            for line_num, line_explanation in enumerate(explanation):
                file.write(f"Line {line_num + 1}: {line_explanation}\n")
            file.write("\n" + "="*50 + "\n")  # Separator between generations


def visualize_grid_with_color(grid, file_name):
    fig, ax = plt.subplots(figsize=(6, 6))  # Consistent figure size
    grid_size = len(grid)
    
    # Set consistent plot limits
    ax.set_xlim(0, grid_size)
    ax.set_ylim(0, grid_size)
    
    ax.set_aspect('equal', 'box')  # Equal aspect ratio
    ax.axis('off')  # No axes for a clean look
    
    glyph_colors = {'C': 'blue', 'X': 'red', 'R': 'green', 'K': 'black', 'I': 'purple', 'T': 'orange', 'S': 'brown', 'E': 'white'}
    for i in range(grid_size):
        for j in range(grid_size):
            glyph = grid[i, j]
            color = glyph_colors.get(glyph, 'white')
            rect = patches.Rectangle((j, grid_size - i - 1), 1, 1, linewidth=1, edgecolor='none', facecolor=color)
            ax.add_patch(rect)
            if glyph != 'E':
                ax.text(j + 0.5, grid_size - i - 0.5, glyph, color='black', ha='center', va='center', fontsize=12, family='monospace')
    
    plt.tight_layout()  # Remove excess whitespace
    plt.savefig(file_name)  # Save with minimal padding
    plt.close(fig)  # Close the figure to release the memory


def plot_3d(generations, base_file_name):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    glyph_colors = {'C': 'blue', 'X': 'red', 'R': 'green', 'K': 'black', 'I': 'purple', 'T': 'orange', 'S': 'brown', 'E': 'white'}
    grid_size = len(generations[0])
    
    for z, generation in enumerate(generations):
        for x in range(grid_size):
            for y in range(grid_size):
                glyph = generation[x, y]
                color = glyph_colors.get(glyph, 'white')
                if glyph != 'E':  # Skip plotting empty spaces
                    ax.scatter(y, grid_size - x - 1, z, c=color, s=50)  # s denotes the size of the point in the scatter plot
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Generation')
    
    plt.savefig(f"{base_file_name}_3d_plot.png")
    plt.close(fig)

def generate_needlework_instructions(grid):
    needlework_mapping = {
        'C': 'Perform a Chain Stitch at',
        'X': 'Perform a Cross Stitch at',
        'R': 'Perform a Running Stitch at',
        'K': 'Perform a Knot Stitch at',
        'I': 'Perform an Import Stitch at',
        'T': 'Perform a Return Stitch at',
        'S': 'Perform a Structure Stitch at',
        'E': 'Leave an Empty Space at'
    }
    
    instructions = []
    grid_size = len(grid)
    input_positions = []
    return_positions = []
    
    for i in range(grid_size):
        for j in range(grid_size):
            glyph = grid[i, j]
            instruction = needlework_mapping.get(glyph, 'Unknown operation.')
            if glyph != 'E':  # Skip instructions for Empty Space
                instructions.append(f"{instruction} position ({i + 1}, {j + 1}).")
            
            if glyph == 'I':
                input_positions.append((i, j))
            elif glyph == 'T':
                return_positions.append((i, j))
    
    # Generate instructions to tie threads between 'I' and 'T'
    connection_instructions = []
    for i_pos in input_positions:
        for t_pos in return_positions:
            connection_instructions.append(f"Connect a thread from position {i_pos[0] + 1, i_pos[1] + 1} to position {t_pos[0] + 1, t_pos[1] + 1}.")
    
    # Append connection instructions last
    instructions.extend(connection_instructions)
    
    return instructions


def save_needlework_instructions(instructions, file_name):
    with open(file_name, 'w') as file:
        file.write("\n".join(instructions))


def main():
    print_intro()
    grid_size = int(input("Enter the grid size (n): "))
    initial_state = input(f"Enter the initial state as a string of stitches (e.g. 'CXRIKTS'): ")
    num_generations = int(input("Enter the number of generations you want to generate: "))
    
    unique_id = str(uuid.uuid4())
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    base_file_name = f"{initial_state}_{timestamp}_{unique_id}"
    
    grid = initialize_grid(grid_size, initial_state)
    
    generations = [grid.copy()]  # List to store each generation
    images = []  # List to store the paths of the image files
    
    for gen_num in range(num_generations):
        img_file_name = f"{base_file_name}_gen_{gen_num}.png"
        visualize_grid_with_color(grid, img_file_name)  # Save the visual representation of the grid as a .png file
        images.append(img_file_name)  # Append the image file path to the list
        
        if gen_num < num_generations - 1:  # Skip applying rules for the last generation
            grid = apply_rules(grid)  # Apply rules to get the next generation
            generations.append(grid.copy())  # Store the new generation
        
    plot_3d(generations, base_file_name)  # Create a 3D plot after all generations have been created
    gif_file_name = f"{base_file_name}_animated.gif"
    imageio.mimsave(gif_file_name, [imageio.imread(image) for image in images], duration=1)  # Create GIF after all generations have been created
    needlework_instructions = generate_needlework_instructions(grid)
    needlework_file_name = f"{base_file_name}_needlework_instructions.txt"
    save_needlework_instructions(needlework_instructions, needlework_file_name)


    txt_file_name = f"{base_file_name}_pattern.txt"
    save_to_file(grid_size, initial_state, generations, [generate_explanations(grid) for grid in generations], txt_file_name)  # Save the text representation and explanations of each generation to a .txt file

if __name__ == "__main__":
    main()
