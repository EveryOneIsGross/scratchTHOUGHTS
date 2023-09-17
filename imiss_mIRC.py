import datetime
import time
import asyncio
import textwrap
import string
import threading
from gpt4all import GPT4All
from collections import deque
import upnpclient
import logging

logging.basicConfig(level=logging.INFO, filename='server_log.txt', format='%(asctime)s - %(levelname)s - %(message)s')

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

def sanitize_filename(filename):
    """Remove invalid characters from a filename."""
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    return ''.join(c for c in filename if c in valid_chars)


class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.members = set()
        self.message_buffer = deque(maxlen=1000)  # Set max buffer size to 1000 messages
        self.history = []  # Store the chat history
        asyncio.create_task(self.process_messages()) # Start the message processing task
    
    def extract_raw_conversation(self, last_n=10):
        # Extract the last n messages from the chat history
        recent_history = self.history[-last_n:]
        raw_conversation = ""
        for message in recent_history:
            # Extract the actual message content, ignoring timestamps and other formatting
            message_content = message.split("]")[-1].strip()
            raw_conversation += message_content + "\n"
        return raw_conversation
    
    async def process_messages(self):
        while True:
            if self.message_buffer:
                sender, message = self.message_buffer.popleft()
                await self.broadcast(sender, message)
            await asyncio.sleep(0.05)  # Process every 50ms to avoid CPU hogging

    async def broadcast(self, sender, message):
        timestamp = get_timestamp()
        formatted_message = None
        
        # Check if the message is an action ("/me") and strip the prefix if present
        if message.startswith("/me"):
            action_message = message[4:]
            formatted_message = f"[{timestamp}] [{self.name}] {sender.name} {action_message}\n"
        else:
            formatted_message = f"[{timestamp}] [{self.name}] {sender.name}: {message}\n"

        self.history.append(formatted_message)  # Save the message to history

        for member in self.members:
            if member != sender or sender.name == "Chatbot":
                await member.send_message(formatted_message)
        
        # If the sender is the chatbot, don't ask for another response
        if sender.name == "Chatbot":
            return

        # If the sender is a user, get a response from the chatbot
        context = self.extract_raw_conversation()
        context += f"{sender.name}: {message}"
        with model.chat_session():
            chatbot_response = model.generate(prompt=context, temp=0.7, max_tokens=200)
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
            if not args or not args[0].strip():
                # If no name is provided or if the provided name is just whitespace
                self.name = f"user_{int(time.time())}"  # Using UNIX timestamp for uniqueness
                await self.send_message(f"No name provided. Defaulting nickname to {self.name}.")
            else:
                self.name = args[0]
                await self.send_message(f"Nickname set to {self.name}")
                
        elif command == "/me":
            action_message = f"{self.name} {' '.join(args)}"
            action_message = action_message.replace("/me", "", 1).strip()
            if self.room:
                #await self.room.broadcast(self, action_message)
                await self.send_user_message(action_message)  # Send action to chatbot


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

def setup_port_forwarding(port):
    devices = upnpclient.discover()
    valid_devices = []

    if not devices:
        logging.warning("No UPnP devices found on the network.")
        return False

    for device in devices:
        try:
            if device.WANIPConn1:
                valid_devices.append(device)
        except Exception as e:
            logging.error(f"Error with device {device.location}: {e}")

    if not valid_devices:
        logging.warning("No suitable UPnP devices found for port forwarding.")
        return False

    device = valid_devices[0]
    try:
        device.WANIPConn1.AddPortMapping(
            NewRemoteHost="",
            NewExternalPort=port,
            NewProtocol="TCP",
            NewInternalPort=port,
            NewInternalClient=device.host,
            NewEnabled=1,
            NewPortMappingDescription="IRC Server",
            NewLeaseDuration=0
        )
        logging.info(f"Port {port} has been forwarded.")
        return True
    except Exception as e:
        logging.error(f"Failed to set up port forwarding: {e}")
        return False



async def main():
    mode = input("Should the server be public or private? (public/private): ").strip().lower()
    if mode == "public":
        if not setup_port_forwarding(6667):
            print("Failed to setup automatic port forwarding. Falling back to local mode.")
            mode = "private"  # Fallback to private mode

    # Start the termination listener on a secondary thread
    threading.Thread(target=wait_for_termination, daemon=True).start()
    
    #...
    server = await asyncio.start_server(handle_connection, '127.0.0.1', 6667)
    #...
    
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
        current_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')  # Get the current time in a compact format
        # Save chatroom histories to .txt files when the server exits
        for room_name, room in rooms.items():
            sanitized_room_name = sanitize_filename(room_name)
            with open(f"{sanitized_room_name}_{current_time}.txt", "w") as f:
                    f.writelines(room.history)


# Create a Chatbot client instance
Chatbot = IRCClient(None, None)
Chatbot.name = "Chatbot"

if __name__ == "__main__":
    asyncio.run(main())
