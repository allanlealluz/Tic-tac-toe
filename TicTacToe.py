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
    for valor in matriz:
        print(f'{valor}')
    linha = int(input('Escolha uma linha de 1 a 3'))
    coluna = int(input('Escolha uma coluna de 1 a 3'))
    matriz[linha-1][coluna-1] = 'o'
    for valor in matriz:
        print(f'{valor}')
        if valor.count('o') == 3:
            print('Ganhou')
            ganhou = True
    for i in range(0,3):
        colunas.append(matriz[0][i])
        colunas.append(matriz[1][i])
        colunas.append(matriz[2][i])
        if colunas.count('o') == 3:
            print('ganhou')
            ganhou = True
        else:
           colunas.clear()
        diagonal1 = []
        diagonal1.append(matriz[0][0])
        diagonal1.append(matriz[1][1])
        diagonal1.append(matriz[2][2])
        diagonal2 = []
        diagonal2.append(matriz[0][2])
        diagonal2.append(matriz[1][1])
        diagonal2.append(matriz[2][0])
        if diagonal1.count('x') == 3 or diagonal2.count('x') == 3:
            print('ganhou')
            ganhou = True
        diagonal1.clear()
        diagonal2.clear()

