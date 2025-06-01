# Exercicio 5
a = []
for i in range(0,10,1):
    b = int(input('Digite um numero: ')) 
    a.append(b)

print(sum(a))


print('Ou') # Neste sera o ultimo que mostrarei que há formas diferentes

c = 0 # Acredito que dessa forma se encaixa mais na proposta do exercicio
d = 0
while c<10:
    e = int(input('Digite um numero: ')) 
    d = d + e
    c = c+1
print(d)