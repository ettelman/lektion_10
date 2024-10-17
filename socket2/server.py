import socket
import threading

def handle_client(client_socket, addr):
    print(f"Ansluten till {addr}")
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                print(f"Klient {addr} kopplade ner.")
                break
            print(f"Meddelande från {addr}: {data}")
            client_socket.send("Meddelande mottaget av server".encode())
        except ConnectionRefusedError:
            print("Anslutning avslutades oväntat")
            break
    
    client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)
print("Servern lyssnar på 12345")

while True:
    client_socket, addr = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    client_thread.start()