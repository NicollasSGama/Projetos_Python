lista = [
    'nicolas@contato.com',
    'jose@contato.com',
    'ademar@senac.com'
]



lista_pronta = list()
def nada():
    for separar in lista:
        i = separar.split('@')
        lista_pronta.append(i)
    return lista_pronta


print(nada())