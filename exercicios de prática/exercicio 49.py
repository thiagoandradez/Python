while True:
    numero = int(input('Digite um número :'))
    for c in range(1, 11):
        print(f'{numero} x {c} = {numero*c}')
        
    resp = input('Deseja continuar ? [S/N]').upper().strip()
    if resp in 'S':
        pass
    else: 
        print('Voce escolheu Sair do programa!')
        break
