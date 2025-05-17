# Exercicio 18
import sys
op = input('Escolha uma operacao: (1/soma 2/sub 3/multi 4/div): ')

try:
    op = int(op)

except ValueError:
    print('Operacao invalida')
    sys.exit()

a = input('digite o primeiro numero: ')
b = input('digite o segundo numero: ')
try:
    a = int(a)
    b= int(b)
except ValueError:
    print('Voce precisa digitar numeros')
    sys.exit()

if op == 1:
    print(a+b)
elif op == 2:
    print(a-b)
elif op == 3:
    print(a*b)
elif op == 4:
    if b == 0:
        print('Operacao invalida')
    if b!=0:
        print(a/b)
else:
    print('Operacao invalida')
