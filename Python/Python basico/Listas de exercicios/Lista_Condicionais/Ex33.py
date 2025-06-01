# Exercicio 33
import sys
preco = input('Digite o preco do produto: ')
try: 
    preco = int(preco)
    sys.exit()
except:
    print('Preco invalido')

aumento = 0

if preco < 50:
    aumento = preco + preco*(5/100)
    print(f'O novo preco e {aumento}')
elif 50 <= preco <= 100:
    aumento = preco + preco*(10/100)
    print(f'O novo preco e {aumento}')
elif 100 < preco:
    aumento = preco + preco*(15/100)
    print(f'O novo preco e {aumento}')

