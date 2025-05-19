# Exercicio 4
import math as m
import cmath as c

a = int(input('digite um numero: '))

if a>0:
    print(f'A raiz quadrada e: {m.sqrt(a)}')
    print(f'O numero ao quadrado e: {a**2}')

# complemento no exercicio

elif a<0:
    print(f'A raiz quadrada e: {c.sqrt(a):.3f}')
    print(f'O numero negativo ao quadrado e: {a**2}')