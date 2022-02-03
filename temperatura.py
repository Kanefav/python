class temp:
    def __init__(self, name, start, num):
        self.name = name
        self.start = start
        self.num = num 
    
    def translate(temp, amount, temp1):
        return ((amount * temp1.num) - (temp.start * temp1.num) + (temp1.start * temp.num)) / temp.num 
                           
                           
    def FandC(temp, amount):
        if temp == 'f': return (amount - 32) / 1.8 # f to c
        return amount * 1.8 + 32 # c to f


    def KandC(temp, amount):
        if temp == 'k': return amount - 273 # k to c
        return amount + 273 # c to k


    def FandK(temp, amount):
        pass


celsius = temp('c', 0, 5)
fahrenheit = temp('f', 32, 9)
kelvin = temp('k', 273, 5)
x = temp('x', 20, 3)
while True:
    break
    ask = str(input('1 - celsius, 2 - fahrenheit, 3 - kelvin: '))
    if ask == '1':
        ask = celsius
    if ask == '2':
        ask = fahrenheit
    if ask == '3':
        ask = kelvin
    print('to')
    ask1 = str(input('1 - celsius, 2 - fahrenheit, 3 - kelvin: '))
    if ask1 == '1':
        ask1 = celsius
    if ask1 == '2':
        ask1 = fahrenheit
    if ask1 == '3':
        ask1 = kelvin
    amount = int(input('temperatura: '))
    print(temp.translate(ask, amount, ask1))    
#print(temp.translate(celsius, 58.888888888888886, fahrenheit), 'class')
print(temp.FandC('c', 58), 'notClass')
print(temp.KandC('k', 298))