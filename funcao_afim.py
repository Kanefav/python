def traduzir(x, y, grau=2):
    if grau == 1:
        a = y/x
        return f'{y}/{x} = {a}, equação: F(x)= {a}x'
    if grau == 2:
        a = y/x 
        a *= 1
        if y >= 0:
            return f'{y}/{x} = {a}, equação: F(x)= {a:.1f}x + {y}'
        else:
            return f'{y}/{x} = {a}, equação: F(x)= {a:.1f}x {y}'

while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        grau = int(input('grau[1|2]: '))
        print(traduzir(x, y, grau))
    except Exception as erro:
        print(erro)
        print('tradução: digita certo mula')