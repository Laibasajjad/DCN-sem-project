import socket
import threading
import tkinter as tk
from tkinter import filedialog

#  CONNECTION 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5000))  

username = input("Enter username: ")
client.send(username.encode())


#  WINDOW 
window = tk.Tk()
window.title("WhatsApp DCN Chat")
window.geometry("450x500")
window.configure(bg="#111b21")


#  CHAT AREA 
chat_frame = tk.Frame(window, bg="#111b21")
chat_frame.pack(fill=tk.BOTH, expand=True)

chat_box = tk.Text(
    chat_frame,
    bg="#111b21",
    fg="white",
    font=("Arial", 11),
    bd=0,
    wrap="word",
    padx=10,
    pady=10
)

chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_box.config(state=tk.DISABLED)

# Chat styles
chat_box.tag_configure("left", justify="left", foreground="#e9edef")
chat_box.tag_configure("right", justify="right", foreground="#00a884")
chat_box.tag_configure("system", justify="center", foreground="gray")


#  MESSAGE INPUT 
entry_frame = tk.Frame(window, bg="#202c33")
entry_frame.pack(fill=tk.X)

entry = tk.Entry(
    entry_frame,
    font=("Arial", 12),
    bg="#2a3942",
    fg="white",
    insertbackground="white",
    relief=tk.FLAT
)
entry.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.X, expand=True)
entry.focus()


#  DISPLAY MESSAGE 
def display(msg, sender=""):
    chat_box.config(state=tk.NORMAL)

    # System message
    if msg.startswith("📢"):
        chat_box.insert(tk.END, f"\n{msg}\n", "system")

    elif sender == username:
        chat_box.insert(tk.END, f"\nYou: {msg}\n", "right")

    else:
        chat_box.insert(tk.END, f"\n{msg}\n", "left")

    chat_box.config(state=tk.DISABLED)
    chat_box.see(tk.END)


# SEND MESSAGE 
def send_msg():
    msg = entry.get().strip()
    if msg == "":
        return

    full_msg = f"{username}: {msg}"
    client.send(full_msg.encode())

    display(msg, username)
    entry.delete(0, tk.END)


# ENTER KEY BIND 
def send_msg_event(event):
    send_msg()

entry.bind("<Return>", send_msg_event)


# SEND FILE 
def send_file():
    file_path = filedialog.askopenfilename()

    if file_path:
        filename = file_path.split("/")[-1]

        with open(file_path, "rb") as f:
            data = f.read()

        payload = b"FILE:" + filename.encode() + b"|" + data
        client.send(payload)

        display(f"📁 Sent file: {filename}", username)


# BUTTONS 
btn_frame = tk.Frame(entry_frame, bg="#202c33")
btn_frame.pack(side=tk.RIGHT)

send_btn = tk.Button(
    btn_frame,
    text="Send",
    bg="#00a884",
    fg="white",
    command=send_msg
)
send_btn.pack(side=tk.LEFT, padx=5)

file_btn = tk.Button(
    btn_frame,
    text="📁",
    bg="#2a3942",
    fg="white",
    command=send_file
)
file_btn.pack(side=tk.LEFT)


# RECEIVE 
def receive():
    while True:
        try:
            msg = client.recv(4096)

            if msg.startswith(b"FILE:"):
                parts = msg[5:].split(b"|", 1)
                filename = parts[0].decode()
                data = parts[1]

                with open("received_" + filename, "wb") as f:
                    f.write(data)

                display(f"📁 File received: {filename}")

            else:
                display(msg.decode())

        except:
            break


threading.Thread(target=receive, daemon=True).start()

window.mainloop()