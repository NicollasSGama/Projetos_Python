#-------------------------------------------
# CEP
#-------------------------------------------
import json
import requests

cep = input('Digite o CEP: ')
def obterCEP():
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    data = json.loads(resposta.content)
    return data
    # if resposta.status_code == 200:
    #    data = json.loads(resposta.content)
    #    print('CEP: ', data['cep'])
    #    print('Logradouro: ', data['logradouro'])
    #    print('Complemento: ', data['complemento'])
    #    print('Bairro: ', data['bairro'])
    #    print('Cidade: ', data['localidade'])
    #    print('Estado: ', data['uf'])
    # else:
    #     print('Não foi possível obter informações do CEP informado.')
    # return
# -------------------------------------------
print(obterCEP())