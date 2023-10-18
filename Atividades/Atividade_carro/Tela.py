from PySimpleGUI import (
    Input, Window, Button,
    Frame, Text, theme,
    Column, Push, popup,
    WIN_CLOSED
)


def marcha_carro():
    theme('Blue')

    layout = [
        [
            Text(text='Velocidade atual')
        ],

        [
            Input(key='velocidade'),

            Button(target='velocidade')
        ]
    ]

    layout = [
        [
            Frame(title='Teste',
                  layout=layout)
        ]
    ]
    return Window(title='',
                  layout=layout,
                  finalize=True)


janela = marcha_carro()

while True:
    evento, valor = janela.read()
    if WIN_CLOSED:
        break

janela.close()