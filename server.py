import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server.bind(("0.0.0.0", 5000))


server.listen()

print("Server is running...")

while True:
    
    conn, addr = server.accept()

    print(f"Connected with {addr}")

    username = conn.recv(1024).decode()

    print(f"{username} joined the chat")

    conn.close()