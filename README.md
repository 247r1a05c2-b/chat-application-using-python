# chat-application-using-python
# Python GUI Chat Application (Auto Server Discovery)

A multi-user **GUI-based chat application** built using **Python standard libraries only**.  
The application allows multiple clients to chat with each other and the server across **different laptops on the same network**, with **automatic server discovery** (no IP configuration required).

---

## 🚀 Features

- ✅ GUI-based **Server and Client** (Tkinter)
- ✅ **Multi-user chat** support
- ✅ **Two-way messaging**
  - Client ↔ Server
  - Client ↔ Client
- ✅ **Automatic server discovery**
- ✅ Runs on **different laptops** in the same Wi-Fi/LAN
- ✅ Uses **only Python built-in libraries**
- ❌ No `pip install`
- ❌ No external packages
- ❌ No manual IP configuration

---

## 🛠️ Technologies Used

- Python 3
- Tkinter (GUI)
- Socket Programming (TCP & UDP)
- Threading

---

## 📁 Project Structure

ChatApplication/
├── server.py # GUI-based chat server
├── client.py # GUI-based chat client
└── README.md

yaml
Copy code

---

## ⚙️ Requirements

- Python 3.x (already installed)
- All devices must be connected to the **same Wi-Fi / LAN**
- Firewall should allow Python network access (first run)

> ⚠️ No additional libraries or installations are required.

---

## ▶️ How to Run

### 1️⃣ Run Server (on one laptop)
```bash
python server.py
Opens a Server GUI

Starts listening for clients automatically

2️⃣ Run Client (on other laptops)
bash
Copy code
python client.py
Opens a Client GUI

Automatically finds and connects to the server

No IP input required

🧪 Sample Workflow
Start the server

Start multiple clients on different laptops

Enter username

Start chatting instantly

Messages sent by:

Clients are visible to server and all clients

Server messages are visible to all clients

🖼️ Sample Output
Include a screenshot of:

Server window showing client messages

Client window showing chat messages

(Add your screenshot here in GitHub)

🔒 Limitations
Works only within the same local network

UDP discovery does not work over the internet

📌 Project Title (for Resume)
Multi-User GUI Chat Application with Automatic Server Discovery Using Python

📝 Resume Description
Developed a multi-user GUI-based chat application using Python socket programming and Tkinter. The system supports real-time communication across multiple devices on the same network with automatic server discovery, two-way messaging, and no external dependencies.

👤 Author
Shaik Irfan Hussain
GitHub: https://github.com/247r1a05c2-b

