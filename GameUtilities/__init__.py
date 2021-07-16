class Persona():
    def __init__(self, classe, vida, dano, xp, nivel, akuma, wallet):
        self.nivel = nivel
        self.classe = classe
        self.vida = vida
        self.dano = dano
        self.xp = xp
        self.akuma = akuma
        self.wallet = wallet

    def criar():
        print('Criação de um novo personagem')
        classe = str(input('''Qual classe deseja?
        1 para Cavaleiro
        2 para Mago
        '''))
        if classe == '1':
            return Persona('Cavaleiro', 150, 50, 0, 0, 'Sem', 0)
        if classe == '2':
            return Persona('Mago', 100, 100, 0, 0, 'Sem', 0)

    def levelup(self):
        if self.nivel == 0:
            if self.xp < 2:
                print(f'ainda não possui XP, Seu Xp {self.xp} Necessário: 2')
                return Persona(self.classe, self.vida, self.dano, self.xp, self.nivel, self.akuma, self.wallet)
            if self.xp >= 2 <=5:
                print('Seu nivel aumentou Para 1')
                return Persona(self.classe, self.vida+50, self.dano+50, self.xp, self.nivel+1, self.akuma, self.wallet)
        if self.nivel == 1:
            if self.xp < 6:
                print(f'ainda não possui XP, Seu XP:{self.xp} Necessário: 6')
                return Persona(self.classe, self.vida, self.dano, self.xp, self.nivel, self.akuma, self.wallet)
            if self.xp >= 6 <= 10:
                print('Seu nivel aumentou Para 2')
                return Persona(self.classe, self.vida+100, self.dano+100, self.xp, self.nivel+1, self.akuma, self.wallet)

    def status(self):
        print(f'CLASSE: {self.classe}\nVIDA: {self.vida}\nDANO: {self.dano}\nXP: {self.xp}\nFRUTA: {self.akuma}')
        print(f'Seu nivel atual: {self.nivel}\n Seu dinheiro: {self.wallet}Zenis')    

    def batalha(persona, inimigo):
        rounds = 0
        InimigoVidaTemp = inimigo.vida
        PersonaVidaTemp = persona.vida
        if persona.akuma == 'borracha':
            buff = PersonaVidaTemp * 0.15
            PersonaVidaTemp += buff
        while True:
            rounds += 1


            #Persona atacando
            InimigoVidaTemp -= persona.dano
            print(f'ROUND{rounds}: Você ataca {inimigo.classe}, Vida restante: {InimigoVidaTemp}')
            #vitoria
            if InimigoVidaTemp <= 0:
                print('Vítoria')
                if inimigo.classe == 'InimigoFacil':
                    return Persona(persona.classe, persona.vida, persona.dano, persona.xp + 1, persona.nivel, persona.akuma, persona.wallet+500)
                if inimigo.classe == 'InimigoMedio':
                    return Persona(persona.classe, persona.vida, persona.dano, persona.xp +2, persona.nivel, persona.akuma, persona.wallet+10)

            #Inimigo Atacando
            PersonaVidaTemp -= inimigo.dano
            print(f'ROUND{rounds}: {inimigo.classe} te ataca, Vida restante: {PersonaVidaTemp}')
            #derrota
            if PersonaVidaTemp <= 0:
                print('DERROTA!, tente melhorar seus status, começe com batalhas mais fáceis')
                print('A Cada Derrota se perde 2 XP (nao importa o inimigo ainda)')
                return Persona(persona.classe, persona.vida, persona.dano, persona.xp - 2, persona.nivel, persona.akuma, persona.wallet)
        
    def akumas(persona):
        print('''Loja de frutas:
Borracha(1), custa: 100Zenis
    Buffs = +15(Porcento de vida) & Atq Especial(ainda nao feito) \n
Controle(2), custa: 500Zenis
    Buffs =  -10(Porcento de vida) & +40(Porcento de vida) & Atq Especial(ainda nao feito)
  Digite 0 Para volta ao menu
        ''')
        while True:
            try:
                compra = int(input('Escolha Uma ou volte para o menu: '))
                #volta menu
                if compra == 0: 
                    return Persona(persona.classe, persona.vida, persona.dano, persona.xp, persona.nivel, persona.akuma, persona.wallet)
                #gomu gomu
                if compra == 1:
                    if persona.wallet <100:
                        print(f'Ainda não possui 100 zenis, Seu dinheiro:{persona.wallet}')
                        return Persona(persona.classe, persona.vida, persona.dano, persona.xp, persona.nivel, persona.akuma, persona.wallet)
                    else:
                        persona.akuma = 'borracha'
                        print('Sucesso')
                        return Persona(persona.classe, persona.vida, persona.dano, persona.xp, persona.nivel, persona.akuma, persona.wallet-100)
                #ope ope
                if compra == 2:
                    pass
            except Exception as erro:
                print(f'Erro, relatório:{erro}')




class inimigo():
    def __init__(self, classe, vida, dano, haki):
        self.classe = classe
        self.vida = vida
        self. dano = dano
        self.haki = haki

#mecanica de haki ainda nao completa
InimigoFacil = inimigo('InimigoFacil', 100, 25, 'Sem')
InimigoMedio = inimigo('InimigoMedio', 200, 50, 'Com')


def StartGame(personagem):
    while True:
        try:
            print('''Digite 1 para Batalhar
Digite 2 para Tentar dar Level Up
Digite 3 para Olhar seus Status
Digite 4 para ir Para Loja de Frutas
Digite 5 para Sair
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
                personagem = Persona.akumas(personagem)
            if acao == 5:
                break
        except ValueError:
            print('Digite apenas algum número das opçoes')
        except Exception as erro:
            print(f'Algum erro desconhecido, relatório: {erro}')
