# Exercicio 22
import sys
idade = input('Digite idade do trabalhador: ')

try: 
    idade = int(idade)
except ValueError:
    print('Digite uma idade valida.')
    sys.exit()

TempoServico = input('Digite o tempo de servico: ')

try: 
    TempoServico = float(TempoServico) # pode ser algo como 29.5 anos, conta-se como vinte nove e meio
except ValueError:
    print('Digite um tempo valido.')
    sys.exit()

if idade >= 65 or TempoServico >= 30:
    print('O trabalhador pode se aposentar')

elif idade >=60 and TempoServico >=25:
    print('O trabalhador pode se aposentar')

else: 
    print('O trabalhador nao pode se aposentar')
