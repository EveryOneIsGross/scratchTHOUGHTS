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


## Integration into Sim SIM

I see. Focusing the dice system on the market and work aspects of your simulation is an interesting approach. This could create a more dynamic economic system within your game. Let's explore how we can implement this.



```javascript
// Dice rolling function
function rollDice(num) {
  return Array(num).fill().map(() => Math.floor(Math.random() * 6) + 1);
}

// Work function with dice system
function work() {
  const workRisk = calculateWorkRisk();
  const diceRoll = rollDice(sim.dicePool);
  const outcome = resolveWorkOutcome(diceRoll, workRisk);
  
  if (outcome.success) {
    const producedItems = produceItems(outcome.productionBonus);
    addItemsToMarket(producedItems);
    sim.money += outcome.earnings;
    addToDialog(`The Sim worked successfully, earning $${outcome.earnings} and producing items.`);
  } else {
    sim.condition -= outcome.conditionLoss;
    addToDialog(`The Sim had a difficult day at work, losing ${outcome.conditionLoss} condition.`);
  }
  
  updateSimCondition();
}

// Calculate work risk based on sim's condition
function calculateWorkRisk() {
  if (sim.condition > 7) return "Safe";
  if (sim.condition > 4) return "Risky";
  return "Dangerous";
}

// Resolve work outcome based on dice roll and risk
function resolveWorkOutcome(diceRoll, risk) {
  const highestRoll = Math.max(...diceRoll);
  
  switch(risk) {
    case "Safe":
      if (highestRoll >= 3) return { success: true, earnings: 50 + (highestRoll - 3) * 10, productionBonus: highestRoll - 2 };
      return { success: false, conditionLoss: 1 };
    case "Risky":
      if (highestRoll >= 4) return { success: true, earnings: 80 + (highestRoll - 4) * 20, productionBonus: highestRoll - 3 };
      return { success: false, conditionLoss: 2 };
    case "Dangerous":
      if (highestRoll >= 5) return { success: true, earnings: 120 + (highestRoll - 5) * 40, productionBonus: highestRoll - 4 };
      return { success: false, conditionLoss: 3 };
  }
}

// Produce items based on work success
function produceItems(productionBonus) {
  const items = Object.keys(marketItems);
  const producedItems = {};
  
  for (let i = 0; i < productionBonus; i++) {
    const randomItem = items[Math.floor(Math.random() * items.length)];
    producedItems[randomItem] = (producedItems[randomItem] || 0) + 1;
  }
  
  return producedItems;
}

// Add produced items to market
function addItemsToMarket(items) {
  for (const [item, quantity] of Object.entries(items)) {
    marketItems[item].quantity += quantity;
    // Adjust price based on new supply
    marketItems[item].price = Math.max(1, Math.floor(marketItems[item].price * (1 - 0.05 * quantity)));
  }
  updateMarket();
}

// Update sim's condition
function updateSimCondition() {
  sim.dicePool = Math.max(1, Math.min(5, Math.floor(sim.condition / 2)));
}

// Market transaction with dice system
function marketTransaction(action, item) {
  const transactionRisk = calculateMarketRisk(action, item);
  const diceRoll = rollDice(sim.dicePool);
  const outcome = resolveMarketOutcome(diceRoll, transactionRisk);
  
  if (outcome.success) {
    if (action === 'buy') {
      buyMarketItem(item, outcome.priceModifier);
    } else {
      sellMarketItem(item, outcome.priceModifier);
    }
  } else {
    addToDialog(`The market transaction for ${marketItems[item].name} failed. ${outcome.reason}`);
  }
  
  updateMarketPrices(item, outcome);
}

// Calculate market risk
function calculateMarketRisk(action, item) {
  const priceVolatility = Math.abs(marketItems[item].price - marketItems[item].basePrice) / marketItems[item].basePrice;
  if (priceVolatility < 0.1) return "Safe";
  if (priceVolatility < 0.3) return "Risky";
  return "Dangerous";
}

// Resolve market outcome
function resolveMarketOutcome(diceRoll, risk) {
  const highestRoll = Math.max(...diceRoll);
  
  switch(risk) {
    case "Safe":
      if (highestRoll >= 2) return { success: true, priceModifier: 1 + (highestRoll - 2) * 0.05 };
      return { success: false, reason: "Market conditions unfavorable." };
    case "Risky":
      if (highestRoll >= 3) return { success: true, priceModifier: 1 + (highestRoll - 3) * 0.1 };
      return { success: false, reason: "Market too volatile." };
    case "Dangerous":
      if (highestRoll >= 4) return { success: true, priceModifier: 1 + (highestRoll - 4) * 0.2 };
      return { success: false, reason: "Extreme market fluctuations." };
  }
}

// Update market prices based on transactions
function updateMarketPrices(item, outcome) {
  if (outcome.success) {
    marketItems[item].price = Math.floor(marketItems[item].price * outcome.priceModifier);
  } else {
    // Market becomes more volatile after failed transactions
    marketItems[item].price = Math.floor(marketItems[item].price * (1 + (Math.random() - 0.5) * 0.2));
  }
  updateMarket();
}

// Modify existing buyMarketItem and sellMarketItem functions to use the new system
function buyMarketItem(item, priceModifier) {
  const finalPrice = Math.floor(marketItems[item].price * priceModifier);
  if (sim.money >= finalPrice && marketItems[item].quantity > 0) {
    sim.money -= finalPrice;
    marketItems[item].quantity--;
    if (!sim.inventory[item]) {
      sim.inventory[item] = 0;
    }
    sim.inventory[item]++;
    addToDialog(`The Sim bought a ${marketItems[item].name} for $${finalPrice}.`);
    updateMarket();
    updateStats();
  } else {
    addToDialog(`The Sim can't afford ${marketItems[item].name} or it's out of stock.`);
  }
}

function sellMarketItem(item, priceModifier) {
  const finalPrice = Math.floor(marketItems[item].price * priceModifier);
  if (sim.inventory[item] && sim.inventory[item] > 0) {
    sim.money += finalPrice;
    marketItems[item].quantity++;
    sim.inventory[item]--;
    addToDialog(`The Sim sold a ${marketItems[item].name} for $${finalPrice}.`);
    updateMarket();
    updateStats();
  } else {
    addToDialog(`The Sim doesn't have any ${marketItems[item].name} to sell.`);
  }
}

