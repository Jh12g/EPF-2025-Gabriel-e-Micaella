from .base_model import BaseModel
from .entidades import EntidadeReceita

class ReceitaModel(BaseModel):
    def __init__(self):
        # chamando o construtor da classe pai (base) definindo o arquivo
        super().__init__('receitas.json')

    def buscar_por_id(self, id_item):
        # esse next percorre a lista caçando o id, esse none significa p parar assim q encontrar o primeiro resultado
        return next((r for r in self.dados if r['id'] == id_item), None)

    def buscar_por_status(self, status):
        # percorre a lista e cria uma nova p status 
        return [r for r in self.dados if r.get('status') == status]

    def adicionar(self, receita): 
        self.dados.append(receita.to_dict()) # transforma em dicionário p json
        self.salvar()