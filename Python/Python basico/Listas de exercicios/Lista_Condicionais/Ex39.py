# Exercicio 39
import sys
salario = input('Digite o salario atual do funcionario: ')
tempo = input('Digite o tempo de servico do funcionario: ')
try: 
    salario = int(salario)
    tempo = int(tempo)
except:
    print('Salario invalido')
    print('Tempo invalido')
    sys.exit()

SalarioNovo = 0

if salario < 500:
   SalarioNovo = salario + salario*(25/100)
elif 500 <= salario < 1000:
    SalarioNovo = salario + salario*(20/100)
elif 1000 <= salario < 1500:
    SalarioNovo = salario + salario*(15/100)
elif 1500 <= salario <= 2000:
    SalarioNovo = salario + salario*(10/100)
elif 2000 < salario:
    SalarioNovo = salario
    print(f'Sem reajuste: {SalarioNovo}')
elif salario<0:
    print('Salario invalido')
if tempo < 1:
    SalarioNovo = SalarioNovo
    print(f'Sem bonus: {SalarioNovo}')
elif 1 <= tempo <= 3:
    SalarioNovo = SalarioNovo + 100
    print(f'O salario atual e {SalarioNovo}')
elif 4 <= tempo <= 6:
    SalarioNovo = SalarioNovo + 200
    print(f'O salario atual e {SalarioNovo}')
elif 7 <= tempo <= 10:
    SalarioNovo = SalarioNovo + 300
    print(f'O salario atual e {SalarioNovo}')
elif 10 < tempo:
    SalarioNovo = SalarioNovo + 500
    print(f'O salario atual e {SalarioNovo}')
elif tempo<0:
    print('Tempo invalido')