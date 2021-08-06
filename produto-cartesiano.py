def produtoCartesiano(x, y):
    for numero in range(0, len(x)):
       for valor in range(0, len(y)):
            xyTemp = x[numero], y[valor]
            xy.append(xyTemp)
    return xy
            

x = []
y = []
xy = []
while True:
    try:
        xInput = int(input('Valores de x: (digite 999 para ir para o y) '))
        if xInput == 999:
            break
        else:
            x.append(xInput)
    except Exception as erro:
        print(f'erro: {erro}')
while True:
    try:
        yInput = int(input('Valores de y: (digite 999 para terminar) '))
        if yInput == 999:
            break
        else:
            y.append(yInput)
    except Exception as erro:
        print(f'erro: {erro}')
print(f'X: {x}, Y: {y}')
print(produtoCartesiano(x, y))
