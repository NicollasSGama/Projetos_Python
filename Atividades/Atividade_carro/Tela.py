#-*- coding: utf-8 -*-
from PySimpleGUI import (
    Input, Window, Button,
    Frame, Text, theme,
    Column, Push, popup,
    WIN_CLOSED
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
        num = int(num)
        if num == 0:
            popup('Neutro')
        if num <= 20:
            popup('1° Marcha')
        if 20 > num >= 40:
            popup('2° Marcha')
        if 40 > num >= 50:
            popup('3° Marcha')
        if 50 > num >= 60:
            popup('4° Marcha')
        if num > 60:
            popup('5° Marcha')
        else:
            popup('Valor inválido')
    janela['-VEL-'].update('')
janela.close()