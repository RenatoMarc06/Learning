# Exercicio 10
s = input('digite o sexo (f para feminino e m para masculino): ')
h = float(input('digite a altura em m: '))

if s == 'm':
    print(f'seu peso ideal e {72.7 * h - 58}')
elif s == 'f':
    print(f'seu peso ideal e {62.1 * h - 44.7}')
else:
    print('sexo invalido')