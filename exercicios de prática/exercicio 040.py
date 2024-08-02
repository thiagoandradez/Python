nome = str(input("Digite seu nome : "))
nota1 = float(input('Digite a sua primeira nota : '))
nota2 = float(input('Digite a sua segunda nota : '))
media = (nota1 + nota2) / 2

if media < 5:
    print(f'Olá {nome}, infelizmente você foi reprovado! sua primeira nota é {nota1} e a sua segunda nota é {
          nota2} tendo uma média de {media}. A nota para ser aprovado é 5! , se esforçe mais da próxima vez. ')

elif media == 5 and media <= 6.9:
    print(f'Olá {nome}, infelizmente você está de recuperação, sua primeira nota é {nota1} e a sua segunda nota é {nota2} tendo uma média de {media}. A nota para ser aprovado é 5! , se esforçe mais da próxima vez. ')

elif media >= 7:
    print(f'Olá {nome}, parabéns voce foi aprovado! sua primeira nota é {nota1} e a sua segunda nota é {nota2} tendo uma média de {media}. A nota para ser aprovado é 5! , continue assim. ')
