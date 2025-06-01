# Exercicio 13 e 14
import sys
N = int(input('Digite inteiro positivo par: '))
if N <0:
    print('Digite um inteiro positivo')
    sys.exit()
if N %2==1:
    print('Digite um numero par')
    sys.exit()

print('Crescente:')
for i in range(0,N+1,1):
    if i%2==0:
        print(i)
print('Decrescente:')
for i in range(N,0-1,-1):
    if i%2==0:
        print(i)