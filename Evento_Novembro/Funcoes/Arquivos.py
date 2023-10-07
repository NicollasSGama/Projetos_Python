def ler_txt():
    with open('requisicao.txt', 'r+') as arquivos:
        lista = list()
        for linha in arquivos:
            linha.replace('\n', '')
            arquivo = linha.split(' ')
            lista.append(arquivo)
        return lista


def requistadas_txt():
    with open('requisitadas.txt', 'r+') as arquivos:
        lista = list()
        for linha in arquivos:
            linha.replace('\n', '')
            arquivo = linha.split(' ')
            lista.append(arquivo)
        return lista


def concluidas_txt():
    with open('concluidas.txt', 'r+') as arquivos:
        lista = list()
        for linha in arquivos:
            linha.replace('\n', '')
            arquivo = linha.split(' ')
            lista.append(arquivo)
        return lista


def historico_txt():
    with open('historico.txt', 'r+') as arquivos:
        lista = list()
        for linha in arquivos:
            linha.replace('\n', '')
            arquivo = linha.split(' ')
            lista.append(arquivo)
        return lista
