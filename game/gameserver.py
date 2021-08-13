from socket import *
import GameUtilities as func


if func.VerificarArqExistente('profile') == False:
    func.CriarArquivo('profile')
else:
    host = gethostname()
    port = 22441

    server = socket(AF_INET, SOCK_STREAM)
    server.bind((host, port))
    server.listen(2)
    print(f'Host:{host}, Porta:{port}')

    while True:
        connection, adr = server.accept()
        print(f'Connect from {adr}')
        receber = connection.recv(2048)
        if receber.decode() == 'start':
            msg = 'Jogo Iniciando'
            connection.sendto(msg.encode(), adr)
        while True:
            criarpersona = 'PKey'
            connection.sendto(criarpersona.encode(), adr)
