# Exercicio 20
A = int(input('digite o valor do primeiro lado: '))
B = int(input('digite o valor do segundo lado: '))
C = int(input('digite o valor do terceiro lado: '))

if (B+C) > A and (C+A) > B and (A+B)>C:
    if A==B and B==C and C==A:
        print('Triangulo existente e equilatero')
    elif A==B or B==C or C==A:
        print('Triangulo existente e escaleno')
    elif A!=B and B!=C and C!=A:
        print('Triangulo existente e isosceles')
else:
    print('Triangulo impossivel de existir')