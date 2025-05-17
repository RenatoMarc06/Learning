# Exercicio 14
import sys

Nota1 = float(input('digite a nota do trabalho de laboratorio: '))
if Nota1>10 or Nota1<0:
    print('nota do trabalho de laboratorio invalida')
    sys.exit()

Nota2 = float(input('digite a nota da avaliacao semestral: '))
if Nota2>10 or Nota2<0:
    print('nota da avaliacao semestral invalida')
    sys.exit()

Nota3 = float(input('digite a nota do exame final: '))
if Nota3>10 or Nota3<0:
    print('nota do exame final invalida')
    sys.exit()

Nota1 = Nota1*0.2
Nota2 = Nota2*0.3
Nota3 = Nota3*0.5
media = Nota1 + Nota2 + Nota3

if 0<=media<=2.9:
    print('aluno aprovado')

elif 3<=media<=4.9:
    print('aluno de recuperacao')

elif 5<=media:
    print('aluno aprovado')