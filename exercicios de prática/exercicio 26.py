frase = str(input('Digite uma frase: ')).upper()
print(f'A letra ''A'' aparece na sua frase {} vezes'.format(frase.count('A')))
print(f'A letra ''A'' aparece na {} vez na sua frase'.format(frase.find('A')+1))
print('A letra ''A'' aparece na {} ultima vez na sua frase'.format(frase.rfind('A')+1))