#-*- coding: utf-8 -*-
import PySimpleGUI as sg
import json
def janelaLogin():
    layout=[
        [sg.Push(background_color="#2F6073"),sg.Image("img/FundoImagem.png",background_color="#2F6073"),sg.Push(background_color="#2F6073")],
        [sg.Image("img/dentro.png",background_color="#2F6073"),sg.Text("Login",size=7,background_color="#2F6073",text_color="#FFFFFF",font=" roboto 20" ),sg.Input(size=20,background_color="#FFFFFF",font=" roboto 15", key="-LOGIN-")],
        [sg.Image("img/seguro.png",background_color="#2F6073"),sg.Text("Senha",size=7,background_color="#2F6073",text_color="#FFFFFF", font=" roboto 20"),sg.Input(size=20,background_color="#FFFFFF",font=" roboto 15",password_char="*",key="-SENHA-" )],
        [sg.Push(background_color="#2F6073"),sg.Button("Entrar",size=10,font="arial 15",pad=25,mouseover_colors=("#FFFFFF","#FFE054"),button_color="#5AADBF",key="-BOTAO-"),sg.Push(background_color="#2F6073")],
        [sg.Push(background_color="#2F6073"),sg.Text("Recuperar Senha!",background_color="#2F6073",text_color="#5AADBF", font=("Helvetica",12), enable_events=True, key="-CREATE_USER-"),sg.Push(background_color="#2F6073")]
    ]
    return sg.Window("Login",layout,background_color="#2F6073")

def janelaRecuperarSenha():
    layout=[
        [sg.Push(background_color="#2F6073"),sg.Image("img/mudarSenha.png",background_color="#2F6073"),sg.Push(background_color="#2F6073")],
        [sg.Text("Entre com o seu CPF",size=18,text_color="#FFFFFF", font=("Helvetica",12), background_color="#2F6073"), sg.Input(key="-CPF-",size=20,background_color="#FFFFFF",font="Helvetica 15",)],
        [sg.Button("Recuperar Senha",size=15,font="arial 15",pad=8,mouseover_colors=("#FFFFFF","#FFE054"),button_color="#5AADBF"), sg.Text("",visible=False,background_color="#2F6073",text_color="#5AADBF")]
    ]
    return sg.Window("Recuperar Senha", layout,background_color="#2F6073")

def janelaCadastrarFuncionario():
    lista = ['Gerente', 'Administrativo', 'Operacional']
    valor =[[[]]]
    # arquivo = {"item 1": [{"name": "title 1"}, {"name": "title 2"}], "item 2": [{"name": "title 3"}, {"name": "title 4"}]}
    # lista = json.dumps(arquivo)

    layout = [
        [
        sg.Image("img/logoAPP.png",background_color="#2F6073"),sg.Push(background_color="#2F6073"),sg.Text("CADASTRAR FUNCIONARIO",background_color="#2F6073",font=("Helvetica ",17,"bold")),sg.Push(background_color="#2F6073")
        ],

        [
        sg.HSep()
        ],

        [
         sg.Text("Nome",background_color="#2F6073",font="arial 15",size=5), sg.Input(size=(70,50),background_color="#FFFFFF",font="arial 15"),
         sg.Text("Nascimento",background_color="#2F6073",font="arial 15",size=10), sg.Input(size=(20,10),background_color="#FFFFFF",font="arial 15"),
         sg.Image("img/calendar.png",background_color="#2F6073")
        ],

        [
         sg.Text('CPF', background_color="#2F6073",font="arial 15",size=5), sg.Input(size=(20,10),background_color="#FFFFFF",font="arial 15"),
         sg.Text("Cargo", background_color="#2F6073", font="arial 15",size=5), sg.Combo(lista, size=(20,10), font="arial 15"),
         sg.Text('Cadastrar Contato', background_color="#2F6073",font="arial 15",size=15), sg.Image('img/contato.png',background_color="#2F6073")
        ],

        [
         sg.Text('Senha', background_color="#2F6073",font="arial 15",size=5), sg.Input(size=(20,10),background_color="#FFFFFF",font="arial 15", password_char='*'),
         sg.Text("Nível", background_color="#2F6073", font="arial 15", size=5),
         sg.Radio('ADM','radio1', background_color="#2F6073",font="arial 15"), sg.Radio('COMUM','radio1',True, background_color="#2F6073",font="arial 15"),
         sg.Push(background_color="#2F6073"), sg.Button('Cadastrar', font="arial 15"), sg.Push(background_color="#2F6073")
        ],

        [
            sg.Table(valor, headings=lista)
        ],
    ]
    return sg.Window("Cadastro",layout,resizable=True,background_color="#2F6073")

janelaRecuperarSenha().read()