from math import sqrt


def equation(e, g): # equation, grau
    values = [] # a-0 b-1 c-2
    temp = ''
    
    for letter in range(0, len(e)):                     # complete the sinals (theyre not being used)
        if e[letter] in '1234567890':
            temp += f'{e[letter]}'
            if letter+1 == len(e):
                values.append(temp)
        else:
            if len(temp) > 0:
                values.append(temp)
            temp = ''
            
    
    delta = int(values[1]) * int(values[1]) - (4 * int(values[0]) * int(values[2]))
    if delta <= 0:
        raizD = 0
    else:
        raizD = int(sqrt(delta))
    bhaskara = -(int(values[1])) + raizD
    bhaskara2 = -(int(values[1])) - raizD
    b = bhaskara // (2*int(values[0]))
    b2 = bhaskara2 // (2*int(values[0]))
    return [b, b2]

        


print(equation('2x^ - 4x - 20', 2))