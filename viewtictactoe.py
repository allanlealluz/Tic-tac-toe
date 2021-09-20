import PySimpleGUI as py
linha1 = []
linha2 = []
soma = 0
py.theme('reddit')
layout = [
    [py.Button(' ',key='1'),py.Button(' ',key='2'), py.Button(' ',key='3')],
    [py.Button(' ',key='4'),py.Button(' ',key='5'), py.Button(' ',key='6')],
    [py.Button(' ',key='7'),py.Button(' ',key='8'), py.Button(' ',key='9')]
]
janela = py.Window('Tic Tac Toe',layout)
jogador = 1
while True:
    eventos,valores = janela.read()
    if eventos == py.WINDOW_CLOSED:
        break
    if eventos != '':
       if int(jogador) == 1:
           janela[eventos[0]].update('o')
           linha1.append(eventos[0])
           jogador += 1
           if len(linha1) > 3:
               linha1 = sorted(linha1)
               ultv = [linha1[-1], linha1[-2], linha1[-3]]
               print(f'hello eu sou jogador 1 e eu tirei {ultv}')
               for value in ultv:
                   soma += int(value)
           else:
               for value in linha1:
                   soma += int(value)
           print(f'a soma é {soma}')
           if soma == 6 and len(linha1) == 3 or len(linha1) > 3:
               print('jogador 1 ganhou linha 1')
               break
           elif soma == 12 and len(linha1) == 3 or len(linha1) > 3:
               print('jogador 1 ganhou coluna 1')
               break
           elif soma == 15 and len(linha1) == 3 or len(linha1) > 3:
               print('jogador 1 ganhou linha 2 ou coluna 2 ou diagonal 1 e 2')
               break
           elif soma == 18 and len(linha1) == 3 or len(linha1) > 3:
               print('jogador 1 ganhou coluna 3')
               break
           elif soma == 24 and len(linha1) == 3 or len(linha1) > 3:
               print('jogador 1 ganhou linha 3')

           soma = 0
       elif int(jogador) == 2:
            janela[eventos[0]].update('x')
            linha2.append(eventos[0])
            jogador -= 1
            if len(linha2) > 3:
                linha2 = sorted(linha2)
                ultvt = [linha2[-1],linha2[-2],linha2[-3]]
                print(f'hello jogador 2 {ultvt}')
                for value in ultvt:
                    soma += int(value)
                    print(value)
            else:
                for value in linha2:
                    soma += int(value)
                    print(value)
            print(f'a soma do jogador 2 é {soma}')
            if soma == 6 and len(linha2) == 3 or len(linha2) > 3:
                print('O jogador 2 Ganhou')
                break
            elif soma == 12 and len(linha2) == 3 or len(linha2) > 3:
                print('O jogador 2 Ganhou')
                break
            elif soma == 15 and len(linha2) == 3 or len(linha2) > 3:
                print('O jogador 2 Ganhou')
                break
            elif soma == 18 and len(linha2) == 3 or len(linha2) > 3:
                print('O jogador 2 Ganhou')
                break
            elif soma == 24 and len(linha2) == 3 or len(linha2) > 3:
                print('O jogador 2 Ganhou')
                break
            soma = 0








       




