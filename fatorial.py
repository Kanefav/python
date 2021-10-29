def fatorial(num, division=False):
    numbers = []
    for num in range(num, 0, -1):
        numbers.append(num)
    if division==True:
        return numbers
    else:
        return multiplicador_lista(numbers)


def multiplicador_lista(list):
    output = 1
    for num in list:
        output *= num
    return output


def dividir_fatorial(Fa, Fb):
    x = 0
    numbers = []
    Fa = fatorial(Fa, True)
    Fb = fatorial(Fb, True)
    for diferente in range(len(Fb), len(Fa)):
        numbers.append(Fa[x])
        x += 1
    return multiplicador_lista(numbers) 


print(f'fatorial de 12: {fatorial(12)}')
print('dividido por')
print(f'fatorial de 10: {fatorial(10)}', end= ' ')
print('=', end=' ')
print(dividir_fatorial(12, 10))