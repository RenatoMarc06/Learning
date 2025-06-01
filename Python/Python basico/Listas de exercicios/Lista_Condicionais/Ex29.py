import random
acertos = 0

for i in range(5):
    a = random.randint(1, 99)
    b = random.randint(1, 99)
    print(f'Pergunta {i+1}: qual a soma de {a} + {b}?')
    resp = int(input('Resposta: '))
    correta = a + b
    if resp == correta:
        acertos += 1
    print(f'Resposta correta: {correta}')

print(f'Total de acertos: {acertos} de 5')