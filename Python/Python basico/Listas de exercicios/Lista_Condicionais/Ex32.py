# Exercicio 32 # Vou melhorar o exercicio para deixa-lo mais real
Anotacao = []
soma = 0
print('Cardapio: ') 
print('Cachorro quente - Codigo 100 - preco: R$1,20')
print('Bauru simples - Codigo 101 - preco: R$1,30')
print('Bauru com ovo - Codigo 102 - preco: R$1,50')
print('Hamburguer - Codigo 103 - preco: R$1,20')
print('Cheeseburger - Codigo 104- preco: R$1,70')
print('Suco - Codigo 105 - preco: R$2,20')
print('Refrigerante - Codigo 106 - preco: R$1,00')
print('Finalizar pedido - Codigo 0')

while True:
    codigo = input('Digite o codigo do pedido: ')
    if codigo == '100':
        Anotacao.append('Cachorro quente')
        print(Anotacao)
        soma = soma + 1.20
    elif codigo == '101':
        Anotacao.append('Bauru simples')
        print(Anotacao)
        soma = soma + 1.30
    elif codigo == '102':
        Anotacao.append('Bauru com ovo')
        print(Anotacao)
        soma = soma + 1.50
    elif codigo == '103':
        Anotacao.append('Hamburguer')
        print(Anotacao)
        soma = soma + 1.20
    elif codigo == '104':
        Anotacao.append('Cheeseburguer')
        print(Anotacao)
        soma = soma + 1.70
    elif codigo == '105':
        Anotacao.append('Suco')
        print(Anotacao)
        soma = soma + 2.20
    elif codigo == '106':
        Anotacao.append('Refrigerante')
        print(Anotacao)
        soma = soma + 1.00
    elif codigo == '0':
        print('Pedido finalizado')
        print(Anotacao)
        print(f'O total e R${soma:.2f}')
        break
    else:
        print('Codigo invalido')
        