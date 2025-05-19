# Exercicio 9
salario = float(input('Digite o salario: '))
emprestimo = float(input('Digite o valor do emprestimo: '))

if emprestimo > (salario*0.2):
    print('emprestimo nao concedido')
elif emprestimo <= (salario*0.2):
    print('emprestimo concedido')