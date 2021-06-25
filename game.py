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
        while True:
            rounds += 1
            print(f'ROUND {rounds}: Você ataca Inimigo Facil', end=' ')
            InimigoFacil.vida = InimigoFacil.vida - MainPersona.dano
            print(f'VIDA DO INIMIGO:{InimigoFacil.vida}')
            if InimigoFacil.vida == 0:
                return Persona(self.vida, self.dano, self.xp + 3)
        

        

MainPersona = Persona.criar()
InimigoFacil = Persona(100, 20, 0)
MainPersona = MainPersona.batalhaFacil()
MainPersona = MainPersona.levelup()
MainPersona.status()
