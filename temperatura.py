class temp:
    def __init__(self, name, start, num):
        self.name = name
        self.start = start
        self.num = num 
        
        
    def init():
        celsius = temp('celsius', 0, 5)
        fahrenheit = temp('fahrenheit', 32, 9)
        kelvin = temp('kelvin', 273, 5)
        temps = [celsius, fahrenheit, kelvin]
        while True:
            option = int(input('''
1 - Criar nova temperatura
2 - transformar temperatura 
3 - status
                               :'''))
            
            #option 1
            if option == 1:
                x = temp.criar()
                temps.append(x)
            
            #option 2
            if option == 2: 
                option_temp = int(input('''
1 - celsius                                       
2 - fahrenheit
3 - kelvin
4 - (criada)
                                       :'''))
                if option_temp == 1: option_temp = celsius
                if option_temp == 2: option_temp = fahrenheit
                if option_temp == 3: option_temp = kelvin
                if option_temp == 4: option_temp = x
                option_temp1 = int(input('''
1 - celsius                                       
2 - fahrenheit
3 - kelvin
4 - (criada)
                                       :'''))
                if option_temp1 == 1: option_temp1 = celsius
                if option_temp1 == 2: option_temp1 = fahrenheit
                if option_temp1 == 3: option_temp1 = kelvin
                if option_temp1 == 4: option_temp1 = x
                option_amount = int(input('quanto: '))
                print(temp.translate(option_temp, option_amount, option_temp1))
                
            #option 3
            if option == 3:
                for item in temps:
                    print(item.name, item.start, item.num)
                
        
        
    def criar():
        new_name = str(input('name: '))
        new_start = int(input('start: '))
        new_num = int(input('num: '))
        return temp(f'{new_name}', new_start, new_num)
        
    
    def translate(temp, amount, temp1):
        return ((amount * temp1.num) - (temp.start * temp1.num) + (temp1.start * temp.num)) / temp.num 
                           
                           
    #def FandC(temp, amount):
        if temp == 'f': return (amount - 32) / 1.8 # f to c
        return amount * 1.8 + 32 # c to f


    #def KandC(temp, amount):
        if temp == 'k': return amount - 273 # k to c
        return amount + 273 # c to k


    #def FandK(temp, amount):
        if temp == 'f': return (amount - 32) / 1.8 + 273 # f to k 
        return (amount - 273) * 1.8 + 32 # k to f


#print(temp.translate(fahrenheit, 99, kelvin))
#print(temp.FandC('c', 58))
#print(temp.KandC('k', 298))
#print(temp.FandK('f', 99))
temp.init()