// Update the main simulation loop to include these new systems
function simulateStep() {
  if (sim.currentItem && sim.currentItem.name === 'Work') {
    work();
  } else {
    // ... existing simulation logic ...
  }
  
  // Periodically update market prices
  if (Math.random() < 0.1) { // 10% chance each step
    updateMarketPrices(Object.keys(marketItems)[Math.floor(Math.random() * Object.keys(marketItems).length)], { success: true, priceModifier: 1 + (Math.random() - 0.5) * 0.1 });
  }
  
  drawHouse();
  updateMarket();
}

```

This system integrates the dice mechanics into the work and market aspects of your simulation. Here's how it works:

1. Work System:
   - The sim's condition determines the risk level of work (Safe, Risky, Dangerous).
   - Dice rolls determine the success of the workday, with higher rolls needed for riskier conditions.
   - Successful work results in earning money and producing items for the market.
   - Failed work results in a loss of condition for the sim.

2. Market System:
   - Market transactions (buying/selling) now use the dice system.
   - The risk of a transaction is determined by the price volatility of the item.
   - Successful transactions may result in better prices, while failed transactions can lead to more volatile prices.
   - The market prices are updated based on supply (from work production) and transaction outcomes.

3. Resource Simulation:
   - Work produces items that are added to the market, simulating supply.
   - Market transactions simulate demand.
   - Prices fluctuate based on supply, demand, and the outcomes of dice rolls.

To implement this system:

1. Add the new functions to your existing code.
2. Modify your `work()` function to use the new dice-based system.
3. Update your market transaction functions (`buyMarketItem` and `sellMarketItem`) to use the new `marketTransaction` function.
4. Modify your main simulation loop (`simulateStep`) to include periodic market updates.

This system creates a more dynamic economy where the sim's work directly affects the market, and market transactions carry an element of risk and reward. The dice system adds unpredictability to both work and market interactions, making the economic aspect of your simulation more engaging and complex.

```js
// Dice rolling function
function rollDice(num) {
  return Array(num).fill().map(() => Math.floor(Math.random() * 6) + 1);
}

