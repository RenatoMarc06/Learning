# Exercicio 8
maior = 0
menor = 0

for i in range(0,10,1):
    num = int(input('Digite numero: '))
    if num>maior:
        maior = num
    if menor == 0 or num<menor:
        menor = num
    
print(f'O maior numero e {maior} e o menor e: {menor}')