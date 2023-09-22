#-*- coding: utf-8 -*-
import PySimpleGUI as sg
from Variavel import *
from Logica import *
def janelaCadastro():
    layout=[
        [
            sg.Image('img/logoAPP.png'), sg.Push(), sg.Text('CONTATO'), sg.Push()
        ],

        [
            sg.HSep()
        ],

        [
            sg.Text('E-mail'), sg.Input(),
            sg.Text('Telefone'), sg.Input()
        ],

        [
            sg.HSep()
        ],

        [
            sg.Text('Rua'), sg.Input(),
            sg.Text('Número'), sg.Input(),
            sg.Text('CEP'), sg.Input(), sg.Button('Buscar')
        ],

        [
            sg.Text('Bairro'), sg.Input(),
            sg.Text('Cidade'), sg.Input(),
            sg.Text('Estado'), sg.Input()
        ],

        [
            sg.Push(), sg.Button('Voltar'), sg.Button('Cadastrar'), sg.Push()
        ],
    ]
    return sg.Window('Cadastrar',layout)

janelaCadastro().read()