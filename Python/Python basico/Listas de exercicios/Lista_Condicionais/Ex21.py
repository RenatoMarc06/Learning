# Exercicio 21
import sys
print('Escolha a opcao: \n' \
'1 - Soma de 2 numeros.\n' \
'2 - Diferenca entre 2 numeros (maior pelo menor).\n' \
'3 - Produto de 2 numeros.\n' \
'4 - Divisao entre 2 numeros (denominador nao pode ser zero).\n'
)
op = input('')
try: 
    op = int(op)
    if op>4 or op<1:
        print('Operacao invalida')
        sys.exit()
except ValueError:
    print('Digite um numero para selecionar operacao.')
    sys.exit()

a = input('Digite um numero: ')
try: 
    a = int(a)
except ValueError:
    print('Digite numeros.')
    sys.exit()

b = input('Digite um outro numero: ')
try: 
    b = int(b)
except ValueError:
    print('Digite numeros.')
    sys.exit()

if op == 1:
    print(f'A soma e {a+b}')
elif op==2:
    if a>b:
        print(f'A diferenca e {a-b}')
    elif a<b:
        print(f'A diferenca e {b-a}')

elif op==3:
    print(f'A multiplicacao e {a*b}')
elif op==4:
    if b==0:
        print('Nao se pode dividir por 0')
    else:
        print(f'A divisao e {a/b}')


