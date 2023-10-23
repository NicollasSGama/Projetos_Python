from PySimpleGUI import (
    Text, Input, Button,
    Multiline, Canvas, popup,
    Table, CalendarButton,
    Window, WIN_CLOSED,
    popup_get_text, Frame,
    Column, Combo, Push,
    theme, VSeparator, VPush,
    HSeparator, Tab, TabGroup,
    popup_yes_no
)
from Evento_Novembro.Funcoes.Arquivos import *

tema = 'LightBlue2'

tabela_dados = [
    'Setor',
    'Requerente',
    'Problema',
    'Data',
    'Observações'
]

tabela_dados_responsavel = [
    'Setor',
    'Requerente',
    'Problema',
    'Data',
    'Observações',
    'Responsável'
]

tab2 = [
    [
        'Pendente'
    ]
]

tab3 = [
    [
        'Concluído'
    ]
]


def tabela():
    theme(tema)

    layout_tab = [[Tab(title='Pendentes',
                       layout=[
                           [
                               Table(values=ler_txt(),
                                     headings=tabela_dados,
                                     key='-TPENDENTES-',
                                     justification='center',
                                     def_col_width=15,
                                     auto_size_columns=False,
                                     enable_events=True,
                                     enable_click_events=True,
                                     expand_x=True,
                                     expand_y=True)
                           ],

                           [
                               Button(button_text='ATUALIZAR',
                                      key='-ATUALIZAR-'),
                               Push(),
                               Button(button_text='RESPONSÁVEL',
                                      key='-RESPONSAVEL-'),
                               Push(),
                               Button(button_text='REGISTRAR',
                                      key='-REGISTRAR-')
                           ]
                       ]
                       ),

                   Tab(title='Requisitadas',
                       layout=
                       [
                           [
                               Table(values=tab2,
                                     headings=tabela_dados_responsavel,
                                     key='-TREQUISITADAS-',
                                     justification='center',
                                     def_col_width=15,
                                     auto_size_columns=False,
                                     enable_events=True,
                                     expand_x=True,
                                     expand_y=True)
                           ]
                       ]
                       ),

                   Tab(title='Concluídas',
                       layout=
                       [
                           [
                               Table(values=tab3,
                                     headings=tabela_dados_responsavel,
                                     key='-TCONCLUIDAS-',
                                     justification='center',
                                     def_col_width=15,
                                     auto_size_columns=False,
                                     enable_events=True,
                                     expand_x=True,
                                     expand_y=True)
                           ]
                       ]
                       ),

                   Tab(title='Histórico',
                       layout=
                       [
                           [
                               Table(values=tab3,
                                     headings=tabela_dados_responsavel,
                                     key='THISTORICO',
                                     justification='center',
                                     def_col_width=15,
                                     auto_size_columns=False,
                                     enable_events=True,
                                     expand_x=True,
                                     expand_y=True)
                           ]
                       ]
                       )
                   ]
                  ]

    layout_tab_grupo = [
        [
            TabGroup(layout=layout_tab)
        ]
    ]

    layout = [
        [
            Frame(title='REQUISIÇÕES',
                  layout=layout_tab_grupo)
        ]
    ]

    return Window(title='Nada',
                  layout=layout)


janela = tabela()

while True:
    eventos, valores = janela.read()
    # if janela['-TPENDENTES-'] in eventos:
    if '+CLICKED+' in eventos:
        valor = eventos[2][0]
        if valor == -1 or None:
            None
        if valor in range(0, 9999):
            if valor == 0:
                pass
            print(valor)

    if '-REGISTRAR-' in eventos:
        popup_yes_no('REGISTRAR?')
        # if 'Nada':
        #     popup('Entrou')
        # if 'No':
        #     None

    if eventos == '-ATUALIZAR-':
        janela['-TPENDENTES-'].update(values=ler_txt())

    if eventos == WIN_CLOSED:
        break

janela.close()
