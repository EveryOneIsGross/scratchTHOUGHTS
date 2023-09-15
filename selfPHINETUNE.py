'''

chat with phi, 'exit' generates a phinetuning corpus from chat history for future self tuning.

shame phi doesn't support beam search
'''
import torch
import torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer, AdamW, get_linear_schedule_with_warmup
import math
import os

# Setup and initialize the model and tokenizer
torch.set_default_device('cpu')
model = AutoModelForCausalLM.from_pretrained("microsoft/phi-1_5", trust_remote_code=True, torch_dtype="auto")
tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-1_5", trust_remote_code=True, torch_dtype="auto")
model = model.to('cpu').float()

def generate_completion(prompt):
    inputs = tokenizer(prompt, return_tensors="pt", return_attention_mask=False).to('cpu')
    outputs = model.generate(**inputs, max_length=200)
    text = tokenizer.batch_decode(outputs)[0]
    return text

class CascadingModel:
    def __init__(self, model_name="microsoft/phi-1_5"):
        # Setup and initialize the model and tokenizer
        torch.set_default_device('cpu')
        self.model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True, torch_dtype="auto").to('cpu').float()
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True, torch_dtype="auto")
        self.checkpoint_dir = './checkpoints/'
        if not os.path.exists(self.checkpoint_dir):
            os.makedirs(self.checkpoint_dir)
        
        # Initialize anchor model
        self.anchor_model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True, torch_dtype="auto").to('cpu').float()

    def generate_completion(self, prompt):
        if not prompt.strip():  # Check if prompt is empty or whitespace
            return "Invalid input"
        inputs = self.tokenizer(prompt, return_tensors="pt", return_attention_mask=False).to('cpu')
        outputs = self.model.generate(**inputs, max_length=200)
        text = self.tokenizer.batch_decode(outputs)[0]
        return text

    def fine_tune(self, train_data, epochs=1, learning_rate=5e-5, weight_decay=0.01, anchor_lambda=0.1):
        optimizer = AdamW(self.model.parameters(), lr=learning_rate, weight_decay=weight_decay)
        scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=0, num_training_steps=len(train_data) * epochs)
        
        for epoch in range(epochs):
            for prompt, target in train_data:
                # Convert input and target to tensor
                input_tensor = self.tokenizer(prompt, return_tensors="pt", return_attention_mask=False).to('cpu')
                target_tensor = self.tokenizer(target, return_tensors="pt", return_attention_mask=False).to('cpu')
                
                # Model prediction
                outputs = self.model(**input_tensor, labels=target_tensor)
                loss, logits = outputs.loss, outputs.logits
                
                # Regularization with anchor model
                with torch.no_grad():
                    anchor_outputs = self.anchor_model(**input_tensor)
                anchor_logits = anchor_outputs.logits
                regularization_loss = F.mse_loss(logits, anchor_logits.detach())
                
                # Combine the losses
                combined_loss = loss + anchor_lambda * regularization_loss
                
                combined_loss.backward()
                optimizer.step()
                scheduler.step()
                optimizer.zero_grad()

            # Save checkpoint after each epoch
            torch.save(self.model.state_dict(), os.path.join(self.checkpoint_dir, f'epoch_{epoch}.pt'))

    def load_checkpoint(self, epoch):
        self.model.load_state_dict(torch.load(os.path.join(self.checkpoint_dir, f'epoch_{epoch}.pt')))
        self.model.eval()

def chat_with_agent():
    chat_history = []
    print("Hello! You can input a piece of incomplete code or any other prompt, and I'll try to complete it for you.")
    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.lower() in ['quit', 'exit']:
                print("Goodbye!")
                break
            completion = generate_completion(user_input)
            chat_history.append((user_input, completion))
            print(f"\nAgent: {completion}")
        except Exception as e:
            print(f"Error: {e}")

    # Generate fine-tuning corpus
    with open("finetuning_corpus.txt", "w") as f:
        for input_seq, target_seq in chat_history:
            f.write(f"Input: {input_seq}\nTarget: {target_seq}\n\n")

def generate_with_oscillating_temp(prompt, n, oscillation_frequency=1, top_k=50, top_p=0.95, num_beams=1):
    if not prompt.strip():  # Check if prompt is empty or whitespace
        return ["Invalid input"] * n
    completions = []
    for i in range(n):
        temperature = 0.5 + 0.5 * math.sin(i * oscillation_frequency)
        inputs = tokenizer(prompt, return_tensors="pt", return_attention_mask=False)
        outputs = model.generate(**inputs, max_length=200, temperature=temperature, 
                                 top_k=top_k, top_p=top_p, num_beams=num_beams, early_stopping=True, do_sample=True)
        text = tokenizer.batch_decode(outputs)[0]
        completions.append(text)
    return completions


def expand_corpus(file_name="finetuning_corpus.txt", n=5):
    expanded_corpus = []
    with open(file_name, "r") as f:
        lines = f.readlines()
        for i in range(0, len(lines), 3):
            input_seq = lines[i].strip().replace("Input: ", "")
            print(f"Expanding: {input_seq}")
            if not input_seq:  # Checking if the input_seq is empty
                continue
            completions = generate_with_oscillating_temp(input_seq, n)
            for completion in completions:
                expanded_corpus.append((input_seq, completion))

    
    # Save the expanded corpus
    with open("expanded_finetuning_corpus.txt", "w") as f:
        for input_seq, completion in expanded_corpus:
            f.write(f"Input: {input_seq}\nTarget: {completion}\n\n")




# Usage
chat_history = []
cascading_model = CascadingModel()
# Chat with the model, accumulate data in chat_history
# Start the chat
chat_with_agent()

# Expand the corpus after chat concludes
expand_corpus()

# Fine-tuning
cascading_model.fine_tune(chat_history)

