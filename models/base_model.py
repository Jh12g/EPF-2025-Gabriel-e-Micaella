from abc import ABC, abstractmethod
import json
import os

class BaseModel(ABC):
    # essa classe abstrata define o contrato p persistência
    
    def __init__(self, filename):
        # caminho p pasta data/ (a que vai ter os arquivos .json)
        # .. ta saindo de models e indo p data (filename é o arquvio especifico)
        self.file_path = os.path.join(os.path.dirname(__file__), '..', 'data', filename)
        
        # essa linha de código faz com q o ponto de partida seja models
        self.dados = self._carregar()

    def _carregar(self): # _ é encapsulamento em python
        # verificando se o arquivo existe
        if not os.path.exists(self.file_path):
            return []
        try:
            # abre o arquivo so pra leitura
            with open(self.file_path, 'r', encoding='utf-8') as f: #f é so uma variavel q quando o python pega um arquivo aberto (open) ele coloca dentro dela
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def salvar(self):
        # garante que o diretório existe
        # se a pasta q vc quer abrir rodando o cód nao existe, essa linha vai criar p nao dar erro
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        
        # w apaga tudo do conteúdo antigo e escreve outro por isso, isso é p atualizar
        with open(self.file_path, 'w', encoding='utf-8') as f:
            # comando q converte a lista do python p texto json
            json.dump(self.dados, f, indent=4, ensure_ascii=False)

    def listar_todos(self): # getter
        return self.dados

    @abstractmethod
    def buscar_por_id(self, id_item):
        pass