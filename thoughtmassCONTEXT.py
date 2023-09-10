'''
Text Semantics Analysis Tool
This tool performs semantic analysis on input text to model the contours of meaningfulness using concepts from an exploratory ontology of thought.
It segments the text into chunks, then quantifies and visualizes metrics including:

Thought Mass - Semantic density calculated using TF-IDF vectors
Local Entropy - Variability of thought mass representing homogenization
Gradients - Changes in thought mass indicating meaningful edges
Similarity - Contextual continuity measured by cosine distance of adjacent chunks
These metrics allow interactively exploring the dynamics of context, novelty, noise reduction, and information contours within the textual ideascape. Users can tune analysis parameters like chunk size, smoothing thresholds, etc.

Advanced features include 3D visualization, Markov boundary detection, and normalized scaling. The tool is intended as a practical demonstration of mapping mindspace.
'''

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
from matplotlib import gridspec
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler


def read_file(file_path):
    """Reads the contents of a given file."""
    with open(file_path, 'r') as file:
        return file.read()

def segment_text(text, n=20):
    """Segments the text into chunks of n words each."""
    # Remove non-alphabetic characters
    text = ' '.join(word for word in text.split() if word.isalpha())
    words = text.split()
    return [' '.join(words[i:i+n]) for i in range(0, len(words), n)]


def compute_thought_mass_tfidf(unit, units):
    """Compute thought-mass using TF-IDF values."""
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(units)
    tfidf_values = tfidf_matrix[units.index(unit)].toarray()[0]
    return sum(tfidf_values)

def compute_local_entropy(unit, units):
    """Compute the local entropy for a given segment based on its thought-mass."""
    thought_mass = compute_thought_mass_tfidf(unit, units)
    total_mass = sum(compute_thought_mass_tfidf(unit, units) for unit in units)
    probability = thought_mass / total_mass
    return -probability * np.log(probability)

def compute_gradient_of_thought_mass(units):
    """Compute the gradient of thought-mass for each segment."""
    thought_masses = [compute_thought_mass_tfidf(unit, units) for unit in units]
    return np.gradient(thought_masses)

def compute_markov_blanket(unit, units):
    """Compute the Markov blanket for a given segment."""
    # Active states: beginning and ending words of the segment
    active_states = set([unit.split()[0], unit.split()[-1]])
    
    # Sensory states: words in the segment with the highest TF-IDF values
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(units)
    feature_names = vectorizer.get_feature_names_out()
    print (feature_names)
    tfidf_values = tfidf_matrix[units.index(unit)].toarray()[0]
    top_indices = np.argsort(tfidf_values)[-2:]  # Take top 2 for demonstration
    sensory_states = set([feature_names[i] for i in top_indices])
    
    # Markov blanket: union of active and sensory states
    return active_states.union(sensory_states)

def identify_edges(units, threshold=1): 
    """Identify edges in the text using the Markov blanket with an adjustable threshold."""
    markov_blankets = [compute_markov_blanket(unit, units) for unit in units]
    edges = []
    for i, mb in enumerate(markov_blankets):
        # If the difference in the Markov blanket compared to adjacent segments exceeds the threshold, it's an edge
        prev_mb = markov_blankets[i-1] if i-1 >= 0 else set()
        next_mb = markov_blankets[i+1] if i+1 < len(markov_blankets) else set()
        
        is_edge = len(mb.difference(prev_mb)) > threshold or len(mb.difference(next_mb)) > threshold
        edges.append(is_edge)

    return edges







def sigmoid(x):
    """A simple sigmoid function."""
    return 1 / (1 + np.exp(-x))

def suppression_function(entropy, threshold=0.8): # higher threshold = less suppression
    """Suppression function based on entropy using a sigmoid function."""
    suppression_value = sigmoid(10 * (entropy - threshold)) 

    return "SUPPRESSED" if suppression_value < 0.5 else None

def similarity_suppression_function(similarity, threshold=0.8): # higher threshold = more suppression
    """Suppression function based on cosine similarity."""
    return "SUPPRESSED" if similarity > threshold else None