// Work function with dice system
function work() {
  const workRisk = calculateWorkRisk();
  const diceRoll = rollDice(sim.dicePool);
  const outcome = resolveWorkOutcome(diceRoll, workRisk);
  
  if (outcome.success) {
    const producedItems = produceItems(outcome.productionBonus);
    addItemsToMarket(producedItems);
    sim.money += outcome.earnings;
    addToDialog(`The Sim worked successfully, earning $${outcome.earnings} and producing items.`);
  } else {
    sim.condition -= outcome.conditionLoss;
    addToDialog(`The Sim had a difficult day at work, losing ${outcome.conditionLoss} condition.`);
  }
  
  updateSimCondition();
}

// Calculate work risk based on sim's condition
function calculateWorkRisk() {
  if (sim.condition > 7) return "Safe";
  if (sim.condition > 4) return "Risky";
  return "Dangerous";
}

// Resolve work outcome based on dice roll and risk
function resolveWorkOutcome(diceRoll, risk) {
  const highestRoll = Math.max(...diceRoll);
  
  switch(risk) {
    case "Safe":
      if (highestRoll >= 3) return { success: true, earnings: 50 + (highestRoll - 3) * 10, productionBonus: highestRoll - 2 };
      return { success: false, conditionLoss: 1 };
    case "Risky":
      if (highestRoll >= 4) return { success: true, earnings: 80 + (highestRoll - 4) * 20, productionBonus: highestRoll - 3 };
      return { success: false, conditionLoss: 2 };
    case "Dangerous":
      if (highestRoll >= 5) return { success: true, earnings: 120 + (highestRoll - 5) * 40, productionBonus: highestRoll - 4 };
      return { success: false, conditionLoss: 3 };
  }
}

// Produce items based on work success
function produceItems(productionBonus) {
  const items = Object.keys(marketItems);
  const producedItems = {};
  
  for (let i = 0; i < productionBonus; i++) {
    const randomItem = items[Math.floor(Math.random() * items.length)];
    producedItems[randomItem] = (producedItems[randomItem] || 0) + 1;
  }
  
  return producedItems;
}

// Add produced items to market
function addItemsToMarket(items) {
  for (const [item, quantity] of Object.entries(items)) {
    marketItems[item].quantity += quantity;
    // Adjust price based on new supply
    marketItems[item].price = Math.max(1, Math.floor(marketItems[item].price * (1 - 0.05 * quantity)));
  }
  updateMarket();
}

// Update sim's condition
function updateSimCondition() {
  sim.dicePool = Math.max(1, Math.min(5, Math.floor(sim.condition / 2)));
}

// Market transaction with dice system
function marketTransaction(action, item) {
  const transactionRisk = calculateMarketRisk(action, item);
  const diceRoll = rollDice(sim.dicePool);
  const outcome = resolveMarketOutcome(diceRoll, transactionRisk);
  
  if (outcome.success) {
    if (action === 'buy') {
      buyMarketItem(item, outcome.priceModifier);
    } else {
      sellMarketItem(item, outcome.priceModifier);
    }
  } else {
    addToDialog(`The market transaction for ${marketItems[item].name} failed. ${outcome.reason}`);
  }
  
  updateMarketPrices(item, outcome);
}

