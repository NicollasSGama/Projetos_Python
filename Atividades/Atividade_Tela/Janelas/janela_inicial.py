from PySimpleGUI import (
    Text, Input, Table,
    Button, Window, HSeparator,
    VSeparator, theme, Frame,
    Column, Push, popup,
    WIN_CLOSED
)
from Atividades.Atividade_Tela.Variaveis.variaveis import *
from Atividades.Atividade_Tela.Funcoes.funcoes import *
def janela_atividade():
    theme(tema)

    tabela = ['Nome',
              'Sobrenome',
              'E-mail'
              ]

    layout_esquerdo = [
        [
            Text('Nome')
        ],

        [
            Input(key='-NOME-')
        ],

        [
            Text('Sobrenome')
        ],

        [
            Input(key='-SOBRENOME-')
        ],

        [
            Text('E-mail')
        ],

        [
            Input(key='-EMAIL-')
        ],

        [
            Text('Senha')
        ],

        [
            Input(key='-SENHA-',
                  password_char='*'
                  )
        ],
    ]

    layout_baixo = [
        [
            Table(headings=tabela,
                  values=[],
                  key='-TABELA-'
                  )
        ],
    ]

    layout_botao = [
        [
            Button('FECHAR',
                   key='-FECHAR-'
                   ),

            Push(),

            Button('REGISTRAR',
                   key='-REGISTRAR-'
                   )
        ]
    ]

    layout_esquerdo_direito = [
        [
            Column(layout_esquerdo),

            VSeparator(),

            Column(layout_baixo)
        ]
    ]

    layout = [
        [
            Frame('CADASTRO',
                  layout_esquerdo_direito
                  )
        ],

        [
            layout_botao
        ]
    ]

    return Window('ATIVIDADE',
                  layout
                  )


janela = janela_atividade()

while True:
    eventos, valores = janela.read()
    match eventos:
        case '-REGISTRAR-':
            nome = valores['-NOME-']
            sobrenome = valores['-SOBRENOME-']
            email = valores['-EMAIL-']
            senha = valores['-SENHA-']
            # ------------------
            # Salvar os arquivos
            # em '.txt'
            #------------------
            with open('salvar.txt', 'a+') as arquivo:
                arquivo.write(f'{nome} {sobrenome} {email} {senha}\n')
                popup('REGISTRO REALIZADO!')
            # ------------------
            # Atualizar os dados
            # da tabela
            # ------------------
            janela['-TABELA-'].update(values=ler_txt())
        case '-FECHAR-':
            break
        case WIN_CLOSED:
            break
janela.close()