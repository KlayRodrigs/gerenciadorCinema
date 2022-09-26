from classFilme import classFilme
from classSala import classSala
from classSessao import classSessao, auxClassIngresso
import random

class Menu:
    def menuPrincipal(self):
        while True:
            print('------------------Menu Inicial------------------')
            print('[1] - Sala')
            print('[2] - Sessão')
            print('[3] - Filme')
            print('[4] - Ingressos vendidos')
            print('[0] - Sair')
            print('------------------------------------------------')
            opcao = int(input('Digite a opção desejada:'))
            if 0 <= opcao <= 5:
                match opcao:
                    case 1:
                        Menu.menuSala(self)
                    case 2:
                        Menu.menuSessao(self)
                    case 3:
                        Menu.menuFilme(self)
                    case 4:
                        Menu.menuIngresso(self)
                    case 0:
                        break
            else:
                print('Opção inválida, tente outra!')

    def menuSessao(self):
        while True:
            print('------------------Menu Filme------------------')
            print('[1] - Adicionar sessão')
            print('[2] - Ver sessões')
            print('[3] - Editar sessão')
            print('[4] - Excluir sessão')
            print('[0] - Sair')
            print('----------------------------------------------')
            opcao = int(input('Digite a opção desejada:'))
            if 0 <= opcao < 5:
                match opcao:
                    case 1:
                        classSessao.ControllerSessao().adicionarSessao()
                    case 2:
                        classSessao.ControllerSessao().listarSessoes()
                    case 3:
                        classSessao.ControllerSessao().editarSessao()
                    case 4:
                        classSessao.ControllerSessao().deletarSessao()
                    case 0:
                        print('Sair!')
                        break
            else:
                print('Opção inválida, tente outra!')

    def menuFilme(self):
        while True:
            print('------------------Menu Filme------------------')
            print('[1] - Adicionar filme')
            print('[2] - Ver filmes')
            print('[3] - Editar filmes')
            print('[4] - Excluir filmes')
            print('[0] - Sair')
            print('----------------------------------------------')
            opcao = int(input('Digite a opção desejada:'))
            if 0 <= opcao < 5:
                match opcao:
                    case 1:
                        classFilme.ControllerFilmes().adicionarFilme()
                    case 2:
                        classFilme.ControllerFilmes().listarFilmes()
                    case 3:
                        classFilme.ControllerFilmes().editarFilme()
                    case 4:
                        classFilme.ControllerFilmes().deletarFilme()
                    case 0:
                        print('Sair!')
                        break
            else:
                print('Opção inválida, tente outra!')

    def menuSala(self):
        while True:
            print('------------------Menu Sala------------------')
            print('[1] - Adicionar sala')
            print('[2] - Ver salas')
            print('[3] - Editar sala')
            print('[4] - Excluir sala')
            print('[0] - Sair')
            print('----------------------------------------------')
            opcao = int(input('Digite a opção desejada:'))
            if 0 <= opcao < 5:
                match opcao:
                    case 1:
                        classSala.ControllerSala().adicionarSala()
                    case 2:
                        classSala.ControllerSala().consultarSala()
                    case 3:
                        classSala.ControllerSala().editarSala()
                    case 4:
                        classSala.ControllerSala().deleteSala()
                    case 0:
                        print('Sair')
                        break
            else:
                print('Opção inválida, tente outra!')

    #ESSE MÉTODO ESTÁ AQUI MAIS NÃO CABE A ELE ESSA FUNÇÃO. O ATO DE COMPRAR É FEITO PELO USUÁRIO NO MENU DO USUÁRIO E NÃO NO CONTROLLER DO CINEMA. NÃO TEM COMO EU CONTABILIZAR A QUANTIDADE DE INGRESSOS COMPRADOS SE NENHUM PODE SER COMPRADO PELO SISTEMA DO CINEMA.
    def menuIngresso(self):
        print(random.randint(10, 100))#PUTARIA ISSO AQUI


Menu().menuPrincipal()
