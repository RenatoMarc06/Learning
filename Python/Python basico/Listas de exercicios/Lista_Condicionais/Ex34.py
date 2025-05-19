# Exercicio 34
nota = float(input('Digite nota: '))
faltas = int(input('Digite o numero de faltas: '))

if faltas<=20:
    if 9<=nota<=10:
        print('Conceito A')
    elif 7.5<=nota<=8.9:
        print('Conceito B')
    elif 5<=nota<=7.4:
        print('Conceito C')
    elif 4<=nota<=4.9:
        print('Conceito D')
    elif 0<=nota<=3.9:
        print('Conceito E')
    elif nota<0 or nota<10:
        print('Nota invalida')
elif faltas>20:
    if 9<=nota<=10:
        print('Conceito B')
    elif 7.5<=nota<=8.9:
        print('Conceito C')
    elif 5<=nota<=7.4:
        print('Conceito D')
    elif 4<=nota<=4.9:
        print('Conceito E')
    elif 0<=nota<=3.9:
        print('Conceito E')
    elif nota<0 or nota<10:
        print('Nota invalida')