import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

def print_intro():
    print("Welcome to the Needlework Pattern Creator!")
    print("Create beautiful needlework patterns based on user-defined initial states and rules.\n")
    print("Glossary of Stitches:")
    print("C: Chain Stitch - Represents a loop or iteration in programming.")
    print("X: Cross Stitch - Represents a decision point or condition in programming.")
    print("R: Running Stitch - Represents a simple statement or instruction in programming.")
    print("K: Knot Stitch - Represents a variable or a data point in programming.")
    print("I: Import Stitch - Represents an import statement in programming.")
    print("T: Return Stitch - Represents a return statement in programming.")
    print("S: Structure Stitch - Represents a class definition in programming.")
    print("E: Empty Space - Represents a space with no stitch.")
    print("\nEnter the initial state as a string of stitches and observe how it evolves to create intricate needlework patterns.\n")

    

def initialize_grid(grid_size, initial_state):
    grid = np.full((grid_size, grid_size), 'E', dtype='<U1')
    grid[0, :len(initial_state)] = list(initial_state)
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
                new_grid[i, j] = 'C'
            elif top == 'T' or bottom == 'T':
                new_grid[i, j] = 'X'
            elif top_left == 'S' or bottom_right == 'S':
                new_grid[i, j] = 'R'
    return new_grid


def visualize_grid_with_color(grid):
    fig, ax = plt.subplots(figsize=(6, 6))
    grid_size = len(grid)
    ax.set_xlim(0, grid_size)
    ax.set_ylim(0, grid_size)
    ax.axis('off')
    glyph_colors = {'C': 'blue', 'X': 'red', 'R': 'green', 'K': 'black', 'I': 'purple', 'T': 'orange', 'S': 'brown', 'E': 'white'}
    for i in range(grid_size):
        for j in range(grid_size):
            glyph = grid[i, j]
            color = glyph_colors.get(glyph, 'white')
            rect = patches.Rectangle((j, grid_size - i - 1), 1, 1, linewidth=1, edgecolor='none', facecolor=color)
            ax.add_patch(rect)
            if glyph != 'E':
                ax.text(j + 0.5, grid_size - i - 0.5, glyph, color='black', ha='center', va='center', fontsize=12, family='monospace')
    plt.show()

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
    fig, ax = plt.subplots(figsize=(6, 6))
    grid_size = len(grid)
    ax.set_xlim(0, grid_size)
    ax.set_ylim(0, grid_size)
    ax.axis('off')
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
    plt.close(fig)  # Close the figure

# Modify the main loop to call the function with the appropriate file name
def main():
    print_intro()
    grid_size = int(input("Enter the grid size (n): "))
    initial_state = input(f"Enter the initial state as a string of {grid_size} stitches (e.g. 'CXRIKTS'): ")
    grid = initialize_grid(grid_size, initial_state)
    
    generations = [grid.copy()]  # List to store each generation
    explanations_list = [generate_explanations(grid)]  # List to store the explanations corresponding to each generation
    
    gen_num = 0
    while True:
        img_file_name = f"needlework_pattern_gen_{gen_num}.png"
        visualize_grid_with_color(grid, img_file_name)  # Save the visual representation of the grid as a .png file
        
        print_explanations(grid)
        
        continue_generation = input("Would you like to continue to the next generation? (y/n): ").lower()
        if continue_generation != 'y':
            break
        
        grid = apply_rules(grid)  # Apply rules to get the next generation
        generations.append(grid.copy())  # Store the new generation
        explanations_list.append(generate_explanations(grid))  # Store the explanations of the new generation
        
        gen_num += 1
    
    txt_file_name = "needlework_pattern.txt"
    save_to_file(grid_size, initial_state, generations, explanations_list, txt_file_name)  # Save the text representation and explanations of each generation to a .txt file

if __name__ == "__main__":
    main()
