import datetime
import asyncio
import textwrap
import threading
from gpt4all import GPT4All
from collections import deque

# Initialize the GPT4All model
model = GPT4All("orca-mini-3b.ggmlv3.q4_0.bin")
terminate_event = asyncio.Event()

def get_timestamp():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def wait_for_termination():
    """Waits for the 'terminate' command and sets the terminate_event."""
    while True:
        command = input("Enter 'terminate' to shut down the server.\n")
        if command == "terminate":
            terminate_event.set()
            break

async def notify_and_close_clients():
    """Sends a termination message to all clients and closes their connections."""
    termination_message = "The server is shutting down. Thank you for chatting!"
    for room in rooms.values():
        for client in room.members:
            await client.send_message(termination_message)
            client.writer.close()

class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.members = set()
        self.message_buffer = deque(maxlen=1000)  # Set max buffer size to 1000 messages
        self.history = []  # Store the chat history
        asyncio.create_task(self.process_messages()) # Start the message processing task

    async def process_messages(self):
        while True:
            if self.message_buffer:
                sender, message = self.message_buffer.popleft()
                await self.broadcast(sender, message)
            await asyncio.sleep(0.05)  # Process every 50ms to avoid CPU hogging

    async def broadcast(self, sender, message):
        timestamp = get_timestamp()
        formatted_message = f"[{timestamp}] [{self.name}] {sender.name}: {message}\n"
        self.history.append(formatted_message)  # Save the message to history
        for member in self.members:
            if member != sender or sender.name == "Chatbot":
                await member.send_message(formatted_message)
        # If the sender is a user (not the chatbot), get a response from the chatbot
        if sender.name != "Chatbot":
            with model.chat_session():
                chatbot_response = model.generate(prompt=message, temp=0.7, max_tokens=200)
                await self.broadcast(Chatbot, chatbot_response)


    def join(self, client):
        self.members.add(client)
        asyncio.create_task(self.broadcast(client, f"{client.name} has joined the room."))

    def leave(self, client):
        self.members.remove(client)
        asyncio.create_task(self.broadcast(client, f"{client.name} has left the room."))


class IRCClient:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer
        self.name = None
        self.room = None

    async def send_wrapped_message(self, message):
        # This function wraps the message and sends it to the user
        wrapped_message = "\r\n".join(textwrap.wrap(message, width=70))
        self.writer.write(f"{wrapped_message}\r\n".encode())
        await self.writer.drain()

    async def send_user_message(self, message):
        await self.send_wrapped_message(message)

    async def send_message(self, message):
        await self.send_wrapped_message(message)


    async def handle_input(self, data):
        command, *args = data.strip().split()

        if command == "/nick":
            self.name = args[0]
            await self.send_message(f"Nickname set to {self.name}")

        elif command == "/me":
            action_message = f"{self.name} {' '.join(args)}"
            if self.room:
                await self.send_user_message(action_message)  # Send action confirmation to the user
                await self.room.broadcast(self, action_message)


        # Echo back the user's input
        await self.send_user_message(f"You: {data}")

        if command == "/join":
            room_name = args[0]
            if self.room:
                self.room.leave(self)
            self.room = rooms.get(room_name)
            if not self.room:
                self.room = ChatRoom(room_name)
                rooms[room_name] = self.room
            self.room.join(self)

        elif command == "/leave":
            if self.room:
                self.room.leave(self)
                self.room = None

        else:
            if self.room:
                await self.room.broadcast(self, data)

        # Send the Input: prompt only after handling the user's message
        # await self.send_message("Input:")


    async def handle_client(self):
        try:
            while True:
                data = await self.reader.readline()
                if not data:
                    break
                await self.handle_input(data.decode().strip())
        except asyncio.CancelledError:
            pass
        finally:
            if self.room:
                self.room.leave(self)
            self.writer.close()
            await self.writer.wait_closed()


async def handle_connection(reader, writer):
    client = IRCClient(reader, writer)
    await client.send_message("Welcome to the simple IRC server!")
    await client.send_message("Set your nickname with /nick <name>")
    await client.handle_client()

rooms = {}

async def main():
    # Start the termination listener on a secondary thread
    threading.Thread(target=wait_for_termination, daemon=True).start()
    
    server = await asyncio.start_server(handle_connection, '127.0.0.1', 6667)
    # Dynamically fetch the host and port details from the server
    host, port = server.sockets[0].getsockname()
    print(f"Server is open on {host}:{port}")
    
    try:
        while not terminate_event.is_set():
            await asyncio.sleep(1)  # Check every second

        print("Termination command received. Shutting down server...")
        
        # Notify clients and close their connections
        await notify_and_close_clients()

        # Close the server
        server.close()
        await server.wait_closed()
    finally:
        # Save chatroom histories to .txt files
        for room_name, room in rooms.items():
            with open(f"{room_name}.txt", "w") as f:
                f.writelines(room.history)

# Create a Chatbot client instance
Chatbot = IRCClient(None, None)
Chatbot.name = "Chatbot"

if __name__ == "__main__":
    asyncio.run(main())