def combined_suppression_function(unit, index, units, entropy_threshold, similarity_threshold):
    """Refined combination of entropy-based and similarity-based suppression."""
    entropy = compute_local_entropy(unit, units)
    suppress_entropy = sigmoid(10 * (entropy - entropy_threshold))  # Adjusted the multiplier to 10 for a smoother curve
    
    # Get similarity with previous and next segment
    if index > 0:
        sim_prev = compute_adjacent_cosine_similarity(units[index], units[index - 1])
    else:
        sim_prev = 0
    
    if index < len(units) - 1:
        sim_next = compute_adjacent_cosine_similarity(units[index], units[index + 1])
    else:
        sim_next = 0
    
    average_similarity = (sim_prev + sim_next) / 2.0  # Use average similarity
    suppress_similarity = average_similarity > similarity_threshold
    
    return "SUPPRESSED" if suppress_entropy < 0.5 or suppress_similarity else None  # Using OR logic



def display_processed_text(suppressed_states, units, edges):
    print("\nProcessed Text:\n")
    for i, (is_suppressed, segment, edge) in enumerate(zip(suppressed_states, units, edges)):
        suppression_status = "[SUPPRESSED] " if is_suppressed else ""
        edge_status = " [EDGE]" if edge else ""
        
        print(f"Segment {i+1}: {suppression_status}{segment}{edge_status}\n")




def process_text(text, n=20, entropy_threshold=0.1, gradient_threshold=0.5, similarity_threshold=0.9):
    units = segment_text(text, n)
    original_units = units.copy()

    thought_masses = [compute_thought_mass_tfidf(unit, units) for unit in units]
    local_entropies = [compute_local_entropy(unit, units) for unit in units]
    similarities = compute_adjacent_cosine_similarity(units)

    suppressed_states = [False] * len(units)  # Initialize with all segments as not suppressed

    for i in range(len(units)):
        sim_prev = similarities[i-1] if i > 0 else 0
        sim_next = similarities[i] if i < len(similarities) else 0
        average_similarity = (sim_prev + sim_next) / 2.0
        
        if average_similarity > similarity_threshold or local_entropies[i] > entropy_threshold:
            suppressed_states[i] = True  # Mark segment as suppressed
            thought_masses[i] = 0
            local_entropies[i] = 0

    gradients = [abs(thought_masses[i+1] - mass) if i+1 < len(thought_masses) else 0 for i, mass in enumerate(thought_masses)]
    edges = [gradient > gradient_threshold for gradient in gradients]
    
    return units, edges, thought_masses, gradients, local_entropies, suppressed_states





def compute_adjacent_cosine_similarity(units):
    """Compute cosine similarity between adjacent units based on their TF-IDF vectors."""
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(units)
    
    similarities = []
    for i in range(len(units)-1):
        sim = cosine_similarity(tfidf_matrix[i], tfidf_matrix[i+1])
        similarities.append(sim[0][0])
    
    return similarities


def visualize_metrics(units, gradients, local_entropies, edges, similarities):
    segments = range(len(units))
    
    fig = plt.figure(figsize=(20, 15))
    gs = gridspec.GridSpec(3, 1, height_ratios=[1, 1, 0.75])
    fig.suptitle("Analysis of Thought-Mass as an Ontological Primitive", fontsize=16)

    # Plot gradient
    ax1 = fig.add_subplot(gs[0])
    ax1.plot(segments, gradients, marker='o', linestyle='-', color='green', lw=2, label='Gradient')
    ax1.axhline(y=np.mean(gradients), color='gray', linestyle='--', label='Average Gradient')
    for i, edge in enumerate(edges):
        if edge:
            ax1.axvline(x=i, color='red', linestyle='--', alpha=0.5)
    ax1.set_title('Gradient of Thought-Mass: Identifying Shifts in Context')
    ax1.set_ylabel('Gradient Value')
    ax1.legend()

    # Plot entropy
    ax2 = fig.add_subplot(gs[1], sharex=ax1)
    ax2.plot(segments, local_entropies, marker='o', linestyle='-', color='blue', lw=2, label='Entropy')
    ax2.axhline(y=np.mean(local_entropies), color='gray', linestyle='--', label='Average Entropy')
    for i, edge in enumerate(edges):
        if edge:
            ax2.axvline(x=i, color='red', linestyle='--', alpha=0.5)
    ax2.set_title('Local Entropy: Gauge of Information Density')
    ax2.set_ylabel('Entropy Value')
    ax2.legend()

    # Plot cosine similarity
    ax3 = fig.add_subplot(gs[2], sharex=ax1)
    ax3.plot(segments[:-1], similarities, marker='o', linestyle='-', color='purple', lw=2, label='Cosine Similarity')
    ax3.axhline(y=np.mean(similarities), color='gray', linestyle='--', label='Average Similarity')
    for i, edge in enumerate(edges[:-1]):
        if edge:
            ax3.axvline(x=i, color='red', linestyle='--', alpha=0.5)
    ax3.set_title('Cosine Similarity: Comparing Adjacent Segments for Contextual Continuity')
    ax3.set_xlabel('Segment Index')
    ax3.set_ylabel('Similarity Value')
    ax3.legend()
    
    plt.tight_layout()
    plt.subplots_adjust(top=0.93)
    plt.show()

