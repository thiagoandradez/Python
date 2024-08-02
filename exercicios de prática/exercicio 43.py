nome = str(input('Digite seu nome = '))
peso = float(input('Digite o seu peso = '))
altura = float(input('Digite a sua altura = '))
imc = peso / (altura**2)
print(f'Olá {nome}, seu peso é de Kg {peso}, e sua altura de {altura}m! o seu imc conforme esses dados é de IMC = {imc:.1f}')

if imc < 18.5:
    print('Você está abaixo do peso!')

elif imc >= 40:
    print('Você está em obesidade mórbida.')

elif imc <= 18.5 and imc < 25:
    print('Voce está em peso ideal!')

elif imc <= 25 and imc < 30:
    print('Voce está em sobrepeso!')

elif imc <= 30 and imc < 40:
    print('Voce está em obesidade!')
