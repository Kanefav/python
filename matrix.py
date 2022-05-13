def matrix_pol(a, b, pol='+'): # pol-plus or less
    #line = len(a)
    #column = len(a[0])
    
    c = []
    for line in range(0, len(a)):
        ctemp = []
        for item in range(0, len(a[0])):
            if pol == '-':
                ctemp.append(a[line][item] - b[line][item])
            else:
                ctemp.append(a[line][item] + b[line][item])
        c.append(ctemp)
    return c
            

def matrix_gi(line, column): # gi-grade index
    matrix = []
    for eachline in range(1, line+1):
        x = []
        for eachcolumn in range(1, column+1):
            x.append(eachline + eachcolumn)
        matrix.append(x)
    return matrix

m = [ 
    [1, 2],
    [3, 4]
    ]
mtwo = [
    [5, 6],
    [7, 8]
    ]   
#print(matrix_pol(m, mtwo, '-'))

print(matrix_gi(2, 2))