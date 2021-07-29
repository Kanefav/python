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
        if self.nivel == 2:
            if self.xp < 14:
                print(f'ainda não possui XP, Seu XP:{self.xp} Necessário: 15')
                return Persona(self.classe, self.vida, self.dano, self.xp, self.nivel, self.akuma, self.wallet)
            if self.xp > 15 <= 20:
                print('Seu nível aumentou para 3')
                return Persona(self.classe, self.vida+150, self.dano+150, self.xp, self.nivel+1, self.akuma, self.wallet)
        if self.nivel == 3:
            print('Ainda não tem outro nível')
            return Persona(self.classe, self.vida, self.dano, self.xp, self.nivel, self.akuma, self.wallet)


    def status(self):
        print(f'CLASSE: {self.classe}\nVIDA: {self.vida}\nDANO: {self.dano}\nXP: {self.xp}\nFRUTA: {self.akuma}')
        print(f'Seu nivel atual: {self.nivel}\n Seu dinheiro: {self.wallet}Zenis')    

    def batalha(persona, inimigo):
        rounds = 0
        InimigoVidaTemp = inimigo.vida
        PersonaVidaTemp = persona.vida
        PersonaDanoTemp = persona.dano
        if persona.akuma == 'borracha':
            buff = PersonaVidaTemp * 0.15
            PersonaVidaTemp += buff
        if persona.akuma == 'controle':
            buffdano = PersonaDanoTemp * 0.40
            buffvida = PersonaVidaTemp * 0.10
            PersonaVidaTemp -= buffvida
            PersonaDanoTemp += buffdano
        if persona.akuma == 'estrondo':
            buffvida = PersonaVidaTemp * 0.30 
            PersonaVidaTemp += buffvida
        while True:
            rounds += 1

            #persona Atacando
            opcao = int(input('1-Atacar  2-AtqEspecial  3-Desistir'))
            if opcao == 1:
                InimigoVidaTemp -= PersonaDanoTemp
                print(f'ROUND{rounds}: Você ataca {inimigo.classe}, Vida restante: {InimigoVidaTemp}')
            if opcao == 2:
                if persona.akuma == 'Sem':
                    print('Você não possui nenhum AtqEspecial')
                if persona.akuma == 'borracha':
                    input('AtqEspecial: Red Hawk:(120 de dano)')
                    InimigoVidaTemp -= 120
                    print(f'ROUND{rounds}: Você usou Red Hawk, Vida restante: {InimigoVidaTemp}')
                if persona.akuma == 'controle':
                    input('AtqEspecial: Gamma Rush:(240 de dano)')
                    InimigoVidaTemp -= 240
                    print(f'ROUND{rounds}: Você usou Gamma Rush, Vida restante: {InimigoVidaTemp}')
                if persona.akuma == 'estrondo':
                    input('AtqEspecial: El Thor:(400 de dano)')
                    InimigoVidaTemp -= 400
                    print(f'ROUND{rounds}: Você usou El Thor, Vida restante: {InimigoVidaTemp}')
            if opcao == 3:
                print('A luta acabou com sua desistência')
                return Persona(persona.classe, persona.vida, persona.dano, persona.xp +2, persona.nivel, persona.akuma, persona.wallet)
            #vitoria
            if InimigoVidaTemp <= 0:
                print('Vítoria')
                if inimigo.classe == 'InimigoFacil':
                    return Persona(persona.classe, persona.vida, persona.dano, persona.xp + 100, persona.nivel, persona.akuma, persona.wallet+500) #1 #50
                if inimigo.classe == 'InimigoMedio':
                    return Persona(persona.classe, persona.vida, persona.dano, persona.xp +2, persona.nivel, persona.akuma, persona.wallet+100)
                if inimigo.classe == 'BossFacil':
                    return Persona(persona.classe, persona.vida, persona.dano, persona.xp +5, persona.nivel, persona.akuma, persona.wallet+400)

            #Inimigo Atacando
            if persona.akuma in 'estrondo':
                print(f'Você possuiu uma fruta nome dela {persona.akuma}')
                if inimigo.haki == 'Com':
                    PersonaVidaTemp -= inimigo.dano
                    print(f'ROUND{rounds}: {inimigo.classe} Te acerta, Efeito Logia, Vida restante: {PersonaVidaTemp}')
                else:
                    print(f'ROUND{rounds}: {inimigo.classe} Não te acerta, Efeito Logia, Vida restante: {PersonaVidaTemp}')
            else:
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
    Buffs =  -10(Porcento de vida) & +40(Porcento de dano) & Atq Especial(ainda nao feito) \n
Estrondo(3), custa: 1000Zenis
    Buffs = +30(Porcento de vida) & Logia & Atq Especial(ainda nao feito) 
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
                    if persona.wallet <500:
                        print(f'Ainda não possui 500 zenis, Seu dinheiro:{persona.wallet}')
                        return Persona(persona.classe, persona.vida, persona.dano, persona.xp, persona.nivel, persona.akuma, persona.wallet)
                    else:
                        persona.akuma = 'controle'
                        print('Sucesso')
                        return Persona(persona.classe, persona.vida, persona.dano, persona.xp, persona.nivel, persona.akuma, persona.wallet-500)
                #goro goro
                if compra == 3:
                    if persona.wallet <1000:
                        print(f'Ainda não possui 1000 zenis, Seu dinheiro:{persona.wallet}')
                        return Persona(persona.classe, persona.vida, persona.dano, persona.xp, persona.nivel, persona.akuma, persona.wallet)
                    else:
                        persona.akuma = 'estrondo'
                        print('Sucesso')
                        return Persona(persona.classe, persona.vida, persona.dano, persona.xp, persona.nivel, persona.akuma, persona.wallet-1000)
            #erro
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
BossFacil = inimigo('BossFacil', 600, 150, 'Com')


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
                acaobatalha = int(input('''
Digite 0 para ver os bosses
Digite 1 para batalha facil
digite 2 para batalha média:
'''))
                if acaobatalha == 0:
                    print('Digite 3 para boss facil')
                    acaobatalha = int(input('a dada'))
                    if acaobatalha == 3:
                        personagem = Persona.batalha(personagem, BossFacil)
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
