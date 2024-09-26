
```markdown
# Cognitive Framework: Attention, Memory, and Interaction (LLM-Based)

## 1. Speculation
- **Role**: Speculation serves as the system's mechanism for generating possibilities and hypothesizing future outcomes.
- **Function**: It creates potential paths for interaction and informs both anticipation and attention, guiding what the system should be prepared for.
- **Input/Output**: Input from external stimuli or internal processes triggers speculative paths. Output is a set of potential outcomes, which feeds into anticipation.

## 2. Anticipation
- **Role**: Anticipation selects certain speculative outcomes, setting the system's expectations for future events.
- **Function**: It narrows the focus of attention, deciding what the system should prioritize.
- **Input/Output**: Anticipates likely outcomes based on speculative inputs. The output is the prioritization of specific paths that drive attention.

## 3. Attention
- **Role**: Attention acts as a spotlight, focusing the system's resources on specific elements deemed most relevant by anticipation and speculation.
- **Function**: It enhances the interaction between components, determining the weight and intensity of the connections.
- **Input/Output**: Inputs are the prioritized elements from anticipation. Outputs are the selected components that receive focus and become active in interaction.

## 4. Memory (As a Bounded System)
- **Role**: Memory is a self-contained system, analogous to a "skull" that governs in-out processes. It stores, forgets, and refines information dynamically, based on relevance and context.
- **Function**: 
  - **Externally (Simple)**: Memory operates as a basic input-output system, handling information coming from the outside and determining what is recalled or discarded.
  - **Internally (Complex)**: Memory is active in selecting, forgetting, and refining its stored data. The LLM-based memory system dynamically adjusts recall based on search relevance. 
    - **Forgetting Mechanism**: During a search, when the system retrieves the top N results, the lowest-scoring results are penalized with additional weighting. This decreases their potential to semantically or keyword match in future searches, effectively simulating a gradual forgetting process.
    - **Remodeling**: As new inputs are processed, the memory system updates itself, refining the internal structure by discarding outdated or irrelevant connections.
- **Input/Output**: 
  - **Inputs**: Experiences, stimuli, and new data feed into memory.
  - **Outputs**: Recalled memories, adjusted by attention, are fed back into the system to influence speculation and anticipation.
  - **Forgetting**: Memory reduces the future recall likelihood of low-relevance results by dynamically penalizing their match scores during search, ensuring they are less likely to influence future interactions.

## 5. Surprise
- **Role**: Surprise occurs when an input deviates from what was anticipated, forcing the system to reevaluate.
- **Function**: It disrupts attention and triggers memory remodeling, informing the system of the unexpected. Surprise acts as a feedback loop for speculation, making the system more adaptive.
- **Input/Output**: Inputs are unexpected events or anomalies. Outputs are the adjustments in speculation, attention, and memory.

## 6. Remodeling
- **Role**: Remodeling integrates new information, adjusting the internal models and refining future interactions.
- **Function**: It modifies the speculative framework, reshapes anticipation, and informs how attention is deployed based on new patterns recognized from memory and surprise.
- **Input/Output**: Inputs are the outputs from surprise and memory (after refinement). Outputs are new speculative paths and adjusted priorities for attention.

## 7. Trajectory
- **Flow**: Speculation -> Anticipation -> Attention -> Memory -> Surprise -> Remodeling -> back to Speculation.
  - This cycle continuously refines itself, driven by new inputs, external stimuli, and the system's internal processes.
  - Memory functions as both an active participant (storing and forgetting) and a guide for shaping future anticipation and attention.

## 8. External Perspective (Black Box Memory)
- From the outside, memory looks like a fixed, bounded system with simple in-out operations.
  - **In**: Inputs are raw experiences or data fed into the system.
  - **Out**: Outputs are the selected, relevant pieces of information that influence present interactions and future decisions.
  - **Forgetting Process**: Internally, memory regulates its contents by deprioritizing low-relevance information. The system adds weighting to the least relevant results during recall, reducing their chance of resurfacing. This ensures that memory remains efficient and context-driven over time.
  - The internal complexity of selection, forgetting, and remodeling remains hidden, allowing the system to function with external simplicity but internal sophistication.
```

