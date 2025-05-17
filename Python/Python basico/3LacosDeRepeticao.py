a = []

for i in range(0,10,1): # repeticoes definidas
    a.append(i)

print(a)
print('\n')

for j, num in enumerate(a): # percorrer listas, tuplas, etc..
    print(j,num)

print('\n')
b = int(input('digite um numero: '))
while True: # repeticoes nao definidas
    if b<10:
        b = int(input('digite um numero: '))
        continue
    elif b>10:
        print("voce digitou um numero maior que 10")
        break
