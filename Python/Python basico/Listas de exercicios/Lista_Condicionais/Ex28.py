# Exercicio 28
x = int(input('Digite numero: '))
y = int(input('Digite numero: '))
z = int(input('Digite numero: '))
print('Digite a media que gostaria de realizar: \n' \
'1 - Media geometrica\n' \
'2 - Media ponderada\n' \
'3 - Harmonica\n' \
'4 - Aritmetica\n' \
'0 - encerrar programa')
media = int(input(''))

if media == 1:
    print(f'A media geometrica e {(x*y*z)**(1/3):.2f}')
elif media == 2:
    print(f'A media ponderada e {(x+y*2+z*3)/6:.2f}')
elif media == 3:
    print(f'A media harmonica e {1/(1/x + 1/y + 1/z):.2f}')
elif media == 4:
    print(f'A media aritmetica e {(x+y+z)/(3):.2f}')
elif media == 0:
    print('numero invalido')
elif media<0 or media>4:
    print('numero invalido')