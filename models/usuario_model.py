from .base_model import BaseModel
from .entidades import EntidadeUsuario

class UsuarioModel(BaseModel):
    def __init__(self):
        # coloca que vai salvar no arquivo usuarios.json
        super().__init__('usuarios.json')

    def buscar_por_id(self, id_item):
        return next((u for u in self.dados if u['id'] == id_item), None)

    # mét. p Login
    def buscar_por_email(self, email):
        return next((u for u in self.dados if u['email'] == email), None)

    def adicionar(self, usuario: EntidadeUsuario):
        self.dados.append(usuario.to_dict())
        self.salvar()

    def update_user(self, usuario_dict):
        for i, u in enumerate(self.dados):
            if u['id'] == usuario_dict['id']:
                self.dados[i] = usuario_dict
                self.salvar()
                break

    def delete_user(self, user_id: int):
        self.dados = [u for u in self.dados if u['id'] != user_id]
        self.salvar()