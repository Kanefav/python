from socket import *
import GameUtilities as func
    

if func.VerificarArqExistente('profile') == False:
    func.CriarArquivo('profile')
else:
    host = gethostname()
    port = 22441

    cliente = socket(AF_INET, SOCK_STREAM)
    cliente.connect((host, port))

    while True:
        enviar = str(input('Digite: '))
        cliente.send(enviar.encode())

    #MainPersona = Persona.criar()
    #StartGame(MainPersona)