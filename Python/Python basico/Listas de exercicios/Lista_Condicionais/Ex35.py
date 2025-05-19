# Exercicio 35
import sys
print('Digite uma data: ')
ano = int(input('Ano: '))
mes = int(input('Mes: '))
dia = int(input('Dia: '))

if ano % 400 == 0 or (ano%4 == 0 and ano%100 != 0):
    print('Ano bissexto')
    if 1<=mes<=12:
        if mes == 2:
            
        

else:
    print('Ano nao bissexto')
    if mes == 2 and dia == 29:
        print('Dia 29 de fevereiro apenas em ano bissexto')





