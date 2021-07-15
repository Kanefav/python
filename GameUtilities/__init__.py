class Persona():
    def __init__(self, classe, vida, dano, xp, nivel):
        self.nivel = nivel
        self.classe = classe
        self.vida = vida
        self.dano = dano
        self.xp = xp

    def criar():
        print('Criação de um novo personagem')
        classe = str(input('''Qual classe deseja?
        1 para Cavaleiro
        2 para Mago
        '''))
        if classe == '1':
            return Persona('Cavaleiro', 150, 50, 0, 0)
        if classe == '2':
            return Persona('Mago', 100, 100, 0, 0)

    def levelup(self):
        if self.nivel == 0:
            if self.xp < 2:
                print(f'ainda não possui XP, Seu Xp {self.xp} Necessário: 2')
                return Persona(self.classe, self.vida, self.dano, self.xp, self.nivel)
            if self.xp >= 2 <=5:
                print('Seu nivel aumentou Para 1')
                return Persona(self.classe, self.vida+50, self.dano+50, self.xp, self.nivel+1)
        if self.nivel == 1:
            if self.xp < 6:
                print(f'ainda não possui XP, Seu XP:{self.xp} Necessário: 6')
                return Persona(self.classe, self.vida, self.dano, self.xp, self.nivel)
            if self.xp >= 6 <= 10:
                print('Seu nivel aumentou Para 2')
                return Persona(self.classe, self.vida+100, self.dano+100, self.xp, self.nivel+1)

    def status(self):
        print(f'CLASSE: {self.classe}\nVIDA: {self.vida}\nDANO: {self.dano}\nXP: {self.xp}')
        print(f'Seu nivel atual: {self.nivel}')    

    #def batalhaFacil(self):
    #    rounds = 0
    #    InimigoVidaTemp = InimigoFacil.vida
    #    while True:
    #        rounds += 1
    #        print(f'ROUND {rounds}: Você ataca Inimigo Facil', end=' ')
    #        InimigoVidaTemp = InimigoVidaTemp - self.dano
    #        print(f'VIDA DO INIMIGO:{InimigoVidaTemp}')
    #        if InimigoVidaTemp <= 0:
    #           return Persona(self.classe, self.vida, self.dano, self.xp + 1, self.nivel)
        
    #def batalhaMedia(self):
    #   rounds = 0
    #   InimigoVidaTemp = InimigoMedio.vida
    #    while True:
    #       rounds += 1
    #        print(f'ROUND {rounds}: Você ataca Inimigo Médio', end=' ')
    #       InimigoVidaTemp = InimigoVidaTemp - self.dano
    #        print(f'VIDA DO INIMIGO: {InimigoVidaTemp}')
    #        if InimigoVidaTemp <= 0:
    #            return Persona(self.classe, self.vida, self.dano, self.xp + 2, self.nivel)

    def batalha(persona, inimigo):
        rounds = 0
        InimigoVidaTemp = inimigo.vida
        PersonaVidaTemp = persona.vida
        while True:
            rounds += 1

            #Persona atacando
            InimigoVidaTemp -= persona.dano
            print(f'ROUND{rounds}: Você ataca {inimigo.classe}, Vida restante: {InimigoVidaTemp}')
            #vitoria
            if InimigoVidaTemp <= 0:
                print('Vítoria')
                if inimigo.classe == 'InimigoFacil':
                    return Persona(persona.classe, persona.vida, persona.dano, persona.xp + 1, persona.nivel)
                if inimigo.classe == 'InimigoMedio':
                    return Persona(persona.classe, persona.vida, persona.dano, persona.xp +2, persona.nivel)

            #Inimigo Atacando
            PersonaVidaTemp -= inimigo.dano
            print(f'ROUND{rounds}: {inimigo.classe} te ataca, Vida restante: {PersonaVidaTemp}')
            #derrota
            if PersonaVidaTemp <= 0:
                print('DERROTA!, tente melhorar seus status, começe com batalhas mais fáceis')
                print('A Cada Derrota se perde 2 XP (nao importa o inimigo ainda)')
                return Persona(persona.classe, persona.vida, persona.dano, persona.xp - 2, persona.nivel)


InimigoFacil = Persona('InimigoFacil', 100, 20, 0, 0)
InimigoMedio = Persona('InimigoMedio', 200, 40, 0, 0)


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
                acaobatalha = int(input('''Digite 1 para batalha facil
digite 2 para batalha média:'''))
                if acaobatalha == 1:
                    personagem = Persona.batalha(personagem, InimigoFacil)
                if acaobatalha == 2:
                    personagem = Persona.batalha(personagem, InimigoMedio)
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
