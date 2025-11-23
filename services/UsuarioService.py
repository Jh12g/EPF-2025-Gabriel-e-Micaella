from models.Usuario import Usuario

class UsuarioService:
    def __init__(self):
        
        self._usuarioModel = Usuario()

    def autenticador(self, email, senha):
        
        return self._usuarioModel.verificarSenha(email, senha)

    def criarUsuario(self, nome, email, senha, admin=False):
       
        try:
            lista_usuarios = self._usuarioModel.retornarTudo()
            novo_id = 1
            if lista_usuarios:
                novo_id = max(u['id'] for u in lista_usuarios) + 1

            
            novo_user = Usuario(novo_id, nome, email, senha, admin)
            
            
            self._usuarioModel._dados.append(novo_user.tradutorJ())
            
            
            self._usuarioModel.salvar()
            return True
        except Exception as e:
            print(f"Erro ao criar usuário: {e}")
            return False

    def obterId(self, email):
        
        user_dict = self._usuarioModel.buscarEmail(email)
        if user_dict:
            return user_dict['id']
        return None

    def admin(self, id):
        
        user_dict = self._usuarioModel.buscarID(id)
        if user_dict and user_dict['admin'] is True:
            return True
        return False