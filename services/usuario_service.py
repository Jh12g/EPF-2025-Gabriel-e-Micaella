from models.usuario_model import UsuarioModel
from models.entidades import EntidadeUsuario

class UsuarioService:
    def __init__(self):
        self.model = UsuarioModel()

    def autenticar(self, email, senha):
        """Verifica login"""
        usuario = self.model.buscar_por_email(email)
        if usuario and usuario['senha'] == senha:
            return usuario
        return None

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