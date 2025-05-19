# Exercicio 11
a = input('digite um numero maior que 0: ')

if int(a)>0:
    print(sum(int(i) for i in a ))

elif int(a)<=0:
    print('numero invalido')