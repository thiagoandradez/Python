numericos = []
alfabeticos = []
maisculas = []
minusculos = []
espacos = []


usuario = input('Digite algo:')
resposta1 = input('Qual é o tipo primitivo desse valor : ')
if resposta1 in '''float''' and '''int''':
    numericos.append(resposta1)
if resposta1 in '''str''':
    alfabeticos.append(resposta1)


resposta2 = input('tem espaços? :')
if resposta2 in 'Ss':
    espacos.append(resposta2)
else:
    pass
if resposta2 in espacos:
    print('É verdadeiro, tem espaços !')
else:
    print('É falso, não tem espaços!')

respota3 = input('É um numero? :')
if respota3 in 'Ss':
    numericos.append(respota3)
else:
    pass

if respota3 in numericos:
    print('É verdadeiro, é numerico!')
else:
    print('É falso, não é numérico!')

reposta4 = input('É alfabético ? :')
if reposta4 in 'Ss':
    alfabeticos.append(reposta4)
else:
    pass
if reposta4 in alfabeticos:
    print('Sim é alfabético')
else:
    print('Não é alfabético')

reposta6 = input('Está em maisculas? :')
if reposta6 in 'Ss':
    maisculas.append(reposta6)
else:
    pass
if reposta6 in maisculas:
    print('É maiscula')
else:
    print('Não é maiscula')

reposta7 = input('Está em minúsculo? :')
if reposta7 in 'Ss':
    minusculos.append(reposta7)
else:
    pass
if reposta7 in minusculos:
    print('É minusculo')
else:
    print('Não é minusculo')


print(numericos)
print(espacos)
print(maisculas)
print(minusculos)
print(alfabeticos)