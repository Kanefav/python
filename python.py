blocks = int(input("Enter the number of blocks: "))
height = 0
while True:
    height += 1
    blocks -= height
    if blocks <= 0:
        break

print("The height of the pyramid:", height-1)


user_word = str(input('Digite: '))
for letter in user_word:
    if letter in 'aeiou':
        continue 
    print(letter)
    
    
def chupacabra(word):
    while True:
        if word == 'chupacabra':
            return print("You've successfully left the loop.")
        else:
            return chupacabra(str(input('Digite: ')))


chupacabra(str(input('Digite: '))) 