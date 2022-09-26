from auxClassAtor import Ator

class Atua:
    def __init__(self, atua:str):
        self.atua = atua

    def ver(self):
        return f'{self.atua}, {self.puxar()}'

    def puxar(self, ator):
        nome_ator = Ator(ator).ver()
        return nome_ator
