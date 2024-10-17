import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('localhost', 12345))

server_socket.listen(1)
print("Servern lyssnar på 12345")

client_socket, addr = server_socket.accept()

data = client_socket.recv(1024).decode()
print(f"Meddelande från klienten: {data}")

client_socket.send("Tack för ditt meddelande".encode())

client_socket.close()
server_socket.close()