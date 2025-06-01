# Exercicio 7
a = 0
i = 0
while i<10:
    b = int(input('Digite numero: '))
    if b>=0:
        a = a + b
        i = i + 1
    elif b<10:
        print('Numero negativo')

print(a/10)