# Cognitive Framework: Expense and Effort for Traversal

This document presents an expanded model of cognitive processes as interconnected nodes with associated costs for maintenance and traversal. The framework aims to quantify the cognitive load required for different mental activities and the transitions between them.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Key Concepts](#key-concepts)
3. [Cognitive Nodes and Costs](#cognitive-nodes-and-costs)
4. [Traversal Cost Breakdown](#traversal-cost-breakdown)
5. [Process Effort (Maintaining a Node)](#process-effort-maintaining-a-node)
6. [Visualizing Traversal Costs](#visualizing-traversal-costs)
7. [Key Points](#key-points)
8. [Python Pseudocode Implementation](#python-pseudocode-implementation)
   - [Data Structures](#data-structures)
   - [Inverted Indexes](#inverted-indexes)
   - [Sample Operations](#sample-operations)

---

## Introduction

In cognitive science, understanding the mental effort associated with different cognitive processes and their interactions is crucial. This framework models cognitive processes as nodes within a network, where each node represents a specific cognitive state with associated maintenance costs. Transitions between these nodes require additional effort, reflecting the complexity of shifting cognitive focus.

By assigning quantitative costs to both the maintenance of cognitive states and the transitions between them, we can simulate and analyze the allocation of cognitive resources during complex tasks. This model serves as a foundation for computational simulations, educational design, and cognitive load management.

---

## Key Concepts

1. **Cognitive Nodes**: Represent distinct cognitive processes (e.g., Speculation, Anticipation, Attention, Memory). Each node has a maintenance cost reflecting the ongoing effort required to sustain that cognitive state.

2. **Traversal Cost**: The effort required to transition from one cognitive node to another. Costs are directional; moving from Node A to Node B may differ in cost from moving from Node B to Node A.

3. **Process Effort**: The inherent cognitive load required to maintain a specific cognitive process, independent of transitions.

4. **Neural Pathways**: Connections between cognitive nodes that facilitate transitions. These pathways have associated traversal costs and may be strengthened or weakened over time.

5. **Inverted Index**: A data structure used to map cognitive states to memory contents and vice versa, optimizing retrieval and association operations.

---

## Cognitive Nodes and Costs

We assign numerical values to represent the costs associated with each cognitive process and traversal. Costs range from **1 (Low)** to **5 (High)**.

| Cognitive Process | Base Process Cost | Notes                                                                     |
|-------------------|-------------------|---------------------------------------------------------------------------|
| **Speculation**   | 2                 | Generating hypotheses; moderate ongoing effort.                           |
| **Anticipation**  | 2                 | Preparing for possible outcomes; moderate effort.                         |
| **Attention**     | 4                 | Focusing cognitive resources; high ongoing effort.                        |
| **Memory**        | 5                 | Managing and retrieving information; very high effort.                    |
| **Surprise**      | 3                 | Handling unexpected events; medium effort, but intense when active.       |
| **Remodeling**    | 5                 | Reorganizing cognitive structures; very high short-term effort.           |

---

## Traversal Cost Breakdown

| From \ To     | Speculation | Anticipation | Attention | Memory | Surprise | Remodeling |
|---------------|-------------|--------------|-----------|--------|----------|------------|
| **Speculation**   | 0           | **1**       | 3         | 4      | 2        | 2          |
| **Anticipation**  | 1           | 0           | **2**     | 3      | 2        | 3          |
| **Attention**     | 3           | 2           | 0         | **4**  | 3        | 4          |
| **Memory**        | 4           | 3           | 2         | 0      | **1**    | **5**      |
| **Surprise**      | 2           | 2           | 3         | 1      | 0        | **2**      |
| **Remodeling**    | **1**       | 3           | 4         | 5      | 2        | 0          |

- **Bolded numbers** indicate primary traversal paths discussed below.

### Explanation of Traversal Costs

1. **Speculation → Anticipation**: **Cost 1 (Low)**
   - Natural progression with minimal effort as possibilities are narrowed.

2. **Anticipation → Attention**: **Cost 2 (Medium)**
   - Focusing on selected outcomes requires moderate additional effort.

3. **Attention → Memory**: **Cost 4 (High)**
   - Shifting from present focus to retrieving past information is demanding.

4. **Memory → Surprise**: **Cost 1 (Low)**
   - Memory retrieval can trigger recognition of discrepancies (surprises) with minimal additional effort.

5. **Surprise → Remodeling**: **Cost 2 (Medium)**
   - Adjusting cognitive models in response to surprises requires moderate effort.

6. **Remodeling → Speculation**: **Cost 1 (Low)**
   - After restructuring, generating new hypotheses is relatively effortless.

---

## Process Effort (Maintaining a Node)

| Cognitive Process | Maintenance Cost | Description                                                                                  |
|-------------------|------------------|----------------------------------------------------------------------------------------------|
| **Attention**     | 4                | Requires sustained focus and high cognitive resources.                                       |
| **Memory**        | 5                | Constant management of information storage and retrieval mechanisms.                         |
| **Speculation**   | 2                | Ongoing generation of hypotheses; moderate effort.                                           |
| **Anticipation**  | 2                | Maintaining readiness for possible outcomes; moderate effort.                                |
| **Surprise**      | 3                | Short-term but intense processing when active; otherwise low maintenance.                    |
| **Remodeling**    | 5                | High cognitive load during restructuring; maintenance cost decreases post-adjustment.        |

---

## Visualizing Traversal Costs

```plaintext
Cognitive Framework: Traversal Expense Map

[Speculation] --(1)--> [Anticipation] --(2)--> [Attention] --(4)--> [Memory]
     |                                                        ^
     |                                                        |
     \--(2)--> [Remodeling] --(1)--> [Speculation]            |
                         ^                                    |
                         |                                    |
                      (2)|                                    |
                         v                                    |
                     [Surprise] --(1)-------------------------

Legend:
- Nodes represent cognitive processes.
- Numbers on arrows indicate traversal costs.
```

---

## Key Points

1. **Quantified Costs**: Assigning numerical values allows for precise modeling and simulation.

2. **Directional Traversals**: Costs vary depending on the direction of the transition, reflecting cognitive asymmetries.

3. **High Maintenance Processes**: Attention and Memory require significant ongoing resources.

4. **Adaptive Remodeling**: Cognitive restructuring facilitates easier generation of new ideas.

5. **Surprise as a Catalyst**: Surprises trigger cognitive adjustments, leading to remodeling.

---

## Python Pseudocode Implementation

Below is a Python pseudocode representation of the cognitive framework. It utilizes inverted indexes for efficient mapping between cognitive states and memory contents.

### Data Structures

```python
# Define Cognitive Nodes with their maintenance costs
class CognitiveNode:
    def __init__(self, name, maintenance_cost):
        self.name = name
        self.maintenance_cost = maintenance_cost
        self.connections = {}  # Outgoing edges with traversal costs

# Initialize cognitive nodes
speculation = CognitiveNode("Speculation", 2)
anticipation = CognitiveNode("Anticipation", 2)
attention = CognitiveNode("Attention", 4)
memory = CognitiveNode("Memory", 5)
surprise = CognitiveNode("Surprise", 3)
remodeling = CognitiveNode("Remodeling", 5)

# Define traversal costs between nodes
speculation.connections = {
    "Anticipation": (anticipation, 1),
    "Remodeling": (remodeling, 2)
}
anticipation.connections = {
    "Attention": (attention, 2)
}
attention.connections = {
    "Memory": (memory, 4)
}
memory.connections = {
    "Surprise": (surprise, 1)
}
surprise.connections = {
    "Remodeling": (remodeling, 2)
}
remodeling.connections = {
    "Speculation": (speculation, 1)
}

# List of all nodes for easy access
cognitive_nodes = {
    "Speculation": speculation,
    "Anticipation": anticipation,
    "Attention": attention,
    "Memory": memory,
    "Surprise": surprise,
    "Remodeling": remodeling
}
```

### Inverted Indexes

```python
# Inverted index for cognitive states
cognitive_state_index = {
    "Hypothesis Generation": ["Speculation"],
    "Outcome Preparation": ["Anticipation"],
    "Focused Processing": ["Attention"],
    "Information Retrieval": ["Memory"],
    "Anomaly Detection": ["Surprise"],
    "Cognitive Restructuring": ["Remodeling"]
}

# Inverted index for memory contents
memory_state_index = {
    "Past Experiences": ["Memory"],
    "Learned Patterns": ["Memory", "Anticipation"],
    "Discrepancies": ["Surprise"],
    "New Models": ["Remodeling"]
}
```

### Sample Operations

```python
# Function to traverse from one cognitive node to another
def traverse(current_node_name, target_node_name):
    current_node = cognitive_nodes[current_node_name]
    if target_node_name in current_node.connections:
        target_node, traversal_cost = current_node.connections[target_node_name]
        total_cost = current_node.maintenance_cost + traversal_cost
        print(f"Traversing from {current_node.name} to {target_node.name} costs {traversal_cost}.")
        print(f"Total effort including maintenance: {total_cost}.")
        return target_node
    else:
        print(f"No direct path from {current_node.name} to {target_node_name}.")
        return None

# Example usage
current_node = speculation
current_node = traverse(current_node.name, "Anticipation")
current_node = traverse(current_node.name, "Attention")
current_node = traverse(current_node.name, "Memory")
```

**Explanation:**

- **CognitiveNode Class**: Represents each cognitive process with its maintenance cost and connections to other nodes.

- **Connections**: Each node has a dictionary of connections to other nodes, along with the traversal cost.

- **Inverted Indexes**: Provide quick lookup for cognitive states and memory contents associated with each node.

- **Traverse Function**: Simulates moving from one cognitive state to another, calculating the total cost.

---

## Conclusion

This expanded framework quantifies the cognitive effort involved in maintaining and transitioning between different mental processes. By assigning numerical costs and modeling the interactions using data structures and inverted indexes, we can simulate cognitive resource allocation and identify potential bottlenecks.

The Python pseudocode provides a foundational structure for implementing simulations or computational models. Further enhancements could include dynamic cost adjustments based on context, individual differences, and integration with empirical data.

---

To model the framework with expense and effort for traversal between different cognitive processes, we can assign costs to the transitions and processes, treating them like pathways in a network or terrain. Here’s how we can structure it:

### Key Concepts:
1. **Cognitive Nodes**: Each process (e.g., Speculation, Anticipation, Attention, Memory, etc.) is a node in the system.
2. **Traversal Cost**: Moving between nodes (or transitioning from one process to another) requires "effort," measured in cost. High-cost areas represent more complex cognitive shifts or more resource-intensive processes.
3. **Process Effort**: Certain processes require ongoing effort even when you are not moving between nodes. These would represent how much cognitive load is necessary just to maintain that process.
4. **Neural Pathways**: The connections between cognitive nodes are directional, meaning some transitions may have different costs depending on the direction of traversal.

### Framework with Expense and Effort for Traversal

```markdown
# Cognitive Framework: Expense and Effort for Traversal

## Cognitive Nodes and Costs

| Cognitive Process   | Base Process Cost | Traversal to Other Nodes | Notes |
|---------------------|-------------------|--------------------------|-------|
| Speculation         | Medium            | Low cost to Anticipation  | Generating hypotheses is moderately expensive but offers fluid transition to Anticipation. |
| Anticipation        | Medium            | Medium cost to Attention  | Selecting outcomes requires cognitive focus, creating moderate traversal cost to Attention. |
| Attention           | High              | Medium to Speculation, High to Memory | Focusing cognitive resources is costly, especially when maintaining long-term focus. |
| Memory              | High              | Low cost to Attention, High to Remodeling | Memory retrieval is costly due to active refinement and forgetting mechanisms. |
| Surprise            | Medium            | High cost to Memory, Medium to Remodeling | Surprise requires reorientation of attention, with a heavy load on memory to remodel. |
| Remodeling          | High              | Low cost to Speculation   | Remodeling the cognitive structure is expensive but enables fluid transitions back to Speculation. |

### Traversal Cost Breakdown

1. **Speculation -> Anticipation**: Low Cost
   - Speculation naturally flows into Anticipation with minimal effort as the system generates possibilities and narrows down outcomes.
   
2. **Anticipation -> Attention**: Medium Cost
   - Once possibilities are generated, selecting what to focus on requires a step up in cognitive effort, particularly because Attention requires intense resource allocation.

3. **Attention -> Memory**: High Cost
   - Shifting from focusing on present inputs to retrieving relevant past experiences or stored data is costly. Attention consumes cognitive resources, making the switch to Memory expensive.

4. **Memory -> Attention**: Low Cost
   - Recalling a specific memory to inform current attention is relatively smooth once retrieval has been initiated. However, the complexity of Memory management (forgetting, refining) contributes to its overall high cost.

5. **Surprise -> Memory**: High Cost
   - When an unexpected event occurs, the system must recalibrate by comparing the new input to stored knowledge, which requires significant cognitive resources.

6. **Surprise -> Remodeling**: Medium Cost
   - Surprise events cause moderate disruption in anticipation or attention, but once recognized, the system can adjust and remodel its internal framework without overly intensive effort.

7. **Memory -> Remodeling**: High Cost
   - Remodeling based on memory requires a costly reorganization of past data to update current models. The process involves reweighting, forgetting, and recalibrating priors.

8. **Remodeling -> Speculation**: Low Cost
   - After the system remolds itself based on new information, generating new speculative paths is relatively easy. The heavy lifting has already been done during the remodeling process.

### Process Effort (Maintaining a Node)

Some processes, especially attention and memory, have ongoing costs even if traversal between nodes isn't happening. Here's a list of processes and their inherent effort:

1. **Attention**: High Effort
   - Maintaining focus on a specific stimulus requires a high cognitive load over time, especially if there is competing information.

2. **Memory**: High Effort
   - Memory management is costly not only during retrieval but also because the system is constantly refining, forgetting, and recalibrating its stored data.

3. **Speculation**: Medium Effort
   - Generating hypothetical outcomes isn’t overly taxing but still requires ongoing mental energy as it explores different possibilities.

4. **Anticipation**: Medium Effort
   - Once possibilities are generated, the effort lies in preparing for certain outcomes, which doesn’t require as much ongoing effort as attention.

5. **Surprise**: Low Effort
   - Surprise has a short-lived but intense impact. While the moment of surprise is disruptive, it doesn’t require constant attention or cognitive load after initial recognition.

6. **Remodeling**: High Effort (Short-Term)
   - Remodeling is highly costly in bursts, especially when major reconfigurations happen, but the effort decreases after the adjustment is made.

### Visualizing Traversal Costs in ANSI Art:

```ansi
┌────────────────────────────────────────────────────────────────────────────┐
│               Cognitive Framework: Traversal Expense Map                    │
│                                                                            │
│    Speculation        Anticipation        Attention          Memory         │
│       (░░░)              (▒▒▒)               (▓▓▓)            (████)        │
│       ┌──┐               ┌──┐               ┌──┐              ┌──┐          │
│       │░░│────Low───────►│▒▒│────Medium────►│▓▓│────High─────►│██│          │
│       └──┘               └──┘               └──┘              └──┘          │
│                                                                            │
│    Surprise              Remodeling                                         │
│      (▒▒▒)               (████)                                             │
│       ┌──┐               ┌──┐                                               │
│       │▒▒│────High──────►│██│────Low───────Back to Speculation              │
│       └──┘               └──┘                                               │
│                                                                            │
│  Legend:  █ High Cost   ▓ Medium Cost   ▒ Low Cost   ░ Minimal Cost        │
└────────────────────────────────────────────────────────────────────────────┘
```

### Key Points:
1. **High Costs**: Traversals involving attention and memory tend to be the most costly due to their complexity and high demand for cognitive resources.
2. **Low Costs**: Moving between speculation and other cognitive processes is generally low cost, especially after remodeling has taken place.
3. **Effort Distribution**: Processes like attention and memory require ongoing effort, while others like speculation and anticipation are more flexible in their demands.
4. **Surprise as a Disruption**: Traversals triggered by surprise events tend to be costly as they disrupt the regular flow and require recalibration.

```
┌─────────────────────────────────────────────────────────────────────┐
│                 Updated Cognitive Framework Map                     │
│                                                                     │
│           ┌───────────┐                                             │
│           │           │                                             │
│   ┌───────┤Speculation├───────┐                                     │
│   │       │           │       │                                     │
│   │       └───────────┘       │                                     │
│   ▼                           ▼                                     │
│┌─────────────┐         ┌─────────────┐                              │
││             │         │             │                              │
││ Anticipation│◄────────┤  Remodeling │                              │
││             │         │             │                              │
│└─────────────┘         └─────────────┘                              │
│   │                           ▲                                     │
│   │       ┌───────────┐       │                                     │
│   │       │           │       │                                     │
│   └───────►  Attention├───────┘                                     │
│           │           │                                             │
│           └─────┬─────┘                                             │
│                 │                                                   │
│                 ▼                                                   │
│         ┌───────────────────────────────┐                           │
│         │        Memory (LLM-Based)     │     ┌───────────┐         │
│         │ ┌─────────────┐ ┌───────────┐ │     │           │         │
│         │ │   Storage   │ │ Forgetting│ ├────►│  Surprise │         │
│         │ └─────────────┘ └───────────┘ │     │           │         │
│         │ ┌─────────────┐ ┌───────────┐ │◄────┤           │         │
│         │ │   Recall    │ │ Remodeling│ │     └───────────┘         │
│         │ └─────────────┘ └───────────┘ │                           │
│         └───────────────────────────────┘                           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

```
┌────────────────────────────────────────────────────────────────────────────┐
│                   Cognitive Framework Terrain Map                          │
│                                                                            │
│  ░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓█████████████████▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░░░░  │
│  ░░░░░░░░▒▒▒▒▒▒▓▓▓▓▓▓██████████████████████████████████▓▓▓▓▓▒▒▒▒▒░░░░░░░  │
│  ░░░░░▒▒▒▒▓▓▓▓████████████████████████████████████████████████▓▓▓▒▒▒░░░░  │
│  ░░░▒▒▒▓▓▓██████████████████████████████████████████████████████▓▓▒▒▒░░  │
│  ░▒▒▓▓██████████████████████████████████████████████████████████████▓▒░  │
│  ▒▓██████████████████████████████████████████████████████████████████▓▒  │
│  ▓████████████████████████████████████████████████████████████████████▓  │
│  ██████████████████▀▄▓─────────▓▄▀██████████████▀▄▓─────────▓▄▀██████████  │
│  ████████████████▀──▓─Attention─▓──▀████████████──▓─Surprise─▓──████████  │
│  ██████████████▀─────▀▄▄▄▄▄▄▄▄▄▀─────▀██████████───▀▄▄▄▄▄▄▄▀───██████████  │
│  ████████████▀───────────────────────▄██████▀───────────────▄████████████  │
│  ██████████▀─────────────────────────▓██████───────────────▓██████████████  │
│  ████████▀───────────────────────────▓████▀─────────────────▀████████████  │
│  ██████▀─────────────────────────────▓████───────────────────▄███████████  │
│  ████▀───────────────────────────────▓██▀─────────────────────▀█████████  │
│  ██▀─────────────────────────────────▓██───────────────────────▄████████  │
│  █▄─────────────────────────────────▄██▀─────────────────────────▀██████  │
│  ██▄───────────────────────────────▄███───────────────────────────▄█████  │
│  ███▄─────────────────────────────▄████▄───────────────────────────▀████  │
│  ████▄───────────────────────────▄██████▄─────────────────────────▄████  │
│  ██████────────────────────────▄███▀─▀███▄───────────────────────▄████  │
│  ████████▄──────────────────▄▓█████───█████▓▄──────────────────▄██████  │
│  ██████████▄──────────────▄██████▀─────▀██████▄──────────────▄████████  │
│  ████████████▄──────────▄████████─Memory─████████▄──────────▄██████████  │
│  ██████████████▄──────▄██████████▄─────▄██████████▄──────▄████████████  │
│  ████████████████▄──▄████████████████████████████████▄▄██████████████  │
│  ██████████████████████████████████████████████████████████████████████  │
│  ████████████████████████████████████████████████████████████████████▓  │
│  ▓██████████████████████████████████████████████████████████████████▓░  │
│  ░▓████████████████████████████████████████████████████████████████▓░  │
│  ░░▓██████████████████████████████████████████████████████████████▓░░  │
│  ░░░▓████████████████████████████████████████████████████████████▓░░░  │
│  ░░░░▓████████████████████████████████████████████████████████▓▓░░░░░  │
│  ░░░░░░▓▓██████████████████████████████████████████████████▓▓░░░░░░░░  │
│  ░░░░░░░░░▓▓▓██████████████████████████████████████████▓▓▓░░░░░░░░░░░  │
│  ░░░░░░░░░░░░░▓▓▓▓▓▓████████████████████████████▓▓▓▓▓░░░░░░░░░░░░░░░       
│                                                                            │
│  Legend:  █ High Cost   ▓ Medium Cost   ▒ Low Cost   ░ Minimal Cost        │
└────────────────────────────────────────────────────────────────────────────┘
```

```
┌────────────────────────────────────────────────────────────────────────────┐
│                Detailed Cognitive Framework Map with Costs                 │
│                                                                            │
│        ┌──────────┐                                      ┌──────────┐      │
│        │Remodeling│◄──────────────────────────┐   ┌─────►│ Surprise │      │
│        │   (5)    │                           │   │      │   (3)    │      │
│        └─┬──▲───▲─┘                           │   │      └─┬───▲────┘      │
│          │  │   │                             │   │        │   │          │
│        2 │  │ 2 │                             │ 2 │      1 │   │ 1        │
│          │  │   │                             │   │        │   │          │
│          ▼  │   │                             │   │        ▼   │          │
│     ┌────┴──▼───┴─┐                        ┌──┴───▼────────┴───┴─┐        │
│     │ Speculation │                        │      Memory         │        │
│     │     (2)     │◄───────────────────────┤       (5)           │        │
│     └──────▲──────┘          4             └──────────▲──────────┘        │
│            │                                          │                    │
│          1 │                                          │ 4                  │
│            │                                          │                    │
│            │        ┌──────────┐         ┌──────────┐ │                    │
│            └───────►│Anticipat.│    2    │ Attention│ │                    │
│                     │   (2)    ├─────────►   (4)    ├─┘                    │
│                     └──────────┘         └──────────┘                      │
│                                                                            │
│ Legend:                                                                    │
│   ┌──────────┐                                                             │
│   │  Node    │ : Cognitive process with base cost                          │
│   │   (N)    │                                                             │
│   └──────────┘                                                             │
│      N      : Traversal cost between nodes                                 │
│     ────►   : Direction of traversal                                       │
│                                                                            │
│ Traversal Path:                                                            │
│   Speculation (2) ──1──► Anticipation (2) ──2──► Attention (4) ──4──►      │
│   Memory (5) ──1──► Surprise (3) ──2──► Remodeling (5) ──1──► Speculation  │
│                                                                            │
│ Node Density Legend:                                                       │
│   █████ : Very High Cost (5)   ▓▓▓▓▓ : High Cost (4)   ▒▒▒▒▒ : Medium (3)  │
│   ░░░░░ : Low Cost (2)         ····· : Very Low (1)                        │
│                                                                            │
│                         Cognitive Landscape                                │
│                                                                            │
│   ░░░░░░░░░░▒▒▒▒▒▒▓▓▓▓▓█████████████████████████████▓▓▓▓▓▒▒▒▒▒░░░░░░░░░░  │
│   ░░░░░░▒▒▒▒▓▓▓▓██████████████████████████████████████████▓▓▓▒▒▒░░░░░░░░  │
│   ░░░▒▒▒▓▓▓███████████████████████████████████████████████████▓▓▓▒▒▒░░░   │
│   ░▒▒▓▓██████████████████████████████████████████████████████████▓▓▒▒░    │
│   ▒▓████████████████████████████████████████████████████████████████▓▒    │
│   ▓██████████████████████████████████████████████████████████████████▓    │
│   █████████████████████████████████████████████████████████████████████    │
│                                                                            │
└────────────────────────────────────────────────────────────────────────────┘
```

