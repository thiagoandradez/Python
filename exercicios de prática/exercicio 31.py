velocidade = float(input('Digite a distancia percorrida em Km/h :'))
if velocidade <= 200:
    preco_passagem = 0.50 * velocidade
    print(f'Voce deverá pagar R${preco_passagem} pela sua distancia percorrida de {velocidade}')
if velocidade > 200:
    preco_acima = 0.45 * velocidade
    print(f'Voce deverá pagar R${preco_acima} pela sua distancia percorrida de {velocidade}')

