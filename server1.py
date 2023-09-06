import socket
import threading

HOST = '127.0.0.1'  
PORT = 65432        

clients = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server is running on {HOST}:{PORT}")
    while True:
        client, address = s.accept()
        clients.append(client)
        print(f"Connected with {str(address)}")
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()