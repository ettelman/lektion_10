import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

while True:
    message = input("Skriv meddelande: ")
    client_socket.send(message.encode())
    response = client_socket.recv(1024).decode()
    print(f"Svar: {response}")

    if message.lower() == "exit":
        break


client_socket.close()