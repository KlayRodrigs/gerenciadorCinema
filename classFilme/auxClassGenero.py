class Genero:
    def __init__(self):
        self.tipos = {'Ação': 'Bom', 'Romance': 'Gueba', 'Terror': 'Machãum'}

    def ver(self, valor: str):
        for i in self.tipos.keys():
            if valor == i:
                return f'{valor}: {self.tipos[i]}'
        return 'Valor desconhecido'

    def add_genero(self):
        self.descricao = input('Digite o gênero: ')
        return self.descricao