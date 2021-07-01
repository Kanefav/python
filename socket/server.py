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
        msg_enviar = msg1.decode().upper()
        connection.sendto(msg_enviar.encode(), adr)