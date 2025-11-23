from services.BaseAbstrata import BaseAbstrata

class Usuario(BaseAbstrata):
    def __init__(self, id=None, nome="", email="", senha="", admin=False):
        
        super().__init__('data/usuarios.json')
        
        
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.admin = admin

    
    def buscarID(self, id):
        
        for u in self._dados:
            if u['id'] == id:
                return u
        return None


    def tradutorJ(self):
        
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'senha': self.senha,
            'admin': self.admin
        }
        
    def buscarEmail(self, email):
        
        for u in self._dados:
            if u['email'] == email:
                return u 
        return None

    def verificarSenha(self, email, senha):
        
        user_dict = self.buscarEmail(email)
        if user_dict and user_dict['senha'] == senha:
            return True
        return False