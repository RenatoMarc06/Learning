# Exercicio 25
import sys
import numpy as np

a = float(input('digite primeiro termo: ')) # pode ser um numero racional
if a == 0:
    print('Nao e equacao d segundo grau')
    sys.exit()

b = float(input('digite segundo termo: '))
c = float(input('digite terceiro termo: '))
delta = b**2 -4*a*c

if delta == 0:
    print('Existe raiz real')
    print(f'A raiz e: {(-b)/(2*a)}')
elif delta < 0:
    print('Nao existe raiz real')
elif delta > 0:
    x1 = (-b - np.sqrt(delta))/(2*a)
    x2 = (-b + np.sqrt(delta))/(2*a)
    print(f'As raizes sao: {x1:.2f} e {x2:.2f}')
    