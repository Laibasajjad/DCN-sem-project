# DCN Chat Application (TCP Socket Based Multi-Client System)

## Project Overview

This is a real-time multi-client chat application built using Python socket programming and Tkinter GUI. The system allows multiple users to communicate over a network using TCP connections. It supports public messaging, private messaging, and file transfer between clients.

The project demonstrates core concepts of Data Communication and Networking (DCN), including client-server architecture, socket programming, threading, and basic protocol design for message handling.

---

## Features

### 1. Real-Time Messaging

* Multiple clients can connect to a central server
* Messages are broadcasted instantly to all connected users

### 2. Private Messaging

* Users can send direct messages using:
  @username message

### 3. File Sharing

* Users can send files through the chat interface
* Files are received and saved locally on the client side

### 4. Graphical User Interface

* Built using Tkinter
* Simple chat interface with input box and message display area

### 5. Multi-Client Support

* Server handles multiple clients using threading
* Each client runs independently

---

## Technologies Used

* Python 3
* Socket Programming (TCP)
* Threading
* Tkinter (GUI)

---

## Project Structure

DCN/
│── server.py      # Handles client connections, messaging, and file transfer
│── client.py      # GUI-based chat client

---

## How to Run the Project

### 1. Start the Server

Run the server first:

python server.py

Server will start on:
0.0.0.0:5000

---

### 2. Start Clients

Run client on multiple terminals or systems:

python client.py

Enter a username when prompted.

---

### 3. Start Chatting

* Type message and press Enter or Send button
* Use @username message for private chat
* Use file button to send files

---

## Communication Flow

1. Client connects to server using TCP socket
2. Server stores client connection with username
3. Messages are received by server
4. Server broadcasts messages to other clients
5. Files are transferred in binary format and forwarded by server

---

## Concepts Demonstrated

* Client-Server Architecture
* TCP Socket Programming
* Multithreading in Server
* Real-time Data Communication
* GUI-based Network Application
* Basic Protocol Design (custom message format)

---

## Limitations

* No encryption or security layer
* No database storage for chat history
* No message persistence
* Basic error handling

---

## Future Improvements

* Add authentication system (login/signup)
* Store chat history in database
* Add encryption (secure messaging)
* Improve UI with modern chat design
* Add group chat rooms
* Add online/offline status indicators





