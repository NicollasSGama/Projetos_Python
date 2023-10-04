from PySimpleGUI import (
    Text, Input, Button,
    Multiline, Canvas,
    Table, CalendarButton,
    Window, WIN_CLOSED,
    popup_get_text, Frame,
    Column, Combo, Push,
    theme, VSeparator,
    HSeparator
)

tema = 'LightBlue2'
def tela_requisicao():
    theme(tema)

    setor = [
        [
            'Sala-Professor'
        ],

        [
            'Sala-Funcionário'
        ]
    ]

    problema = [
        [
            'Computador'
        ],

        [
            'Limpeza'
        ]
    ]

    professor = [
        [
            'Rogério'
        ],

        [
            'André'
        ]
    ]

    layout_esquerdo = [
        [
            Text('Setor')
        ],

        [
            Combo(setor,
                  size=(21, 1))
        ],

        [
            Text('Professor')
        ],

        [
            Combo(professor,
                  key=,
                  size=(21, 1))
        ],

        [
            HSeparator()
        ],

        [
            Button('FECHAR')
        ]

    ]

    layout_direito = [
        [
            Text('Problema')
        ],

        [
            Combo(problema,
                  size=(21, 1))
        ],

        [
            Text('Data')
        ],

        [
            Input(readonly=True,
                  key='-DATA-',
                  size=(15, 1)),

            CalendarButton('DATA',
                           default_date_m_d_y=(1, 1, 2023),
                           format='%d/%m/%Y',
                           close_when_date_chosen=False,
                           target='-DATA-'
                           )
        ],

        [
            HSeparator()
        ],

        [
            Push(),
            Button('REQUISITAR')
        ]
    ]

    layout = [
        [
            Column(layout_esquerdo),
            VSeparator(),
            Column(layout_direito)
        ]
    ]

    layout = [
        [
            Frame('REQUISITAR',
                  layout)
        ]
    ]


    return Window('',
                  layout)

janela = tela_requisicao()
janela.read()