#verificar string

def verificar(First, Second):
    Igual = False
    if First == Second:
        Igual = True
        return Igual
    else:
        return Igual


FirstString = str(input('1String: '))
SecondString = str(input('2String: '))
print(verificar(FirstString, SecondString))