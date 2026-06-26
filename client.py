import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = 'localhost'
port = 2222
client.connect((url, port))
client.send("Hello, Server!".encode())
data = client.recv(1024).decode()
print(f"Received from server: {data}")
client.close()