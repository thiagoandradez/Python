from datetime import date 

atual = date.today().year
nome = str(input('Digite o seu nome :'))
nasc = int(input('Digite o seu ano de nascimento :'))
idade = int(input('Digite a sua idade :'))

if idade > 18 :
    print(f'Ola {nome} como você nasceu em {nasc} e tem uma idade de {idade}, voce passou do tempo de alistamento!')

if idade == 18:
    print(f'Ola {nome} como você nasceu em {nasc} e tem uma idade de {idade}, está na hora de se alistasr!')

if idade  < 18 :
    print(f'Ola {nome} como você nasceu em {nasc} e tem uma idade de {idade}, está chegando o tempo de se alistar!')