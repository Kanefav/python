class Persona():
    def __init__(self, vida, dano, xp):
        self.vida = vida
        self.dano = dano
        self.xp = xp

    def criar():
        print('Criação de um novo personagem')
        classe = str(input('''Qual classe deseja?
        1 para Cavaleiro
        2 - em breve
        '''))
        if classe == '1':
            return Persona(200, 50, 0)

    def levelup(self):
        if self.xp < 2:
            print(f'ainda não possui XP, você tem {self.xp} de xp')
            return Persona(self.vida, self.dano, self.xp)
        if self.xp >= 2 <=5:
            print('Seu nivel aumentou')
            return Persona(250, 100, self.xp)

    def status(self):
        print(f'VIDA: {self.vida}\nDANO: {self.dano}\nXP: {self.xp}')
    
    def batalhaFacil(self):
        rounds = 0
        InimigoVidaTemp = InimigoFacil.vida
        while True:
            rounds += 1
            print(f'ROUND {rounds}: Você ataca Inimigo Facil', end=' ')
            InimigoVidaTemp = InimigoVidaTemp - self.dano
            print(f'VIDA DO INIMIGO:{InimigoVidaTemp}')
            if InimigoVidaTemp == 0:
                return Persona(self.vida, self.dano, self.xp + 3)


InimigoFacil = Persona(100, 20, 0)


def StartGame(personagem):
    while True:
        try:
            print('''Digite 1 para Batalhar
Digite 2 para Tentar dar Level Up
Digite 3 para Olhar seus Status
Digite 4 para Sair
''', end='')
            acao = int(input(':'))
            if acao == 1:
                personagem = Persona.batalhaFacil(personagem)
            if acao == 2:
                personagem = Persona.levelup(personagem)
            if acao == 3:
                Persona.status(personagem)
            if acao == 4:
                break
        except ValueError:
            print('Digite apenas algum número das opçoes')
        except Exception as erro:
            print(f'Algum erro desconhecido, relatório: {erro}')
