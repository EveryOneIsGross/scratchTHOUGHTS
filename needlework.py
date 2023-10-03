import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.colors as mcolors
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
            # Using modulo arithmetic to wrap around the edges of the grid and obtain neighboring cells' values
            left = grid[i, (j - 1) % grid_size]  # Represents the left neighboring cell
            right = grid[i, (j + 1) % grid_size]  # Represents the right neighboring cell
            top = grid[(i - 1) % grid_size, j]  # Represents the top neighboring cell
            bottom = grid[(i + 1) % grid_size, j]  # Represents the bottom neighboring cell
            top_left = grid[(i - 1) % grid_size, (j - 1) % grid_size]  # Represents the top-left neighboring cell
            top_right = grid[(i - 1) % grid_size, (j + 1) % grid_size]  # Represents the top-right neighboring cell
            bottom_left = grid[(i + 1) % grid_size, (j - 1) % grid_size]  # Represents the bottom-left neighboring cell
            bottom_right = grid[(i + 1) % grid_size, (j + 1) % grid_size]  # Represents the bottom-right neighboring cell
            
            # Apply rules to create different patterns based on the values of the neighboring cells.
            
            # Chain Stitch (C): Represents a loop or iteration in programming.
            if left == 'C' or right == 'C':
                new_grid[i, j] = 'X'  # Transforming to Cross Stitch (X)
                
            # Cross Stitch (X): Represents a decision point or condition in programming.
            elif top == 'X' or bottom == 'X':
                new_grid[i, j] = 'R'  # Transforming to Running Stitch (R)
                
            # Running Stitch (R): Represents a simple statement or instruction in programming.
            elif top_left == 'R' or bottom_right == 'R':
                new_grid[i, j] = 'C'  # Transforming to Chain Stitch (C)
                
            # Knot Stitch (K): Represents a variable or a data point in programming.
            elif top_right == 'K' or bottom_left == 'K':
                new_grid[i, j] = 'K'  # Maintaining as Knot Stitch (K)
                
            # Import Stitch (I): Represents an import statement in programming.
            elif left == 'I' or right == 'I':
                new_grid[i, j] = 'T'  # Transforming to Return Stitch (T)
                
            # Return Stitch (T): Represents a return statement in programming.
            elif top == 'T' or bottom == 'T':
                new_grid[i, j] = 'I'  # Transforming to Import Stitch (I)
                
            # Structure Stitch (S): Represents a class definition in programming.
            # It's symbolic of defining complex data types and encapsulating data and methods.
            #elif top_left == 'S' or bottom_right == 'S':
                #new_grid[i, j] = 'R'  # Transforming to Running Stitch (R)
                
    return new_grid  # Returning the grid after applying the rules.

def plot_3d(generations, base_file_name):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    grid_size = len(generations[0])
    x = np.arange(0, grid_size)
    y = np.arange(0, grid_size)
    X, Y = np.meshgrid(x, y)
    
    Z = np.full((grid_size, grid_size), -1)  # Set initial Z-values to -1
    
    for z, generation in enumerate(reversed(generations)):
        for i in range(grid_size):
            for j in range(grid_size):
                glyph = generation[i, j]
                if glyph != 'E' and (Z[i, j] == -1 or z > Z[i, j]):
                    Z[i, j] = z
    
    # Interpolate cells with Z-value of -1
    for i in range(grid_size):
        for j in range(grid_size):
            if Z[i, j] == -1:
                neighbors = []
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < grid_size and 0 <= nj < grid_size and Z[ni, nj] != -1:
                            neighbors.append(Z[ni, nj])
                Z[i, j] = np.mean(neighbors) if neighbors else 0

    # Plot the surface with a colormap based on Z values
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
    fig.colorbar(surf)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Generation')
    ax.view_init(elev=30, azim=-60)
    plt.savefig(f"{base_file_name}_3d_surface_plot.png")
    plt.show()

    plt.close(fig)








