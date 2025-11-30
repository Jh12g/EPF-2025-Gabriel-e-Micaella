from models.usuario_model import UsuarioModel
from models.entidades import EntidadeUsuario

class UsuarioService:
    def __init__(self):
        self.model = UsuarioModel()

    def get_all(self):
        return self.model.listar_todos()
    
    def get_by_id(self, user_id):
        return self.model.buscar_por_id(user_id)

    def autenticar(self, email, senha):
        """Verifica login"""
        usuario = self.model.buscar_por_email(email)
        
        # acessando senha com colchetes
        if usuario and usuario['senha'] == senha:
            return usuario
        return None
    
    # adicionado método save p compatibilidade com UserController
    def save(self):
        from bottle import request
        nome = request.forms.get('name')
        email = request.forms.get('email')
        senha = request.forms.get('password') 
        self.criar_usuario(nome, email, senha)

    def criar_usuario(self, nome, email, senha, admin=False):
        # verifica se já existe esse email
        if self.model.buscar_por_email(email):
            return False, "Email já cadastrado!"

        # gera novo id
        todos = self.model.listar_todos()
        novo_id = (max([u['id'] for u in todos]) + 1) if todos else 1

        # cria a entidade
        novo_usuario = EntidadeUsuario(
            id=novo_id,
            nome=nome,
            email=email,
            senha=senha,
            admin=admin
        )
        
        self.model.adicionar(novo_usuario)
        return True, "Usuário criado com sucesso!"

    def obter_nome_por_id(self, user_id):
        user = self.model.buscar_por_id(user_id)
        return user['nome'] if user else "Desconhecido"
    
    def delete_user(self, user_id):
        self.model.delete_user(user_id)
        
    def edit_user(self, user):
        self.model.update_user(user)