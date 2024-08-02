funcionario = str(input('Digite o seu nome :'))
salario = float(input('Digite o seu salário : '))
novo = salario + (salario * 15 / 100)
print(f'Olá {funcionario}, o seu salário de R${
      salario} com um reajuste salarial de 15% terá um novo valor a ser recebido de R${novo}')
