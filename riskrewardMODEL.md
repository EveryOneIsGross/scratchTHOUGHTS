# Dice Choice System for LLMs

## Core Mechanics
- LLM receive 1-5 dice each cycle, based on their character's condition
- Dice are numbered 1-6, with higher numbers generally offering better odds of success
- Dice are spent on actions, with the outcome determined by the die's value and action's difficulty

## Dice Probability Table
| Die Number | Probability                             |
|------------|-----------------------------------------|
| One        | 50% Neutral, 50% Negative               |
| Two        | 50% Neutral, 50% Negative               |
| Three      | 25% Positive, 50% Neutral, 25% Negative |
| Four       | 25% Positive, 50% Neutral, 25% Negative |
| Five       | 50% Positive, 50% Neutral               |
| Six        | 100% Positive                           |

## Action Resolution
- Each die roll can result in Positive, Neutral, or Negative outcomes
- Higher-numbered dice have better chances of positive outcomes
- Skills and perks can modify the effectiveness of dice rolls

## Risk Levels
- Actions are categorized as Safe, Risky, or Dangerous
- Higher risk levels can result in loss of condition, energy, or resources on failed or neutral outcomes

## Resource Management
- LLM must balance condition, energy, and other resources
- Maintaining good condition is crucial for having more dice available each cycle

## Strategic Elements
- Choosing which actions to attempt with which dice
- Balancing risk and reward

```python
import json
import random
from openai import OpenAI

class LLMInterface:
    def __init__(self, base_url, api_key):
        self.client = OpenAI(base_url=base_url, api_key=api_key)

    def query(self, messages, model="llama2"):
        response = self.client.chat.completions.create(
            model=model,
            messages=messages
        )
        return response.choices[0].message.content

class DicePool:
    def __init__(self, num_dice):
        self.dice = [random.randint(1, 6) for _ in range(num_dice)]

    def roll(self):
        return random.choice(self.dice)

class Action:
    def __init__(self, name, risk_level):
        self.name = name
        self.risk_level = risk_level

    def resolve(self, dice_roll):
        if self.risk_level == "Safe":
            return "Positive" if dice_roll >= 3 else "Neutral"
        elif self.risk_level == "Risky":
            if dice_roll >= 5:
                return "Positive"
            elif dice_roll >= 3:
                return "Neutral"
            else:
                return "Negative"
        else:  # Dangerous
            return "Positive" if dice_roll == 6 else "Negative"

class SystemState:
    def __init__(self, initial_condition=3):
        self.condition = initial_condition
        self.history = []

    def update(self, action_result):
        if action_result == "Positive":
            self.condition = min(5, self.condition + 1)
        elif action_result == "Negative":
            self.condition = max(1, self.condition - 1)
        self.history.append((action_result, self.condition))

class LLMDiceSystem:
    def __init__(self, base_url, api_key):
        self.llm = LLMInterface(base_url, api_key)
        self.state = SystemState()

    def generate_actions(self):
        prompt = {
            "role": "system",
            "content": "Generate 3 possible actions for an adventure game. Each action should have a name and a risk level (Safe, Risky, or Dangerous). Provide the output as a JSON array."
        }
        response = self.llm.query([prompt])
        return json.loads(response)

    def process_cycle(self):
        actions = self.generate_actions()
        dice_pool = DicePool(self.state.condition)
        
        print(f"Current condition: {self.state.condition}")
        print("Available actions:")
        for i, action in enumerate(actions):
            print(f"{i+1}. {action['name']} ({action['risk_level']})")
        
        choice = random.randint(0, len(actions) - 1)
        chosen_action = Action(actions[choice]['name'], actions[choice]['risk_level'])
        
        dice_roll = dice_pool.roll()
        result = chosen_action.resolve(dice_roll)
        
        self.state.update(result)
        
        return {
            "action": chosen_action.name,
            "risk_level": chosen_action.risk_level,
            "dice_roll": dice_roll,
            "result": result,
            "new_condition": self.state.condition
        }

def main():
    system = LLMDiceSystem('http://localhost:11434/v1', 'ollama')
    
    for i in range(5):  # Run for 5 cycles
        print(f"\nCycle {i+1}")
        result = system.process_cycle()
        print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
```

# LLM Dice Choice Cybernetic System

## System Overview

1. Input Module: Receives user queries and system state
2. Resource Management Module: Manages dice allocation based on system condition
3. Action Resolution Module: Uses dice to determine action outcomes
4. LLM Interface Module: Interacts with the LLM API
5. Output Generation Module: Produces responses based on action outcomes
6. Learning Module: Adjusts system parameters based on outcomes
7. State Tracking Module: Maintains system condition and history

## Cybernetic Loop

1. User input received
2. Current state assessed, dice allocated
3. Action resolved using dice
4. LLM queried based on action outcome
5. Response generated and delivered to user
6. System learns from interaction
7. State updated for next cycle

## Implementation Plan

1. Set up basic API interaction
2. Implement dice allocation system
3. Create action resolution mechanism
4. Develop state tracking and learning modules
5. Integrate all components
6. Test and refine

## Detailed Python Implementation Steps

1. Set up API interaction:
   - Use the provided code as a starting point
   - Create a wrapper class for API interactions

2. Implement dice allocation:
   - Create a `DicePool` class to manage dice
   - Implement methods for allocating and rolling dice

3. Create action resolution:
   - Define action types (Safe, Risky, Dangerous)
   - Implement outcome determination based on dice rolls

4. Develop state tracking and learning:
   - Create a `SystemState` class to track condition and resources
   - Implement a simple learning mechanism to adjust parameters

5. Integrate components:
   - Create a main `LLMDiceSystem` class to orchestrate all modules
   - Implement the cybernetic loop in this class

6. Test and refine:
   - Create a simple CLI for interaction
   - Run multiple cycles and adjust as needed
