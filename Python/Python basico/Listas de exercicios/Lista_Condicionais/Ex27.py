# Exercicio 27
import sys
idade = int(input('Digite a idade do nadador: '))
 # Posso verificar se e numero ou nao, fiz em alguns codigos, porem nesse caso e em alguns preferi nao fazer, porem e possivel

if 5<=idade<=7:
    print('Infantil A')
elif 8<=idade<=10:
    print('Infantil B')
elif 11<=idade<=13:
    print('Juvenil A')
elif 14<=idade<=17:
    print('Juvenil B')
elif idade>=18:
    print('Senior')
else: # Acrescentei
    print('Idade insuficiente para nadar')