def visualize_grid_with_color(grid, file_name):
    fig, ax = plt.subplots(figsize=(6, 6))  # Ensure that the figure size is consistent for all images
    grid_size = len(grid)
    ax.set_xlim(0, grid_size)
    ax.set_ylim(0, grid_size)
    ax.axis('off')
    
    # Ensure that the figure size remains consistent, which is important for creating GIFs
    ax.set_aspect('equal', adjustable='box')
    
    glyph_colors = {
        'C': '#FFB6C1',  # Light Pink
        'X': '#ADD8E6',  # Light Blue
        'R': '#98FB98',  # Pale Green
        'K': '#FFFACD',  # Lemon Chiffon
        'I': '#E6E6FA',  # Lavender
        'T': '#FFDAB9',  # Peach Puff
        'E': '#F0F8FF'   # Alice Blue
    }
    for i in range(grid_size):
        for j in range(grid_size):
            glyph = grid[i, j]
            color = glyph_colors.get(glyph, 'white')
            rect = patches.Rectangle((j, grid_size - i - 1), 1, 1, linewidth=1, edgecolor='none', facecolor=color)
            ax.add_patch(rect)
            if glyph != 'E':
                ax.text(j + 0.5, grid_size - i - 0.5, glyph, color='white', ha='center', va='center', fontsize=12, family='monospace')
    plt.savefig(file_name, bbox_inches='tight')
    plt.close(fig)  # Close the figure to release the memory

def visualize_tapestry_with_connections(generations, file_name):
    fig, ax = plt.subplots(figsize=(10, 10))
    
    ax.axis('off')  # Disable the axis
    
    num_generations = len(generations)
    grid_size = len(generations[0])
    
    glyph_colors = {
        'C': '#FFB6C1',  # Light Pink
        'X': '#ADD8E6',  # Light Blue
        'R': '#98FB98',  # Pale Green
        'K': '#FFFACD',  # Lemon Chiffon
        'I': '#E6E6FA',  # Lavender
        'T': '#FFDAB9',  # Peach Puff
        'E': '#F0F8FF'   # Alice Blue
    }
    
    total_width = grid_size * num_generations
    ax.set_xlim(0, total_width)
    ax.set_ylim(0, grid_size)
    
    for gen_num, generation in enumerate(generations):
        start_x = grid_size * gen_num  # starting x-coordinate for each generation
        for i in range(grid_size):
            for j in range(grid_size):
                glyph = generation[i, j]
                color = glyph_colors.get(glyph, 'white')
                rect = patches.Rectangle((start_x + j, i), 1, 1, linewidth=1, edgecolor='none', facecolor=color)
                ax.add_patch(rect)
                # Do not draw the letters, so the following line is commented out.
                # if glyph != 'E':
                #     ax.text(start_x + j + 0.5, i + 0.5, glyph, color='black', ha='center', va='center', fontsize=12, family='monospace')
        
        # Drawing connections between generations
        if gen_num < num_generations - 1:
            next_generation = generations[gen_num + 1]
            # Define a color map to get a range of colors for the connections
            cmap = plt.get_cmap('plasma')
            for i in range(grid_size):
                for j in range(grid_size):
                    if generation[i, j] == 'I':
                        for x in range(grid_size):
                            for y in range(grid_size):
                                if next_generation[x, y] == 'T':
                                    # Define a normalized scalar to get a color from the color map
                                    #norm = mcolors.Normalize(vmin=0, vmax=grid_size)
                                    #connection_color = cmap(norm(x))
                                    connection_color = 'black'
                                    ax.plot([start_x + j + 0.5, start_x + grid_size + y + 0.5], [i + 0.5, x + 0.5], color=connection_color, linewidth=0.2)
    
    plt.gca().set_aspect('equal', adjustable='box')
    plt.savefig(file_name, bbox_inches='tight', dpi=300)  # Save with high dpi and minimal padding
    plt.close(fig)  # Close the figure to release the memory
    
    # Rotate the saved image
    img = Image.open(file_name)
    rotated_img = img.rotate(90, expand=True)  # Rotate 90 degrees and expand the canvas if needed
    rotated_img.save(file_name)  # Overwrite the original file with the rotated image


