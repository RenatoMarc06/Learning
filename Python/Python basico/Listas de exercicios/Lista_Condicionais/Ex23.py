# Exercicio 23
import sys
ano = input('Digite o ano: ')

try: 
    ano = int(ano)
except ValueError:
    print('Digite um ano valido.')
    sys.exit()

if ano % 400 == 0:
    print('Ano bissexto')

elif ano%4 == 0 and ano%100 != 0:
    print('Ano bissexto')

else:
    print('Ano nao bissexto')
