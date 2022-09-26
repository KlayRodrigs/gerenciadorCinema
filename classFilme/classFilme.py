from classFilme.auxFilme import Format
from time import time
from classFilme.database_controler import Database
from classFilme.auxClassGenero import Genero
from classFilme.auxClassAtor import Ator


class Filme:
    def __init__(self, titulo: str, duracao: time, genero: str, papelAtor: str, quemAtua: str):
        self.titulo = titulo
        self.duracao = duracao
        self.genero = genero
        self.atua = quemAtua
        self.papelAtor = papelAtor

    def __str__(self):
        return f'Titulo: {self.titulo}, Duracao: {self.duracao}, Genero: {self.genero}, Ator: {self.atua}, Papel: {self.papelAtor}'


class ControllerFilmes:
    def __init__(self):
        self.__load = Database().load_database('classFilme/bd_filmes.json', 5)
        self.__bd = Database()
        self.__format = Format().formatation_title

    def adicionarFilme(self):
        self.__format("Adicionar Filme")
        titulo = input("Digite o nome do filme: ")
        duracao = input("Digite a duração do filme: ")
        genero = input("Digite o gênero do filme: ").title()
        descri = Genero().ver(genero)
        papelAtor = input("Digite o papel do ator: ")
        at = Ator(papelAtor).ver()
        quemAtua = input("Digite o nome do ator: ")
        #dicionarioTemporario = {'ator': papelAtor, 'papel': quemAtua} UM FILME PODE TER VÁRIOS ATORES

        novo_filme = Filme(titulo=titulo, duracao=duracao, genero=descri, papelAtor=at, quemAtua=quemAtua).__dict__
        self.__load[titulo] = novo_filme
        self.__bd.add_database('classFilme/bd_filmes.json', self.__load, 4)
        print("{:~^43}".format(''))
        print("Filme adicionado com sucesso")

    def listarFilmes(self):
        self.__format("Filmes disponíveis")
        print("{:<16}{:<26}".format("Titulo", "Duração/min"))
        print("{:~^43}".format(''))
        for filme in self.__load.values():
            print("{:<16}{:<16}".format(filme.get("titulo"), filme.get("duracao")))
            continue
        print("{:~^43}".format(''))

    def deletarFilme(self):
        self.__format("Deletar Filme")
        titulo = input('Digite o nome do filme para remover: ')
        for filme in self.__load.values():
            if filme.get("titulo") == titulo:
                del self.__load[titulo]
                break
        self.__bd.add_database('classFilme/bd_filmes.json', self.__load, 4)
        print("{:~^43}".format(''))
        print("Filme deletado com sucesso")

    def editarFilme(self):
        pass
