# Exercicio 41
import sys
peso = input('Digite seu peso (Kg): ')
try: 
    peso = float(peso)
except ValueError:
    print('Digite um peso valido.')
    sys.exit()
if peso<=0: 
    print('Digite um peso valido')
    sys.exit()

altura = float(input('Digite sua altura (cm): '))
try: 
    altura = float(altura)
except ValueError:
    print('Digite um peso valido.')
    sys.exit()

if peso/((altura/100)**2) < 18.5:
    print('Abaixo do peso')
elif 18.6<peso/((altura/100)**2)<24.9:
    print('Saudavel')
elif 25<peso/((altura/100)**2)<29.9:
    print('Peso em excesso')
elif 30<peso/((altura/100)**2)<34.9:
    print('Obesidade grau 1')
elif 35<peso/((altura/100)**2)<39.9:
    print('Obesidade grau 2(Severa)')
elif 40<=peso/((altura/100)**2):
    print('Obesidade grau 3(morbida)')
