#-*- coding: utf-8 -*-
from PySimpleGUI import (
    Input, Window, Button,
    Frame, Text, theme,
    Column, Push, popup,
    WIN_CLOSED, popup_no_buttons
)


def marcha_carro():
    theme('BluePurple')

    layout = [
        [
            Text(text='Velocidade em km/h')
        ],

        [
            Input(key='-VEL-',
                  size=(25, 1),
                  justification='center'),

            Button(button_text='Testar',
                   target='-VEL-',
                   key='-BVEL-')
        ]
    ]

    layout = [
        [
            Frame(title='Simulação',
                  layout=layout)
        ]
    ]
    return Window(title='',
                  layout=layout,
                  finalize=True)


janela = marcha_carro()

while True:
    evento, valor = janela.read()
    if evento == WIN_CLOSED:
        break
    if '-BVEL-' in evento:
        num = valor['-VEL-']
        # ----------------------------
        # Validação da variável
        #----------------------------
        if not num.isdigit():
            popup('Valor inválido.')
        else:
            num = int(num)
            # ----------------------------
            # Condições para a troca
            # ----------------------------
            if num == 0:
                popup_no_buttons(image='marcha.png')
            if num in range(1, 21):
                popup_no_buttons(image='marcha_1.png')
            if num in range(21, 41):
                popup_no_buttons(image='marcha_2.png')
            if num in range(41, 51):
                popup_no_buttons(image='marcha_3.png')
            if num in range(51, 61):
                popup_no_buttons(image='marcha_4.png')
            if num > 60:
                popup_no_buttons(image='marcha_5.png')
        janela['-VEL-'].update('')
janela.close()