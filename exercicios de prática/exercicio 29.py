velocidade = float(input('Digite a velocidade do veiculo : '))
if velocidade > 80 :
    multa=velocidade * 7
    print('Você passou do limite de velocidade, voce foi multado!')
    print('A multa será de R$ 7,00 por cada Km acima desse limite.')
    print(f'A sua multa conforme a sua velocidade de: {velocidade}Km/h é de R${multa}!')
else:
    print('Voce está dentro da velocidade!')