import random

aluno1 = str(input('Digite o nome do Aluno 1 :'))
aluno2 = str(input('Digite o nome do Aluno 2 :'))
aluno3 = str(input('Digite o nome do Aluno 3 :'))
aluno4 = str(input('Digite o nome do Aluno 4 :'))

sorteio = random.randint(1, 4)

print(f'Temos 4 alunos, dentre eles {aluno1},{aluno2},{aluno3},{aluno4}. O professor sorteou um deles para apagar o quadro e o número sorteado dessa vez será {sorteio}')
