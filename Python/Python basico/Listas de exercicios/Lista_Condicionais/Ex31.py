# Exercicio 31
import sys
peso = input('Digite seu peso (Kg): ')
try: 
    peso = float(peso)
except ValueError:
    print('Digite um peso valido.')
    sys.exit()
if peso<=0: 
    print('Digite um peso valido')
    sys.exit()

altura = float(input('Digite sua altura (m): '))
try: 
    altura = float(altura)
except ValueError:
    print('Digite um peso valido.')
    sys.exit()

if peso<=60:
    if altura<1.2:
        print('A')
    elif 1.2<=altura<1.7:
        print('B')
    elif 1.7<=altura:
        print('C')
elif peso>60 and peso<90:
    if altura<1.2:
        print('D')
    elif 1.2<=altura<1.7:
        print('E')
    elif 1.7<=altura:
        print('F')
elif peso>=90:
    if altura<1.2:
        print('G')
    elif 1.2<=altura<1.7:
        print('H')
    elif 1.7<=altura:
        print('I')