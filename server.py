import socket

url = "0.0.0.0"
port = 2222

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((url, port))
server.listen(5)
print(f'Server is running on {url}:{port}')
client, address = server.accept()
print(f"[*] Connection from {address[0]}:{address[1]}")
data = client.recv(1024).decode()
client.send(f"Hello, Mr. {address[0]}!".encode())
print(f"client: {data}")
server.close()
client.close()