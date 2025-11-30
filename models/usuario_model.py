from .base_model import BaseModel
from .entidades import EntidadeUsuario

class UsuarioModel(BaseModel):
    def __init__(self):
        super().__init__('usuarios.json')

    def buscar_por_id(self, id_item):
        # lembrar sempre d usar colchetes pois é um dicionário!!!!!!!!
        return next((u for u in self.dados if u['id'] == id_item), None)

    def buscar_por_email(self, email):
        return next((u for u in self.dados if u['email'] == email), None)

    def adicionar(self, usuario: EntidadeUsuario):
        self.dados.append(usuario.to_dict())
        self.salvar()

    def update_user(self, usuario_dict): # aqui o dict precisa ser acessado como dict ['id']
        
        for i, u in enumerate(self.dados): #o python começa a varrer a lista de todos os usuários cadastrados (self.dados), 
                    #enumerate é um truque p saber o número da linha (i) e os dados da pessoa (u) ao mesmo tempo.
            if u['id'] == usuario_dict['id']: #ve se o id é o mesmo q vc buscou
                self.dados[i] = usuario_dict #se for, ele substitui os dados
                self.salvar()
                break

    def delete_user(self, user_id: int):
        self.dados = [u for u in self.dados if u['id'] != user_id] #msm fita 
        self.salvar()