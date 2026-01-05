import socket
import threading
import tkinter as tk
import sys

TCP_PORT = 1234
UDP_PORT = 50000
clients = []

def broadcast(message):
    for c in clients[:]:
        try:
            c.send(message)
        except:
            clients.remove(c)

def handle_client(client, addr):
    while True:
        try:
            msg = client.recv(1024)
            if not msg:
                break
            text = msg.decode()
            log.insert(tk.END, text + "\n")   # show client msg on server
            broadcast(msg)
        except:
            break

    if client in clients:
        clients.remove(client)
    client.close()
    log.insert(tk.END, f"{addr} disconnected\n")

def tcp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", TCP_PORT))
    server.listen()
    log.insert(tk.END, "Server started\n")

    while True:
        client, addr = server.accept()
        clients.append(client)
        log.insert(tk.END, f"Client connected: {addr}\n")
        threading.Thread(
            target=handle_client,
            args=(client, addr),
            daemon=True
        ).start()

def udp_discovery():
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.bind(("", UDP_PORT))

    while True:
        data, addr = udp.recvfrom(1024)
        if data.decode() == "DISCOVER_SERVER":
            udp.sendto(b"SERVER_FOUND", addr)

def send_from_server():
    text = entry.get().strip()
    if text:
        msg = f"Server: {text}"
        broadcast(msg.encode())
        log.insert(tk.END, msg + "\n")
        entry.delete(0, tk.END)

def on_close():
    root.destroy()
    sys.exit(0)

# ---------- GUI ----------
root = tk.Tk()
root.title("Chat Server")
root.geometry("400x500")
root.protocol("WM_DELETE_WINDOW", on_close)

log = tk.Text(root)
log.pack(fill=tk.BOTH, expand=True)

entry = tk.Entry(root)
entry.pack(fill=tk.X)

tk.Button(root, text="Send", command=send_from_server).pack()

threading.Thread(target=tcp_server, daemon=True).start()
threading.Thread(target=udp_discovery, daemon=True).start()

root.mainloop()
