import socket
import threading
import pickle
import queue
from sklearn.neighbors import NearestNeighbors
from gpt4all import GPT4All, Embed4All
from sklearn.metrics.pairwise import cosine_similarity
import os
import datetime

# Embedding functions and utilities
embedder = Embed4All()

# Loading the GPT4All model
model = GPT4All('C://AI_MODELS//orca-mini-3b.ggmlv3.q4_0.bin')
system_template = 'You are a helpful AI, summarise and reword the following:'
prompt_template = 'USER: {0}\nASSISTANT: '

def generate_response(user_message, context_message=None):
    """Generate a response using the model."""
    if context_message:
        prompt = system_template + prompt_template.format(user_message) + f"\nCONTEXT: {context_message}\n"
    else:
        prompt = system_template + prompt_template.format(user_message)
    response = model.generate(prompt, temp=0)
    return response

def save_to_pickle(username, embedding_memory, message_memory):
    data = {
        'embedding_memory': embedding_memory,
        'message_memory': message_memory
    }
    with open(f'{username}_memory.pkl', 'wb') as f:
        pickle.dump(data, f)

def load_from_pickle(username):
    if os.path.exists(f'{username}_memory.pkl'):
        with open(f'{username}_memory.pkl', 'rb') as f:
            data = pickle.load(f)
            return data['embedding_memory'], data['message_memory']
    return [], []

# P2P Chat Application
class P2PChat:
    def __init__(self, process_input, process_output, mode, username):
        self.process_input = process_input
        self.process_output = process_output
        self.mode = mode
        self.embedding_memory = []  # Store embeddings
        self.message_memory = []  # Store actual messages
        self.username = username
        self.embedding_memory, self.message_memory = load_from_pickle(username)
        self.send_queue = queue.Queue()
        self.receive_queue = queue.Queue()
        self.message_received_event = threading.Event()
        self.initial_message_sent = False


    def _initialize_socket(self, host='localhost', port=12345):
        """Initialize socket based on mode (server/client)"""
        if self.mode == 'server':
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind((host, port))
            server_socket.listen(1)
            print("Server is waiting for a connection...")
            self.sock, _ = server_socket.accept()
            print("Connected to a client!")
            # Receive client's name
            client_name = self.sock.recv(1024).decode('utf-8')
            # Send server's name
            self.sock.sendall(self.username.encode('utf-8'))
            # Set other user's name as client's name
            self.other_username = client_name
        else:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((host, port))
            print("Connected to the server!")
            # Send client's name
            self.sock.sendall(self.username.encode('utf-8'))
            # Receive server's name
            server_name = self.sock.recv(1024).decode('utf-8')
            # Set other user's name as server's name
            self.other_username = server_name

    def retrieve_context(self, embedding):
        """Retrieve the most similar past message based on the embedding."""
        if not self.embedding_memory:
            return None
        similarities = cosine_similarity([embedding], self.embedding_memory)
        most_similar_index = similarities[0].argmax()
        most_similar_message = self.message_memory[most_similar_index]
        print("Most similar message:", most_similar_message)
        return most_similar_message

    def process_send_queue(self):
        """Process and send messages from the send queue."""
        while True:
            message = self.send_queue.get()
            if message == "EXIT":
                break
            ai_elaboration = self.process_input(message)
            print(f"\n{self.username}'s AI:", ai_elaboration)
            elaboration_embedding = embedder.embed(ai_elaboration)
            context_message = self.retrieve_context(elaboration_embedding)
            self.embedding_memory.append(elaboration_embedding)
            self.message_memory.append(ai_elaboration)
            combined_data = pickle.dumps({"message": message, "embedding": elaboration_embedding, "context": context_message})
            message_header = bytes(f"{len(combined_data):<{10}}", 'utf-8')
            self.sock.sendall(message_header + combined_data)
            save_to_pickle(self.username, self.embedding_memory, self.message_memory)

    def process_receive_queue(self):
        """Process and display messages from the receive queue."""
        while True:
            received_data = self.receive_queue.get()
            if received_data == "EXIT":
                break
            received_message = received_data["message"]
            received_embedding = received_data["embedding"]
            received_context = received_data["context"]
            self.embedding_memory.append(received_embedding)
            self.message_memory.append(received_context)
            print("\nContextual Insight:", f"{self.other_username}'s AI elaborated: '{received_context}'")
            response = self.process_output(received_message, received_context)
            print(f"\n{self.other_username}:", received_message)
            print(f"{self.username}'s AI:", response)
            self.message_received_event.set()
            save_to_pickle(self.username, self.embedding_memory, self.message_memory)
            input(f"\n{self.username}: ")  # Prompt the user to input their next message

    def send_message(self):
        """Send message to peer."""
        while True:
            # 1. User types a message
            message = input("You: ")

            # 2. Get an elaboration or definition from the local AI
            ai_elaboration = self.process_input(message)
            print("Local AI Elaboration:", ai_elaboration)

            # 3. Embed the AI elaboration and retrieve context from previous AI responses
            elaboration_embedding = embedder.embed(ai_elaboration)
            context_message = self.retrieve_context(elaboration_embedding)
            
            # Store the AI elaboration embedding and the elaboration itself
            self.embedding_memory.append(elaboration_embedding)
            self.message_memory.append(ai_elaboration)

            # 4. Send the original message and the context to Chat B
            timestamp = datetime.datetime.now().isoformat()  # Generate a timestamp for the message
            combined_data = pickle.dumps({"message": message, "embedding": elaboration_embedding, "context": context_message, "timestamp": timestamp})
            message_header = bytes(f"{len(combined_data):<{10}}", 'utf-8')
            self.sock.sendall(message_header + combined_data)
            # At the end of send_message:
            save_to_pickle(self.username, self.embedding_memory, self.message_memory)


    def receive_message(self):
        """Receive messages and add them to the receive queue."""
        while True:
            data_length_msg = self.sock.recv(10)
            if not data_length_msg:
                break
            data_length = int(data_length_msg.strip())
            full_data = b""
            while len(full_data) < data_length:
                chunk = self.sock.recv(data_length - len(full_data))
                if not chunk:
                    raise ConnectionError("Connection was lost while receiving data")
                full_data += chunk
                received_data = pickle.loads(full_data)
                received_message = received_data["message"]
                received_embedding = received_data["embedding"]
                received_context = received_data["context"]
                received_timestamp = received_data["timestamp"]
            self.receive_queue.put(received_data)

    def start(self):
        """Start the chat based on mode (server/client)."""
        self._initialize_socket()
        threading.Thread(target=self.process_send_queue).start()
        threading.Thread(target=self.process_receive_queue).start()
        if self.mode == 'server':
            threading.Thread(target=self.send_message).start()
            self.receive_message()
        else:
            threading.Thread(target=self.receive_message).start()
            self.send_message()

# Main function to run the chat application
def main():
    def process_input(message, context_message=None):
        return generate_response(message, context_message)

    def process_output(message, context_message=None):
        return generate_response(message, context_message)

    name = input("Enter your name: ")
    mode = input("Enter 'server' to host or 'client' to connect: ").lower()
    if mode not in ['server', 'client']:
        print("Invalid choice. Please enter 'server' or 'client'.")
        return
    chat_agent = P2PChat(process_input, process_output, mode, name)
    chat_agent.start()

if __name__ == "__main__":
    main()
