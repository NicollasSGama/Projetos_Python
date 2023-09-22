#-*- coding: latin-1 -*-
import PySimpleGUI as sg
fonte = ('arial', 10, 'bold')
def janelaLogin():
    layout=[
        [sg.Push(background_color="#2F6073"),sg.Image("img/FundoImagem.png",background_color="#2F6073"),sg.Push(background_color="#2F6073")],
        [sg.Image("img/dentro.png",background_color="#2F6073"),sg.Text("Login",size=7,background_color="#2F6073",text_color="#FFFFFF",font= fonte ),sg.Input(size=20,background_color="#FFFFFF",font=" roboto 15", key="-LOGIN-")],
        [sg.Image("img/seguro.png",background_color="#2F6073"),sg.Text("Senha",size=7,background_color="#2F6073",text_color="#FFFFFF", font=fonte),sg.Input(size=20,background_color="#FFFFFF",font=" roboto 15",password_char="*",key="-SENHA-" )],
        [sg.Push(background_color="#2F6073"),sg.Button("Entrar",size=10,font="arial 15",pad=25,mouseover_colors=("#FFFFFF","#FFE054"),button_color="#E8BF58",key="-BOTAO-"),sg.Push(background_color="#2F6073")],
        [sg.Push(background_color="#2F6073"),sg.Text("Recuperar Senha",background_color="#2F6073",text_color="#FFFFFF", font=("arial",12), enable_events=True, key="-CREATE_USER-"),sg.Push(background_color="#2F6073")]
    ]
    return sg.Window('Entrar', layout, background_color="#2F6073")
janelaLogin().read()

# def recuperarSenha()?
#     layout=[
#         [sg.Push(), sg.Text('Digite o usuário:', size=7), sg.InputText(size=20, key='-usrnm-'), sg.Push()],
#         [sg.Push()]
#
#     ]


def janelaCadastrarFuncionario():
    options=[
        ['Arquivo',['Salvar', 'Imprimir']],
        ['Usuário',['Cadastrar', 'Listar']],
        ['Ponto',['Bater Ponto', 'Relatório de Ponto']]
    ]
    layout=[
        [sg.Menubar(options, font=font)],
        [sg.Text('Conteúdo')]
    ]
    return sg.Window('Nada', layout, resizable=True)
janelaCadastrarFuncionario().read()