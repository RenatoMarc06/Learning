# Exercicio 11 e 12
import sys
N  = int(input('Digite inteiro positivo: '))
if N <0:
    print('Digite inteiro positivo')
    sys.exit()
print('Crescente:')
for i in range(0,N +1,1):
    print(i)
print('Decrescente:')
for i in range(N ,0-1,-1):
    print(i)