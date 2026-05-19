import socket
import threading


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server.bind(("0.0.0.0", 5000))


server.listen()

print("Server is running...")

clients = {}

# BROADCAST MESSAGE
def broadcast(message):
    for client in list(clients.values()):
        try:
            client.send(message)
        except:
            pass

def handle(conn):
    username = conn.recv(1024).decode()
    clients[username] = conn

    broadcast(f"{username} joined the chat".encode())

    while True:
        try:
            msg = conn.recv(1024).decode()

            if msg.startswith("@"):
                parts = msg[1:].split(" ", 1)

                if len(parts) == 2:
                    target, text = parts

                    if target in clients:
                        clients[target].send(f"[DM] {username}: {text}".encode())

            else:
                broadcast(f"{username}: {msg}".encode())

        except:
            break

    del clients[username]
    conn.close()


# ACCEPT CLIENTS
while True:
    conn, addr = server.accept()

    threading.Thread(target=handle, args=(conn,)).start()