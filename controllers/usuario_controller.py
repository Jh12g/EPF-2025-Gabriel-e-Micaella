from bottle import request
from .base_controller import BaseController
from services.usuario_service import UsuarioService

class UserController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.service = UsuarioService()
        self.setup_routes()

    def setup_routes(self):

        # mapeia as URLs para as funções
        # self.app é o bottle (servidor web) 
        # os argumentos tipo /cafe e /almoco é o endereço url
        #met GET é o tipo d acesso permitido q é padrao p quando alguem so quer ver conteudo
        # callback é a instrução principal pra executar a função 
        # get = visualizar, post = tipo quando o usuário quer salvar 

        self.app.route('/users', method='GET', callback=self.list_users)
        self.app.route('/users/add', method=['GET', 'POST'], callback=self.add_user)
        self.app.route('/users/edit/<user_id:int>', method=['GET', 'POST'], callback=self.edit_user)
        self.app.route('/users/delete/<user_id:int>', method='POST', callback=self.delete_user)

    def list_users(self):
        # busca todos os usuários via service
        users = self.service.get_all()
        return self.render('users', users=users)

    def add_user(self):
        if request.method == 'GET':
            # exibe o formulário vazio
            return self.render('user_form', user=None, action="/users/add")
        
        # se for POST (clicou em Salvar):
        # pega os dados que vieram do HTML
        # n esquecer q no html tem q ta esses nomes
        nome = request.forms.get('nome')
        email = request.forms.get('email')
        senha = request.forms.get('senha')
        admin = request.forms.get('admin') == 'on' # exemplo para checkbox

        sucesso, mensagem = self.service.criar_usuario(nome, email, senha, admin) # manda o service criar
        
        return self.redirect('/users') # redireciona

    def edit_user(self, user_id):
        # busca o usuário antigo para preencher o formulário
        user = self.service.get_by_id(user_id)
        if not user:
            return "Usuário não encontrado"

        if request.method == 'GET':
            return self.render('user_form', user=user, action=f"/users/edit/{user_id}")
        
        # se for POST (edição):
        # atualiza o dicionário do usuário com os novos dados do form
        user['nome'] = request.forms.get('nome')
        user['email'] = request.forms.get('email')
        nova_senha = request.forms.get('senha')
        
        if nova_senha and nova_senha.strip() != "": # o if verifica se a nova senha não está vazia
            user['senha'] = nova_senha # se estiver vazia, o código ignora e a senha antiga 
        
        
        self.service.edit_user(user)
        return self.redirect('/users')

    def delete_user(self, user_id):
        self.service.delete_user(user_id)
        return self.redirect('/users')