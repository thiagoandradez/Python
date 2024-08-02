from random import randint

computador = randint(0,5)
usuario = int(input('Digite um valor entre 0 e 5 :'))

if usuario == computador :
    print('Você acertou!')
else:
    print('Voce errou!')


print(f'O numero que o computador escolheu foi {computador}')
print(f'O número que o usuario escolheu foi {usuario}')