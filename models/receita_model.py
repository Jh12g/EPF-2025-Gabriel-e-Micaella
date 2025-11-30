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
        # transforma em dicionário p json
        self.dados.append(receita.to_dict())
        self.salvar()

    # método p salvar alterações editar ou salvar
    def atualizar(self, receita_dict):
        for i, r in enumerate(self.dados):
            if r['id'] == receita_dict['id']:
                self.dados[i] = receita_dict
                self.salvar()
                break

    # método p excluir
    def excluir(self, id_item):
        self.dados = [r for r in self.dados if r['id'] != id_item]
        self.salvar()