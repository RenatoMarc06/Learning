# Exercicio 17
import sys
N = int(input('Digite inteiro positivo: '))
if N <0:
    print('Digite um inteiro positivo')
    sys.exit()
a = 0
for i in range(0,N+1,1):
    a = a+i
print(a)