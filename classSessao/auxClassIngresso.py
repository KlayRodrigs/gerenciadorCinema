from classSala import classSala


class Ingresso:
    def __init__(self, valorEntradaInteira: int, valorEntradaMeia: int):
        self.inteira = valorEntradaInteira
        self.meia = valorEntradaMeia
        self.quantidadeVendidosInteira = 0
        self.quantidadeVendidosMeia = 0
        # Valores a serem opções no menu: 1 = Inteira/ 2 = Meia

    # Usado de base para gerar/lançar ingresso no sistema, está privado porque não precisa retornar nada além de somar o tipo ingresso ao self.tipoDoIngresso
    def _gerarIngresso(self, tipo: int):
        if self.verificaQuantidade() == 1:
            if tipo != 1 or tipo != 2:
                return 3
            if tipo == 1:
                self.quantidadeVendidosInteira += 1
            elif tipo == 2:
                self.quantidadeVendidosMeia += 1
            return 1
        else:
            return 0

    def confirmacaoCompra(self, valor):
        if self._gerarIngresso(valor) == 1:
            print('Compra efetuada com sucesso!')
        elif self._gerarIngresso(valor) == 0:
            print('Compra não efetuada devido a falta de acentos.')
        else:
            print('Por favor selecione apenas uma das opções do menu')

    def verificaQuantidade(self):
        if (self.quantidadeVendidosMeia + self.quantidadeVendidosInteira) < classSala.Sala().capacidade:
            return 1
        else:
            return 0

    def __str__(self) -> str:
        return f'****************************************\n' \
               f'Quantidade de ingressos vendidos: \n' \
               f'Entrada inteira: {self.quantidadeVendidosInteira}\n' \
               f'Entrada meia: {self.quantidadeVendidosMeia}\n' \
               f'****************************************\n'

    # Quando criar o Banco de dados, formular uma forma de excluir/editar adequada, por agora não sei como funcionará.


#Poder adicionar mais de um ator por filme.
#Ingresso
#Unir tudo num db para simular ingresso