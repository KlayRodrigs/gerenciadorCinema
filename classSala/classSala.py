from classSala.database_controler import Database
from classSala.auxSala import Format


class Sala:
    def __init__(self, nro_sala: int, capacidade: int):
        self.nro_sala = nro_sala
        self.capacidade = capacidade

    def __str__(self):
        return f'Numero da sala: {self.nro_sala}, Capacidade: {self.capacidade}'


class ControllerSala:
    def __init__(self):
        self.__load = Database().load_database('classSala/bd_salas.json', 5)
        self.__bd = Database()
        self.__format = Format().formatation_title

    def adicionarSala(self):
        self.__format("Adicionar sala")
        nro_sala = int(input("Digite o número da sala: "))
        capacidade = int(input("Digite a capacidade da sala: "))
        nova_sala = Sala(nro_sala=nro_sala, capacidade=capacidade).__dict__
        self.__load[str(nro_sala)] = nova_sala
        self.__bd.add_database('classSala/bd_salas.json', self.__load, 5)
        print("{:~^43}".format(''))
        print("Sala adicionada com sucesso")

    def deleteSala(self):
        self.__format("Deletar sala")
        nro_sala = input("Digite o número da sala para deletar: ")
        for sala in self.__load.values():
            if sala.get("nro_sala") == int(nro_sala):
                del self.__load[nro_sala]
                break
        self.__bd.add_database('classSala/bd_salas.json', self.__load, 5)
        print("{:~^43}".format(''))
        print("Sala deletada com sucesso")

    def consultarSala(self):
        self.__format("Salas disponíveis")
        nro_sala = input("Digite o número da sala para consulta: ")
        print("{:~^43}".format(''))
        print("{:<16}{:<26}".format("Número da sala", "Capacidade da sala"))
        print("{:~^43}".format(''))
        for sala in self.__load.values():
            if sala.get("nro_sala") == int(nro_sala):
                print("{:<20}{:<20}".format(sala.get("nro_sala"), sala.get("capacidade")))
        print("{:~^43}".format(''))

    def editarSala(self):
        pass
