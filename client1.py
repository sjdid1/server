import socket
import threading

HOST = '127.0.0.1'  
PORT = 65432        

username = input("Enter your username: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    def receive():
        while True:
            try:
                message = s.recv(1024).decode('utf-8')
                if message == 'USERNAME':
                    s.send(username.encode('utf-8'))
                else:
                    print(message)
            except:
                print("An error occurred!")
                s.close()
                break

    def write():
        while True:
            message = f"{username}: {input('')}"
            s.send(message.encode('utf-8'))

    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write_thread = threading.Thread(target=write)
    write_thread.start()