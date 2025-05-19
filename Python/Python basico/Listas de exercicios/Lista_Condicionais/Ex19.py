# Exercicio 19
a = int(input('Digite numero: '))

if a%3==0:
    print('O numero e divisivel por 3')
    if a%5==0:
        print('O numero e divisivel por 5 tambem')
    elif a%5!=0:
        print('O numero nao e divisivel por 5')
elif a%3!=0:
    print('O numero nao e divisivel por 3')
    if a%5==0:
        print('O numero e divisivel por 5')
    elif a%5!=0:
        print(' O numero nao e divisivel por 5')
else:
    print('Numero nao inteiro')