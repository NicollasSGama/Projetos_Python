from PySimpleGUI import (
    Text, Input, Table,
    Button, Window, HSeparator,
    VSeparator, theme, Frame,
    Column, Push
)
from Atividades.Atividade_Tela.Variaveis.variaveis import *
from Atividades.Atividade_Tela.Funcoes.funcoes import *
def janela_atividade():
    theme(tema)

    cadastro = ['Nome',
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

        # [
        #     HSeparator()
        # ]
    ]

    layout_direito = [
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

        # [
        #     HSeparator()
        # ]
    ]

    layout_baixo = [
        [
            Table(headings=cadastro,
                  values=[],
                  key='-TABELA-'
                  )
        ],

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

            Column(layout_direito)
        ]
    ]

    layout = [
        [
            Frame('CADASTRO',
                  layout_esquerdo_direito
                  )
        ],

        [
            Frame('LISTAR',
                  layout_baixo
                  )
        ]
    ]

    return Window('ATIVIDADE',
                  layout
                  )


janela = janela_atividade()
janela.read()