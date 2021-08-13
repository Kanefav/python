from socket import *
import GameUtilities as func
    

host = gethostname()
port = 22441

ask = str(input('Iniciar Jogo? [S/N]')).upper()
if ask in 'SIM':
    cliente = socket(AF_INET, SOCK_STREAM)
    cliente.connect((host, port))
    while True:
        cliente.send('start'.encode())
        receber = cliente.recv(2048)
        print(f'{receber.decode()}')
        #Abandonado