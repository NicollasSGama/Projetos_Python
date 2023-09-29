def ler_txt():
    with open('salvar.txt', 'r+') as arquivos:
        lista = list()
        for linha in arquivos:
            linha.replace('\n', '')
            arquivo = linha.split(' ')
            lista.append(arquivo)
        return lista
