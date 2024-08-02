nome = str(input('Digite seu nome:'))
carro = str(input('Digite o modelo do seu carro alugado :'))
kmp = float(input('Digite a quantidade de KM percorridos :'))
dia = int(input('Digite a quantidade de dias:'))
diaria = dia * 60
kmr = kmp * 0.15
print(f'Olá {nome}! o seu carro do modelo {carro}, com a sua KM fornecida de {kmp} e seus dias usados no total de {dia}. Você terá de pagar um valor de R${diaria} pela a diária e R${kmr} pelos seus km rodados')

# calcule o preço a pagar sabendo que o carro custa 60 reais por dia a cada 0.15 km rodado
# diaria do carro - 60 reais
# pagamento por km - 0.15 reais por cada KM rodado
