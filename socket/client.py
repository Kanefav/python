#cliente 
from socket import *


host = gethostname()
port = 11223

cliente = socket(AF_INET, SOCK_STREAM)
cliente.connect((host, port))

while True:
    msg = str(input('Digite 1: '))
    cliente.send(msg.encode())