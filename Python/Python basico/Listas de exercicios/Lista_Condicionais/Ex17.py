# Exercicio 17
import sys

basemaior = int(input('digite o tamanho da base maior: '))

if basemaior<=0:
    print('tamanho invalido da base maior')
    sys.exit()

basemenor = int(input('digite o tamanho da base menor: '))

if basemenor<=0:
    print('tamanho invalido da base menor')
    sys.exit()

if basemenor>basemaior:
    print('base menor deve ser menor que base maior')
    sys.exit()

altura = int(input('digite a altura: '))

if basemenor<=0:
    print('altura invalida')
    sys.exit()

a = ((basemaior+basemenor)*altura)/2

print(f'A area do trapezio e {a}')

    