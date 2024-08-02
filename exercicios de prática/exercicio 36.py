valor_casa = float(input('Digite o valor da casa:'))
salario = float(input('Digite o seu salário : '))
anos = int(input('Digite em quantos anos você irá pagar : '))
prestacao = valor_casa / (anos * 12)
minimo = salario * 30 / 100

print(F'O valor da sua casa é de R${valor_casa:.2f} e o seu salário é de R${salario:.2f}')
print(f'A sua prestação deverá ser de R${prestacao:.2f}')
print(f'30% do seu salário é de R${minimo:.2f}')

if prestacao <= minimo:
    print('Empréstimo concedido! seus dados são aceitos para o empréstimo.')
else:
    print('''Empréstimo negado! seus dados não são aceitos para o empréstimo, ele não pode execeder 30% do seu salário''')
