import socket
import tkinter as tk 

# client socket created 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client.connect(("127.0.0.1", 5000))

# Ask username
username = input("Enter username: ")

# Send username
client.send(username.encode())

# WINDOW
window = tk.Tk()
window.title("DCN Chat App")
window.geometry("450x500")
window.configure(bg="#111b21")


# CHAT AREA
chat_box = tk.Text(
    window,
    bg="#111b21",
    fg="white",
    font=("Arial", 11),
    bd=0,
    wrap="word"
)

chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

chat_box.insert(tk.END, "Welcome to DCN Chat App\n")
chat_box.config(state=tk.DISABLED)


# MESSAGE AREA
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


# SEND MESSAGE
def send_msg():
    msg = entry.get()

    if msg != "":
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, f"\nYou: {msg}")
        chat_box.config(state=tk.DISABLED)

        entry.delete(0, tk.END)


# SEND BUTTON
send_btn = tk.Button(
    entry_frame,
    text="Send",
    bg="#00a884",
    fg="white",
    command=send_msg
)

send_btn.pack(side=tk.RIGHT, padx=10)


window.mainloop()