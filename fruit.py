value = float(input('valor: '))
owner = value * 0.45 
owner = int(owner)
tax = value - owner
print(f'''value: {value}
    partes
dono: {owner}
tax: {tax}
      ''')