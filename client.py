import socket
# client socket created 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client.connect(("127.0.0.1", 5000))

# Ask username
username = input("Enter username: ")

# Send username
client.send(username.encode())

print("Connected to server")