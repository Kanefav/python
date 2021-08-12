from socket import *

host = gethostname()
port = 22441

server = socket(AF_INET, SOCK_STREAM)
server.bind((host, port))
server.listen(2)
print(f'Host:{host}, Porta:{port}')

while True:
    connection, adr = server.accept()
    print('Connectado')
    while True:
        recebido = connection.recv(2048)
        print(recebido.decode())