// Calculate market risk
function calculateMarketRisk(action, item) {
  const priceVolatility = Math.abs(marketItems[item].price - marketItems[item].basePrice) / marketItems[item].basePrice;
  if (priceVolatility < 0.1) return "Safe";
  if (priceVolatility < 0.3) return "Risky";
  return "Dangerous";
}

// Resolve market outcome
function resolveMarketOutcome(diceRoll, risk) {
  const highestRoll = Math.max(...diceRoll);
  
  switch(risk) {
    case "Safe":
      if (highestRoll >= 2) return { success: true, priceModifier: 1 + (highestRoll - 2) * 0.05 };
      return { success: false, reason: "Market conditions unfavorable." };
    case "Risky":
      if (highestRoll >= 3) return { success: true, priceModifier: 1 + (highestRoll - 3) * 0.1 };
      return { success: false, reason: "Market too volatile." };
    case "Dangerous":
      if (highestRoll >= 4) return { success: true, priceModifier: 1 + (highestRoll - 4) * 0.2 };
      return { success: false, reason: "Extreme market fluctuations." };
  }
}

// Update market prices based on transactions
function updateMarketPrices(item, outcome) {
  if (outcome.success) {
    marketItems[item].price = Math.floor(marketItems[item].price * outcome.priceModifier);
  } else {
    // Market becomes more volatile after failed transactions
    marketItems[item].price = Math.floor(marketItems[item].price * (1 + (Math.random() - 0.5) * 0.2));
  }
  updateMarket();
}

// Modify existing buyMarketItem and sellMarketItem functions to use the new system
function buyMarketItem(item, priceModifier) {
  const finalPrice = Math.floor(marketItems[item].price * priceModifier);
  if (sim.money >= finalPrice && marketItems[item].quantity > 0) {
    sim.money -= finalPrice;
    marketItems[item].quantity--;
    if (!sim.inventory[item]) {
      sim.inventory[item] = 0;
    }
    sim.inventory[item]++;
    addToDialog(`The Sim bought a ${marketItems[item].name} for $${finalPrice}.`);
    updateMarket();
    updateStats();
  } else {
    addToDialog(`The Sim can't afford ${marketItems[item].name} or it's out of stock.`);
  }
}

function sellMarketItem(item, priceModifier) {
  const finalPrice = Math.floor(marketItems[item].price * priceModifier);
  if (sim.inventory[item] && sim.inventory[item] > 0) {
    sim.money += finalPrice;
    marketItems[item].quantity++;
    sim.inventory[item]--;
    addToDialog(`The Sim sold a ${marketItems[item].name} for $${finalPrice}.`);
    updateMarket();
    updateStats();
  } else {
    addToDialog(`The Sim doesn't have any ${marketItems[item].name} to sell.`);
  }
}

// Update the main simulation loop to include these new systems
function simulateStep() {
  if (sim.currentItem && sim.currentItem.name === 'Work') {
    work();
  } else {
    // ... existing simulation logic ...
  }
  
  // Periodically update market prices
  if (Math.random() < 0.1) { // 10% chance each step
    updateMarketPrices(Object.keys(marketItems)[Math.floor(Math.random() * Object.keys(marketItems).length)], { success: true, priceModifier: 1 + (Math.random() - 0.5) * 0.1 });
  }
  
  drawHouse();
  updateMarket();
}
```

TLDR;

Here's a concise summary of the proposed integration of the Dice Choice System into your automated sim demo:

1. Focus: The dice system is applied primarily to work and market interactions.

2. Work System:
   - Risk level determined by sim's condition
   - Dice rolls decide work success
   - Successful work earns money and produces items for the market
   - Failed work decreases sim's condition

3. Market System:
   - Transactions use dice rolls
   - Risk based on item price volatility
   - Successful transactions may yield better prices
   - Failed transactions increase market volatility

4. Resource Simulation:
   - Work produces items, simulating supply
   - Market transactions simulate demand
   - Prices fluctuate based on supply, demand, and dice roll outcomes

5. Implementation:
   - Add new dice-based functions
   - Modify existing work and market functions
   - Update main simulation loop
