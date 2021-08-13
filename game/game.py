from socket import *
import GameUtilities as func

host = gethostname()
port = 22441

default = 2048
ask = str(input('Iniciar Jogo? [S/N]')).upper()
if ask in 'SIM':
    cliente = socket(AF_INET, SOCK_STREAM)
    cliente.connect((host, port))
    cliente.send('start'.encode())
    receber = cliente.recv(default)
    print(f'{receber.decode()}')
    while True:
        persona = cliente.recv(default)
        if persona.decode() == 'PKey':
            Personagem = func.Persona.criar() 
            func.StartGame(Personagem)
        break