from datetime import date
from time import time
from classSessao.auxClassIngresso import *
from classSessao.database_controler import Database
from classSessao.auxSessao import Format

class Sessao:
    def __init__(self, dt_sessao: str, hor_sessao: time, status: int, val_inteira: float, val_meia: float):
        self.dt_sessao = dt_sessao
        self.hor_sessao = hor_sessao
        self.valor_inteira = val_inteira
        self.valor_meia = val_meia
        self.status = status
    
    def __str__(self):
        return f'Data da sessao: {self.dt_sessao},' \
               f'Hora da sessao: {self.hor_sessao}' \
               f'Valor inteira: {self.valor_inteira}' \
               f'Valor meia: {self.valor_meia}' \
               f'Status: {self.status}'

class ControllerSessao:
    def __init__(self):
        self.__load = Database().load_database('classSessao/bd_sessao.json', 5)
        self.__bd = Database()
        self.__format = Format().formatation_title

    def adicionarSessao(self):
        self.__format("Adicionar sessão")
        dt_sessao = input("Digite a data da sessâo: ")
        hor_sessao = input("Digite a hora da sessão: ")
        val_inteira = float(input("Digite o valor da sessão inteira: "))
        val_meia = (val_inteira/2)
        status = int(input("Digite o status da sessão: "))
        nova_sessao = Sessao(dt_sessao=dt_sessao, hor_sessao=hor_sessao, val_inteira=val_inteira, val_meia=val_meia, status=status).__dict__
        self.__load[dt_sessao] = nova_sessao
        self.__bd.add_database('classSessao/bd_sessao.json', self.__load, 5)
        print("{:~^43}".format(''))
        print("Sessão adicionada com sucesso")

    def listarSessoes(self):
        self.__format("Sessões disponíveis")
        print("{:<16}{:<16}{:<16}{:<16}{:<16}".format("Data", "Hora", "Valor inteira", "Valor meia", "Status"))
        print("{:~^74}".format(''))
        for sessao in self.__load.values():
            print("{:<16}{:<16}{:<16}{:<16}{:<16}".format(sessao.get("dt_sessao"), sessao.get("hor_sessao"), sessao.get("valor_inteira"), sessao.get("valor_meia"), sessao.get("status")))
            continue
        print("{:~^74}".format(''))

    def deletarSessao(self):
        self.__format("Deletar sessão")
        data = input("Digite a data da sessão para deletar: ")
        for sessao in self.__load.values():
            if sessao.get("dt_sessao") == data:
                del self.__load[data]
                break
        self.__bd.add_database('classSessao/bd_sessao.json', self.__load, 5)
        print("{:~^43}".format(''))
        print("Sessão deletada com sucesso")

    def editarSessao(self):
        pass
