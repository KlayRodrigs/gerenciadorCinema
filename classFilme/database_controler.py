import os
import json
'''
ID SALA1{
    FILME{
        SESSÕES{    

        }
    }
}
ID SALA2{
    FILME2{
        SESSÕES{

        }
    }
}

'''
class Database:
    def add_database(self, caminho_arquivo: str, dic_adicionar: dict, identacao: int):
        with open(caminho_arquivo, 'w') as arq_json:
            json.dump(dic_adicionar, arq_json, indent=identacao)

    def _load_database(self, caminho_arquivo: str, identacao: int):
        dic_load = {}

        if self.verificar_arquivo(caminho_arquivo):
            with open(caminho_arquivo, 'r') as arq_json:
                dic_load = json.load(arq_json)
            return dic_load
        self.add_database(caminho_arquivo, dic_load, identacao)

    def load_database(self, caminho_arquivo, identacao):
        return self._load_database(caminho_arquivo, identacao)

    def verificar_arquivo(self, caminho_arquivo: str):
        if os.path.exists(caminho_arquivo):
            return caminho_arquivo
        return False