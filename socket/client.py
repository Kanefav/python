#cliente 
from socket import *


host = gethostname()
port = 11223

cliente = socket(AF_INET, SOCK_STREAM)
cliente.connect((host, port))

while True:
    msg = str(input('Digite alguma coisa: '))
    cliente.send(msg.encode())
    msg_receber = cliente.recv(1024)
    print(msg_receber.decode())