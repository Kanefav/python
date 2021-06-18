class Carro:
    def __init__(self, nome, potencia, velocidade_maxima):
        self.nome = nome
        self.potencia = potencia 
        self.velocidade_maxima = velocidade_maxima
    def ligar(self):
        print(f'{self.nome} está ligado')
    
    def desligar(self):
        print(f'{self.nome} está desligado')
    
    def acelerar(self):
        while True:
            aceleracao = int(input(f'Em que velocidade quer acelerar? <Limite de {self.potencia}km>'))
            if aceleracao > self.potencia:
                print(f'Este valor supera o limite de potencia do {self.nome} que é igual a {self.potencia}')
            else:
                print('acelerando')
                for velocidade in range(0, self.velocidade_maxima + 1, aceleracao):
                    print(f'{velocidade}..', end='')
                break
    
    def info_carro(self):
        print(self.nome, self.potencia, self.velocidade_maxima)

print('Comprando um carro')
nome = str(input('Dê um nome ao seu novo carro: '))
potencia = int(input('escolha uma potencia em seu carro: <10 a 200(exemplo)>: '))
Velocidade_maxima = int(input('Digite uma velocidade maxima para seu carro: '))
carro1 = Carro(nome, potencia, Velocidade_maxima)
#carro1.info_carro()
pergunta_ligar = str(input('O carro está pronto, quer liga-lo? <Sim ou não> ')).lower()
if pergunta_ligar in 'ssim':
    carro1.ligar()
    pergunta_acelerar = str(input('Quer acelerar? <Sim ou não> ')).lower()
    if pergunta_acelerar in 'ssim':
        carro1.acelerar()
    else:
        carro1.desligar()
else:
    print('Ok, até outra hora')