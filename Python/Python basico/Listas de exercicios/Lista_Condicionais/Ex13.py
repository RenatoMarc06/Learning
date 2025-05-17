# Exercicio 13 (correcao, 6, nao 60)
import sys

Nota1 = float(input('digite a primeira nota: '))
if Nota1>10 or Nota1<0:
    print('nota 1 invalida')
    sys.exit()

Nota2 = float(input('digite a segunda nota: '))
if Nota2>10 or Nota2<0:
    print('nota 2 invalida')
    sys.exit()

Nota3 = float(input('digite a terceira nota: '))
if Nota3>10 or Nota3<0:
    print('nota 3 invalida')
    sys.exit()

media = (Nota1*1 + Nota2*2 + Nota3*2)/4

if media>=6:
    print('aluno aprovado')

elif media<6:
    print('aluno reprovado')