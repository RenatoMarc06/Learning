# Exercicio 40
import sys
custo = input('Digite o custo do carro: ')
try: 
    custo = int(custo)
except:
    print('Custo invalido')
    sys.exit()

CustoTotal = 0

if custo < 12000:
    CustoTotal = custo + custo*(5/100)
    print(f'Custo total e {CustoTotal}')
elif 12000 <= custo <= 25000:
    CustoTotal = custo + custo*(10/100) + custo*(15/100) 
    print(f'Custo total e {CustoTotal}')
elif 25000 < custo:
    CustoTotal = custo + custo*(15/100) + custo*(20/100) 
    print(f'Custo total e {CustoTotal}')