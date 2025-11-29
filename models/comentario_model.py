from .base_model import BaseModel
from .entidades import EntidadeReceita

class ComentarioModel(BaseModel):
    def __init__(self):
        # chamando o construtor da classe pai (seguindo o modelo das outras classes)
        super().__init__('comentarios.json')

#base model ja salva lista e carrega ent nao precisa reescrever elas + buscar por id

    # buscar o id de quem comentou
    def buscar_por_id(self, id_item): 
        return next((c for c in self.dados if c['id'] == id_item), None)
    
# gabriel aqui n precisa de to_dict pq ja tem na entidadeComentario
#lembrando q as entidades servem p segurar os dados e essas models unicas serve pra gravar e ler no disco
# essas entidades sao como folhas de papeis preenchidas com os dados e as model fazem o trabalho d gerenciar (gurdar e recuperar) as fichas (((service cordena tudo como regras calculos logica)))