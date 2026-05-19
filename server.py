import socket
import threading
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(("0.0.0.0", 5000))
server.listen()

print("🚀 Server running...")

clients = {}
usernames = {}


def broadcast(msg, sender=None):
    for user, conn in clients.items():
        if user != sender:
            try:
                conn.send(msg)
            except:
                pass


def handle(conn):
    username = conn.recv(1024).decode()
    clients[username] = conn
    usernames[conn] = username

    print(f"{username} joined")
    broadcast(f"📢 {username} joined".encode())

    while True:
        try:
            data = conn.recv(4096)

            if data.startswith(b"FILE:"):
                filename, filedata = data[5:].split(b"|", 1)

                print(f"📁 File from {username}: {filename.decode()}")

                # broadcast file to others
                for user, c in clients.items():
                    if user != username:
                        c.send(data)

            else:
                msg = data.decode()

                # private message
                if msg.startswith("@"):
                    target, text = msg[1:].split(" ", 1)
                    if target in clients:
                        clients[target].send(f"[DM] {username}: {text}".encode())
                else:
                    broadcast(f"{username}: {msg}".encode(), username)

        except:
            break

    print(f"{username} left")
    del clients[username]
    conn.close()


while True:
    conn, addr = server.accept()
    threading.Thread(target=handle, args=(conn,)).start()