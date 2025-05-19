# Exercicio 8
import sys

Nota1 = float(input('digite a primeira nota: '))
if Nota1>10 or Nota1<0:
    print('nota 1 invalida')
    sys.exit()

Nota2 = float(input('digite a segunda nota: '))

if Nota2>10 or Nota2<0:
    print('nota 2 invalida')
    sys.exit()

print(f'a media e {(Nota1+Nota2)/2}')