def generate_explanations(generations):
    explanation_mapping = {
        'C': 'A loop or iteration is initiated.', 
        'X': 'A decision point or condition is checked.',
        'R': 'A simple statement or instruction is executed.', 
        'K': 'A variable or a data point is encountered.',
        'I': 'A module or library is imported.', 
        'T': 'A value is returned.', 
        'E': 'An empty space, no operation is performed here.'
    }
    
    all_explanations = []
    
    for gen_num, generation in enumerate(generations):
        explanations = []
        grid_size = len(generation)
        
        for i in range(grid_size):
            row_explanations = []
            for j in range(grid_size):
                glyph = generation[i, j]
                explanation = explanation_mapping.get(glyph, 'Unknown operation.')
                row_explanations.append(explanation)
            explanations.append(' '.join(row_explanations))
        
        # If not the first generation, explain connections between 'I' in this generation to 'T' in the previous generation
        if gen_num > 0:
            prev_generation = generations[gen_num - 1]
            for i in range(grid_size):
                for j in range(grid_size):
                    if generation[i, j] == 'I':
                        for x in range(grid_size):
                            for y in range(grid_size):
                                if prev_generation[x, y] == 'T':
                                    connection_explanation = f"A thread is connected from Return Stitch at position ({x + 1}, {y + 1}) in Generation {gen_num} to Import Stitch at position ({i + 1}, {j + 1}) in Generation {gen_num + 1}."
                                    explanations.append(connection_explanation)
        
        all_explanations.append(explanations)
    
    return all_explanations



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
                file.write(' '.join(row) + '\n')  # Joining the characters to form a single line
            file.write('\n')
            
            # Writing the translation labeled per generation
            file.write("Translation:\n")
            for line_num, line_explanation in enumerate(explanation):
                file.write(f"Line {line_num + 1}: {line_explanation}\n")
            file.write("\n" + "="*50 + "\n")  # Separator between generations



def generate_needlework_instructions(generations):
    needlework_mapping = {
        'C': 'Perform a Chain Stitch at',
        'X': 'Perform a Cross Stitch at',
        'R': 'Perform a Running Stitch at',
        'K': 'Perform a Knot Stitch at',
        'I': 'Perform an Import Stitch at',
        'T': 'Perform a Return Stitch at',
        'E': 'Leave an Empty Space at'
    }
    
    instructions = []
    connection_instructions = []
    
    for gen_num, generation in enumerate(generations):
        if len(generation.shape) != 2:  # Check if the generation is two-dimensional
            raise ValueError(f"Generation {gen_num} is not a 2D array")
        
        grid_size = len(generation)
        input_positions_current = []
        return_positions_next = []
        
        if gen_num < len(generations) - 1:  # Check if there is a next generation
            next_generation = generations[gen_num + 1]
            if len(next_generation.shape) != 2:  # Check if the next generation is two-dimensional
                raise ValueError(f"Next generation {gen_num + 1} is not a 2D array")
            for i in range(grid_size):
                for j in range(grid_size):
                    if next_generation[i, j] == 'T':
                        return_positions_next.append((i, j))
        
        for i in range(grid_size):
            for j in range(grid_size):
                glyph = generation[i, j]
                instruction = needlework_mapping.get(glyph, 'Unknown operation.')
                if glyph != 'E':
                    instructions.append(f"{instruction} position ({i + 1}, {j + 1}) in generation {gen_num + 1}.")
                
                if glyph == 'I':
                    input_positions_current.append((i, j))
        
        # Generate instructions to tie threads between 'I' in the current generation and 'T' in the next generation
        for i_pos in input_positions_current:
            for t_pos in return_positions_next:
                connection_instructions.append(f"Connect a thread from Import Stitch at position {i_pos[0] + 1, i_pos[1] + 1} in generation {gen_num + 1} to Return Stitch at position {t_pos[0] + 1, t_pos[1] + 1} in generation {gen_num + 2}.")
    
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
        # Call the new visualization function to create tapestry with connections
    
    tapestry_file_name = f"{base_file_name}_tapestry.png"
    visualize_tapestry_with_connections(generations, tapestry_file_name)
       
    plot_3d(generations, base_file_name)  # Create a 3D plot after all generations have been created
    gif_file_name = f"{base_file_name}_animated.gif"
    imageio.mimsave(gif_file_name, [imageio.imread(image) for image in images], duration=1)  # Create GIF after all generations have been created
    
    needlework_instructions = generate_needlework_instructions(generations)  # Corrected line
    needlework_file_name = f"{base_file_name}_needlework_instructions.txt"
    save_needlework_instructions(needlework_instructions, needlework_file_name)


    txt_file_name = f"{base_file_name}_pattern.txt"
    save_to_file(grid_size, initial_state, generations, generate_explanations(generations), txt_file_name)  # Save the text representation and explanations of each generation to a .txt file

if __name__ == "__main__":
    main()
