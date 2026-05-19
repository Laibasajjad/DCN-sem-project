import socket
import threading


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server.bind(("0.0.0.0", 5000))


server.listen()

print("Server is running...")

clients = {}

# BROADCAST MESSAGE
def broadcast(message):
    for client in clients.values():
        client.send(message)



# HANDLE CLIENT
def handle(conn):
    username = conn.recv(1024).decode()

    clients[username] = conn

    print(f"{username} joined")

    broadcast(f"{username} joined the chat".encode())

    while True:
        try:
            msg = conn.recv(1024)

            broadcast(msg)

        except:
            break

    del clients[username]
    conn.close()


# ACCEPT CLIENTS
while True:
    conn, addr = server.accept()

    threading.Thread(target=handle, args=(conn,)).start()