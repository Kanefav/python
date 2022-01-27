class temp:
    def __init__(self, name, start, num):
        self.name = name
        self.start = start
        self.num = num 
    
    def translate(temp, amount, temp1):
        return ((amount * temp1.num) - (temp.start * temp1.num) + (temp1.start * temp.num)) / temp.num 
                           

celsius = temp('c', 0, 5)
fahrenheit = temp('f', 32, 9)
kelvin = temp('k', 273, 5)
while True:
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