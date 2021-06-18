print('Faça um Programa que peça dois números e imprima o maior deles.'
'Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.')


def maiornum(a, b):
    MaiorNumTemp = a
    if b > a:
        MaiorNumTemp = b
    print(f'O maio numero é {MaiorNumTemp}')


def numposneg(a, b):
    if a >= 0:
        print(f'O numero {a} é positivo')
    else:
        print(f'O numero {a} não é positivo')
    if b >= 0:
        print(f'O numero {b} é positivo')
    else:
        print(f'O numero {b} não é positivo')


#programa principal 
num = int(input('Digite um numero '))
num2 = int(input('Digite outro numero'))
maiornum(num, num2)
numposneg(num, num2)