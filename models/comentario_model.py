from .base_model import BaseModel
from .entidades import EntidadeReceita

class ComentarioModel(BaseModel):
    def __init__(self):
        # chamando o construtor da classe pai (seguindo o modelo das outras classes)
        super().__init__('comentarios.json')

    # buscar o id de quem comentou
    def buscar_por_id(self, id_item):
        return next((c for c in self.dados if c['id'] == id_item), None)
    

    # não tenho certeza de como é pra ser feito o tradutorJ 
    # (micaella se vc souber melhor essa parte da um help)