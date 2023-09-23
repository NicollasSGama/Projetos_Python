# -------------------------------------------
# CEP
# -------------------------------------------
import json
import requests


def obterCEP(cep):
    url = 'https://viacep.com.br/ws/{}/json/'.format(cep)
    requisicao = requests.get(url)
    endereco = json.loads(requisicao.content)
    return endereco
# -------------------------------------------

cep = input('Digite o CEP: ')
print(obterCEP(cep))
