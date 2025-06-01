# Exercicio 15 e 16
import sys
N = int(input('Digite inteiro positivo impar: '))
if N <0:
    print('Digite um inteiro positivo')
    sys.exit()
if N %2==0:
    print('Digite um numero impar')
    sys.exit()

print('Crescente:')
for i in range(0,N+1,1):
    if i%2==1:
        print(i)
print('Decrescente:')
for i in range(N ,0,-1):
    if i%2==1:
        print(i)