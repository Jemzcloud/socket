import socket

url = "0.0.0.0"
port = 2223

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((url, port))
server.listen(5)
print(f'Server is running on {url}:{port}')

client_socket, addr = server.accept()
print(f'[*]Connection from {addr[0]}:{addr[1]}')
client_socket.send(bytes("Welcome to the server!", "utf-8"))
while True:
    data = client_socket.recv(1024).strip()
    print(f'[>] Client: {data.decode("utf-8")}')
    if data == b'quit':
        print(f'Connection from {addr[0]}:{addr[1]} has been closed!')
        client_socket.close()
        break
    msg = input("server: ")
    client_socket.send(bytes(msg, "utf-8"))
    if msg == 'quit':
        print("Connection closed by server!")
        client_socket.close()
        break



