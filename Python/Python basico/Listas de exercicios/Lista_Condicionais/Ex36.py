# Exercicio 36
import sys
vendas = input('Digite o total em vendas: ')
try: 
    vendas = int(vendas)
    sys.exit()
except:
    print('Total invalido')

comissao = 0

if 100000 <= vendas:
    comissao = 700 + vendas*(16/100)
    print(f'A comissao e {comissao}')
elif 80000<=vendas<100000:
    comissao = 650 + vendas*(14/100)
    print(f'A comissao e {comissao}')
elif 60000<=vendas<80000:
    comissao = 600 + vendas*(14/100)
    print(f'A comissao e {comissao}')
elif 40000<=vendas<60000:
    comissao = 550 + vendas*(14/100)
    print(f'A comissao e {comissao}')
elif 20000<=vendas<40000:
    comissao = 500 + vendas*(14/100)
    print(f'A comissao e {comissao}')
elif vendas<20000:
    comissao = 400 + vendas*(14/100)
    print(f'A comissao e {comissao}')
elif vendas<0:
    print(f'Nao e possivel vendas serem negativas')

