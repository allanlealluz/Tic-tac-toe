import PySimpleGUI as py
linha = []
py.theme('dark')
layout = [
    [py.Button('',key='botao1',button_color='gray'),py.Text('',key='1'),py.Button('',key='botao2',button_color='gray'),py.Text('',key='2'),py.Button('',key='botao3',button_color='gray'),py.Text('',key='3')],
    [py.Button('',key='botao4',button_color='gray'),py.Text('',key='4'),py.Button('',key='botao5',button_color='gray'),py.Text('',key='5'),py.Button('',key='botao6',button_color='gray'),py.Text('',key='6')],
    [py.Button('',key='botao7',button_color='gray'),py.Text('',key='7'),py.Button('',key='botao8',button_color='gray'),py.Text('',key='8'),py.Button('',key='botao9',button_color='gray'),py.Text('',key='9')]
]
janela = py.Window('TesteElemtnos',layout)
jogador = 1
while True:
    eventos,valores = janela._read()
    if eventos == py.WINDOW_CLOSED:
        break
    for c in range(1,10):
        analise = 'botao'+f'{c}'
        if eventos == analise:
            if jogador == 1:
                janela[f'{c}'].update('x')
                janela[f'{analise}'].update(disabled=True)
            else:
                janela[f'{c}'].update('o')
                janela[f'{analise}'].update(disabled=True)
    if jogador == 1:
        valor = 'x'
    else:
        valor = 'o'
    if janela['1'].get() == valor and janela['2'].get() == valor and janela['3'].get() == valor:
        print('Jogador 1 Ganhou'if jogador == 1  else 'Jogador 2 Ganhou')
        break
    if janela['4'].get() == valor and janela['5'].get() == valor and janela['6'].get() == valor:
        print('Jogador 1 Ganhou'if jogador == 1  else 'Jogador 2 Ganhou')
        break
    if janela['7'].get() == valor and janela['8'].get() == valor and janela['9'].get() == valor:
        print('Jogador 1 Ganhou'if jogador == 1  else 'Jogador 2 Ganhou')
        break
    if janela['1'].get() == valor and janela['4'].get() == valor and janela['7'].get() == valor:
        print('Jogador 1 Ganhou'if jogador == 1  else 'Jogador 2 Ganhou')
        break
    if janela['2'].get() == valor and janela['5'].get() == valor and janela['8'].get() == valor:
        print('Jogador 1 Ganhou'if jogador == 1  else 'Jogador 2 Ganhou')
        break
    if janela['3'].get() == valor and janela['6'].get() == valor and janela['9'].get() == valor:
        print('Jogador 1 Ganhou'if jogador == 1  else 'Jogador 2 Ganhou')
        break
    if janela['1'].get() == valor and janela['5'].get() == valor and janela['9'].get() == valor:
        print('Jogador 1 Ganhou'if jogador == 1  else 'Jogador 2 Ganhou')
        break
    if janela['3'].get() == valor and janela['5'].get() == valor and janela['1'].get() == valor:
        print('Jogador 1 Ganhou'if jogador == 1  else 'Jogador 2 Ganhou')
        break
    if jogador == 2:
        jogador -= 1
    elif jogador == 1:
        jogador += 1

