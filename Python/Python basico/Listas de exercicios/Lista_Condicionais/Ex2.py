# Exercicio 2
import math as m
import cmath as c

a = int(input('digite um numero: '))

if a>0:
    print(f'A raiz quadrada e: {m.sqrt(a)}')

elif a<0:
    print(f'numero invalido')

# complemento no exercicio, tirando raizes irracionais
"""
elif a<0:
    print(f'A raiz quadrada e: {c.sqrt(a):.3f}') 
"""