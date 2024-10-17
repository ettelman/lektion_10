import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('localhost', 12345))

client_socket.send("Hej från clienten".encode())

response = client_socket.recv(1024).decode()
print(f"Svar fråns servern: {response}")

client_socket.close()