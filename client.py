import socket
import threading
import tkinter as tk
from tkinter import simpledialog
import sys

TCP_PORT = 1234
UDP_PORT = 50000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def discover_server():
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    udp.settimeout(5)

    udp.sendto(b"DISCOVER_SERVER", ("255.255.255.255", UDP_PORT))
    data, addr = udp.recvfrom(1024)
    return addr[0]   # 🔥 REAL SERVER IP

def receive():
    while True:
        try:
            msg = client.recv(1024).decode()
            chat.insert(tk.END, msg + "\n")
        except:
            break

def send():
    text = entry.get().strip()
    if text:
        client.send(f"{username}: {text}".encode())
        entry.delete(0, tk.END)

def connect():
    try:
        chat.insert(tk.END, "Searching for server...\n")
        server_ip = discover_server()
        client.connect((server_ip, TCP_PORT))
        chat.insert(tk.END, "Connected to server\n")
        threading.Thread(target=receive, daemon=True).start()
    except:
        chat.insert(tk.END, "Server not found\n")

def on_close():
    try:
        client.close()
    except:
        pass
    root.destroy()
    sys.exit(0)

# ---------- GUI ----------
root = tk.Tk()
root.title("Chat Client")
root.geometry("400x500")
root.protocol("WM_DELETE_WINDOW", on_close)

username = simpledialog.askstring("Username", "Enter your name")
if not username:
    username = "User"

chat = tk.Text(root)
chat.pack(fill=tk.BOTH, expand=True)

entry = tk.Entry(root)
entry.pack(fill=tk.X)

tk.Button(root, text="Send", command=send).pack()

threading.Thread(target=connect, daemon=True).start()

root.mainloop()