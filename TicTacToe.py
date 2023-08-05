matriz = [[' ']*3 for _ in range(3)]
ganhou = False

while not ganhou:
    print('Jogador 1')
    
    for linha in matriz:
        print(' '.join(linha))
        
    linha = int(input('Escolha uma linha de 1 a 3: '))
    coluna = int(input('Escolha uma coluna de 1 a 3: '))
    
    matriz[linha-1][coluna-1] = 'x'
    
    for linha in matriz:
        if linha.count('x') == 3:
            print('Ganhou')
            ganhou = True
            break
    
    for i in range(3):
        coluna = [matriz[j][i] for j in range(3)]
        if coluna.count('x') == 3:
            print('Ganhou')
            ganhou = True
            break
    
    diagonal1 = [matriz[i][i] for i in range(3)]
    diagonal2 = [matriz[i][2-i] for i in range(3)]
    
    if diagonal1.count('x') == 3 or diagonal2.count('x') == 3:
        print('Ganhou')
        ganhou = True
        
    if ganhou:
        break
    
    print('-'*30)
    
    print('Jogador 2')
    
    for linha in matriz:
        print(' '.join(linha))
        
    linha = int(input('Escolha uma linha de 1 a 3: '))
    coluna = int(input('Escolha uma coluna de 1 a 3: '))
    
    matriz[linha-1][coluna-1] = 'o'
    
    for linha in matriz:
        if linha.count('o') == 3:
            print('Ganhou')
            ganhou = True
            break
    
    for i in range(3):
        coluna = [matriz[j][i] for j in range(3)]
        if coluna.count('o') == 3:
            print('Ganhou')
            ganhou = True
            break
    
    diagonal1 = [matriz[i][i] for i in range(3)]
    diagonal2 = [matriz[i][2-i] for i in range(3)]
    
    if diagonal1.count('o') == 3 or diagonal2.count('o') == 3:
        print('Ganhou')
        ganhou = True
        
    if ganhou:
        break
    
    print('-'*30)
