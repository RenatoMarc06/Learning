# Exercicio 26
import sys
km = int(input('Digite a distancia percorrida(Km): '))
l = int(input('Digite a quantidade de gasolina gasta(L): '))
if l == 0:
    print('Voce nao percorreu nenhuma distancia')
    sys.exit()

if km/l < 8:
    print('Venda o carro: ')
elif 8<=km/l<=12: # Acredito que houve uma troca entre 12 e 14 na tabela
    print('Economico')
elif 12<km/l<=14:
    print('Super economico')