# Exercicio 30
a = int(input('Digite numero: '))
b = int(input('Digite numero: '))
c = int(input('Digite numero: '))

if a>=b and a>=c:
    if b>=c:
        print(f'{a} {b} {c}')
    elif c>=b:
        print(f'{a} {c} {b}')

elif b>=a and b>=c:
    if a>=c:
        print(f'{b} {a} {c}')
    elif c>=a:
        print(f'{b} {c} {a}')

elif c>=a and c>=b:
    if a>=b:
        print(f'{c} {a} {b}')
    elif b>=a:
        print(f'{c} {b} {a}')


# Complemento
'''
a = int(input('Digite número: '))
b = int(input('Digite número: '))
c = int(input('Digite número: '))

numeros = [a, b, c]
numeros.sort(reverse=True)

print(f'{numeros[0]} {numeros[1]} {numeros[2]}')
'''
# Mais facil rsrs

