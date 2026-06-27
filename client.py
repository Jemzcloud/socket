import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = 'localhost'
port = 2223
client.connect((url, port))

while True:
    data = client.recv(1024).strip()
    print(f'[>] server: {data.decode("utf-8")}')
    if data == b'quit':
        print("Connection closed by server!")
        client.close()
        break
    msg = input("client: ")
    client.send(bytes(msg, "utf-8"))
    if msg == 'quit':
        print("Connection closed by client!")
        client.close()
        break
    


        
