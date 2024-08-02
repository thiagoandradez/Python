nome = str(input('Digite seu nome : '))
idade = int(input('Digite a sua idade :'))

if idade <= 9:
    print(f'Olá {nome} a sua idade é igual a {idade} e voce é da categoria Mirim')

elif idade > 9 and idade <= 14:
    print(f'Olá {nome} a sua idade é igual a {idade} e voce é da categoria infantil')

elif idade > 9 and idade <= 19:
    print((f'Olá {nome} a sua idade é igual a {idade} e voce é da categoria junior'))

elif idade > 9 and idade <= 25:
    print(f'Olá {nome} a sua idade é igual a {idade} e voce é da categoria Senior')

elif idade > 25:
   print(f'Olá {nome} a sua idade é igual a {idade} e voce é da categoria master')
