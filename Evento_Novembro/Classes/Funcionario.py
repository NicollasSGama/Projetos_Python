class Funcionario:
    def __init__(self, nome: str, setor: str):
        self.__nome = nome
        self.__setor = setor

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def setor(self):
        return self.__setor

    @setor.setter
    def setor(self, setor):
        self.__setor = setor

    def horario(self):  # Método para troca de horário dos funcionários
        pass