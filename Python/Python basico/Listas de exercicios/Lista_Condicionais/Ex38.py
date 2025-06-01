# Exercicio 38
import sys
anoA = 2008
dia = int(input('Digite o dia: '))
mes = int(input('Digite o mes: '))
ano = int(input('Digite o ano: '))

if ano > anoA or ano < 0:
    print('data invalida')
    sys.exit()
elif mes < 1 or mes > 12:
    print('data invalida')
    sys.exit()
elif dia < 1:
    print('data invalida')
    sys.exit()
    
elif mes == 2:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        if dia > 29:
            print('data invalida')
            sys.exit()
        else:
            print('data valida')
            sys.exit()
    else:
        if dia > 28:
            print('data invalida')
            sys.exit()
        else:
            print('data valida')
            sys.exit()
elif mes in [4, 6, 9, 11]:
    if dia > 30:
        print('data invalida')
        sys.exit()
    else:
        print('data valida')
        sys.exit()
else:
    if dia > 31:
        print('data invalida')
        sys.exit()
    else:
        print('data valida')
        sys.exit()