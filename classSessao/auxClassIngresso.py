class Ingresso:
    def __init__(self, valorEntradaInteira: int, valorEntradaMeia: int):
        self.inteira = valorEntradaInteira
        self.meia = valorEntradaMeia
        self.quantidadeVendidosInteira = 0
        self.quantidadeVendidosMeia = 0
        # Valores a serem opções no menu: 1 = Inteira/ 2 = Meia

    # Usado de base para gerar/lançar ingresso no sistema, está privado porque não precisa retornar nada além de somar o tipo de ingresso ao self.tipoDoIngresso
    def _gerarIngresso(self, tipo: int):
        if self.verificaQuantidade() == 1:

            # AQUI É SE NÃO FOR INTEIRA OU MEIA
            if tipo != 1 or tipo != 2:
                return 0

            if tipo == 1:
                self.quantidadeVendidosInteira += 1

            elif tipo == 2:
                self.quantidadeVendidosMeia += 1
            return 1

        else:
            return 0

    # AQUI EU CONFIRMO E VERIFICO USANDO OUTRA FUNÇÃO PARA PODER DIZER SE A COMPRA FOI OU NÃO BEM SUCEDIDA.
    def confirmacaoCompra(self, valor):
        # Se deu tudo ok o retorno da função acima será 1, logo a mensagem será de OKay para a compra.
        if self._gerarIngresso(valor) == 1:
            print('Compra efetuada com sucesso!')

        # Caso o retorno seja 0, eu separei abaixo dessa, pois não consegui formular uma frase legal com esses dois problemas(não possuir cadeiras e caso digite algo além de 1 e 0)
        elif self._gerarIngresso(valor) == 0:
            print('Compra não efetuada devido a falta de acentos.')

        else:
            print('Por favor selecione apenas uma das opções do menu')

    # O 10 DEVE SER O REFERENTE A QUANTIDADE DE INGRESSOS NO BD, QUANDO CRIA-LO, MUDAR POR FAVOR POIS ESSE VALOR FOI PURAMENTE PARA TESTE E ESTÁ OKAY!.
    def verificaQuantidade(self):
        if (self.quantidadeVendidosMeia + self.quantidadeVendidosInteira) < 10:  # Esse 10 aqui
            return 1
        else:
            return 0

    def __str__(self) -> str:
        return f'****************************************\n' \
               f'Quantidade de ingressos vendidos: \n' \
               f'Entrada inteira: {self.quantidadeVendidosInteira}\n' \
               f'Entrada meia: {self.quantidadeVendidosMeia}\n' \
               f'****************************************\n'

    # Quando criar o BD, formular uma forma de excluir/editar adequada, por agora não sei como funcionará.
