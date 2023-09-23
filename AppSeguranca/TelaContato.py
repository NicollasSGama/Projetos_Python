#-*- coding: utf-8 -*-
import PySimpleGUI as sg
from Variavel import *
def janelaContato():
    layout = [
        [
            sg.Image('img/logoAPP.png', background_color=corFundo),
            sg.Push(background_color=corFundo),
            sg.Text('CONTATO', background_color=corFundo, font=fonteTitulo, text_color=corTexto),
            sg.Push(background_color=corFundo)
        ],

        [
            sg.HSep()
        ],

        [
            sg.Text('E-mail', background_color=corFundo, font=fonteTitulo, text_color=corTexto),
            sg.Input(size=tamanhoEntrada, background_color=corFundoBranco, font=fonteTexto, key='-EMAIL-'),
            sg.Text('Telefone', background_color=corFundo, font=fonteTitulo, text_color=corTexto),
            sg.Input(size=tamanhoEntradaP, background_color=corFundoBranco, font=fonteTexto, key='-TEL-')
        ],

        [
            sg.HSep()
        ],

        [
            sg.Text('Rua', background_color=corFundo, font=fonteTitulo, text_color=corTexto),
            sg.Input(size=tamanhoEntrada, background_color=corFundoBranco, font=fonteTexto, key='-RUA-'),
            sg.Text('Número', background_color=corFundo, font=fonteTitulo, text_color=corTexto),
            sg.Input(size=tamanhoEntrada, background_color=corFundoBranco, font=fonteTexto, key='-NUM-'),
            sg.Text('CEP', background_color=corFundo, font=fonteTitulo, text_color=corTexto),
            sg.Input(size=tamanhoEntrada, background_color=corFundoBranco, font=fonteTexto, key='-CEP-'),
            sg.Button('Buscar', font=fonteTexto)
        ],

        [
            sg.Text('Bairro', background_color=corFundo, font=fonteTitulo, text_color=corTexto),
            sg.Input(size=tamanhoEntrada, background_color=corFundoBranco, font=fonteTexto, key='-BAI-'),
            sg.Text('Cidade', background_color=corFundo, font=fonteTitulo, text_color=corTexto),
            sg.Input(size=tamanhoEntrada, background_color=corFundoBranco, font=fonteTexto, key='-CID-'),
            sg.Text('Estado', background_color=corFundo, font=fonteTitulo, text_color=corTexto),
            sg.Input(size=tamanhoEntrada, background_color=corFundoBranco, font=fonteTexto, key='-EST-')
        ],

        [
            sg.Push(background_color=corFundo),
            sg.Button('Voltar', font=fonteTexto),
            sg.Button('Cadastrar', font=fonteTexto),
            sg.Push(background_color=corFundo)
        ],
    ]
    return sg.Window('Cadastrar', layout, background_color=corFundo, resizable=True)

janelaContato().read()