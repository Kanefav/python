#servidor 
from socket import *


host = gethostname()
port = 11223

print(f'HOST: {host}, PORT: {port}')

servidor = socket(AF_INET, SOCK_STREAM)
servidor.bind((host, port))
servidor.listen(5)

while True:
    connection, adr = servidor.accept()
    while True:
        msg1 = connection.recv(1024)
        msg1 = msg1.decode()
        if msg1 == '1':
            print('EI! isso é 1 1')
        else:
            print(f'isso aqui {msg1} não é 1 1')