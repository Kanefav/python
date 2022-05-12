def matrix(a, b):
    #line = len(a)
    #column = len(a[0])
    
    c = []
    for line in range(0, len(a)):
        ctemp = []
        for item in range(0, len(a[0])):
            ctemp.append(a[line][item] + b[line][item])
        c.append(ctemp)
    return c
            


m = [ 
    [1, 2],
    [3, 4]
    ]
mtwo = [
    [5, 6],
    [7, 8]
    ]   
print(matrix(m, mtwo))