def enhanced_visualize_3d_entropy_gradient_similarity(entropy, gradient, similarity):
    fig = plt.figure(figsize=(20, 15))
    ax = fig.add_subplot(111, projection='3d')
    
    # Scatter plot with dynamic sizing (increased size for better readability) and coloring based on similarity
    scatter = ax.scatter(entropy, gradient, similarity, c=similarity, cmap='viridis', s=200 * np.array(similarity), alpha=0.7, edgecolors='w', linewidth=1)
    
    # Setting labels and titles
    ax.set_xlabel('Entropy', fontsize=14)
    ax.set_ylabel('Differential Thought-Mass', fontsize=14)

    ax.set_zlabel('Cosine Similarity', fontsize=14)
    ax.set_title('3D Analysis of Entropy, Gradient, and Similarity in Thought-Mass', fontsize=16)
    
    # Add grid for better visualization
    ax.grid(True)
    ax.zaxis.grid(True)
    
    # Adding a colorbar to indicate similarity values
    cbar = fig.colorbar(scatter, ax=ax, orientation='vertical', fraction=0.03, pad=0.04)
    cbar.set_label('Cosine Similarity', rotation=270, labelpad=20, fontsize=12)
    
    # Beautify the axes
    ax.xaxis.pane.fill = ax.yaxis.pane.fill = ax.zaxis.pane.fill = False
    ax.xaxis.pane.set_edgecolor('w')
    ax.yaxis.pane.set_edgecolor('w')
    ax.zaxis.pane.set_edgecolor('w')
    ax.xaxis._axinfo["grid"]['color'] =  ax.yaxis._axinfo["grid"]['color'] = ax.zaxis._axinfo["grid"]['color'] = 'gray'
    
    plt.show()


file_path = input("Please enter the path to your text file: ")
text = read_file(file_path)

units, edges, thought_masses, gradients, local_entropies, suppressed_states = process_text(text, n=25, entropy_threshold=0.9, gradient_threshold=0.3, similarity_threshold=0.1)

# Ensure all lists have the same length for 2D visualization
similarities = compute_adjacent_cosine_similarity(units)
if len(similarities) != len(units) - 1:
    similarities.append(0)

display_processed_text(suppressed_states, units, edges)

print(f"Number of suppressed segments: {suppressed_states.count(True)}")

visualize_metrics(units, gradients, local_entropies, edges, similarities)


# Compute cosine similarity between the segments
similarities = compute_adjacent_cosine_similarity(units)
# Ensure all lists have the same length for 3D visualization
if len(similarities) != len(units):
    similarities.append(0) 

# Combine the features into a single data array
data = np.array([local_entropies, gradients, similarities]).T

# Normalize the data
scaler = StandardScaler()
normalized_data = scaler.fit_transform(data)

# Split the normalized data back into separate lists for visualization
local_entropies_normalized, gradients_normalized, similarities_normalized = normalized_data.T
similarities_normalized = np.clip(similarities_normalized, 0, 1)


# Use the normalized data for visualization
enhanced_visualize_3d_entropy_gradient_similarity(local_entropies_normalized, gradients_normalized, similarities_normalized)


