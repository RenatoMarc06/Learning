# Exercicio 37
h1 = int(input('Hora de chegada: '))
m1 = int(input('Minuto de chegada: '))
h2 = int(input('Hora de saida: '))
m2 = int(input('Minuto de saida: '))

valido = 0 <= h1 <= 24 and 0 <= h2 <= 24 and 0 <= m1 <= 59 and 0 <= m2 <= 59

if not valido:
    print('Hora ou minuto invalido')
    exit()

t1 = h1 * 60 + m1
t2 = h2 * 60 + m2

if t2 < t1:
    t2 = t2 + 24 * 60

tempo = t2 - t1
horas = tempo // 60
minutos = tempo % 60

tempo_em_horas = horas + (1 if minutos > 0 else 0)

if tempo_em_horas <= 1:
    preco = 5
elif tempo_em_horas == 2:
    preco = 10
elif tempo_em_horas == 3:
    preco = 17.5
else:
    preco = 17.5 + (tempo_em_horas - 3) * 5

print(f'Tempo total: {horas}h {minutos}min')
print(f'Valor a pagar: R${preco:.2f}')