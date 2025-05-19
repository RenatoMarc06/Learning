# Exercicio 24
import sys
valor = input('Qual e o valor do produto: ')
try: 
    valor = float(valor)
except ValueError:
    print('Digite um valor valido.')
    sys.exit()

print(' Estados que entregamos: \n' \
'Minas Gerais: mg\n' \
'Sao Paulo: sp\n'
'Rio de Janeiro: rj\n' \
'Mato Grosso do Sul: ms\n')

estado = input('Digite o estado da encomenda para calculo de preco final: ')

if estado == 'mg':
    print(f'O valor final para Minas Gerais e {valor + valor*0.07}')
elif estado == 'sp':
    print(f'O valor final para Sao Paulo e {valor + valor*0.12}')
elif estado == 'rj':
    print(f'O valor final para o Rio de Janeiro e {valor + valor*0.15}')
elif estado == 'ms':
     print(f'O valor final para o Mato Grosso do Sul e {valor + valor*0.08}')
else:
    print('Nao entregamos para este estado ou o estado nao existe')