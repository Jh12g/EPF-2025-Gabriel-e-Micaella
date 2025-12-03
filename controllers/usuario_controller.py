from bottle import request, response
from .base_controller import BaseController
from services.usuario_service import UsuarioService
from config import Config #pro cookie
import json 

class UserController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.service = UsuarioService()
        self.setup_routes()

    def setup_routes(self):
        # mapeia as URLs para as funções
        # self.app é o bottle (servidor web) 
        # os argumentos tipo /cafe e /almoco é o endereço url
        # met GET é o tipo d acesso permitido q é padrao p quando alguem so quer ver conteudo
        # callback é a instrução principal pra executar a função 
        # get = visualizar, post = tipo quando o usuário quer salvar 
        
        # as rotas de login/cadastro que tavam faltando e causando erro
        self.app.route('/login', method=['GET', 'POST'], callback=self.login)
        self.app.route('/cadastro', method=['GET', 'POST'], callback=self.cadastro)
        self.app.route('/logout', method='GET', callback=self.logout)

        # rotas de usuário/admin
        self.app.route('/users', method='GET', callback=self.list_users)
        self.app.route('/users/add', method=['GET', 'POST'], callback=self.add_user)
        self.app.route('/users/edit/<user_id:int>', method=['GET', 'POST'], callback=self.edit_user)
        self.app.route('/users/delete/<user_id:int>', method='POST', callback=self.delete_user)

    # métodos de logim
    def login(self):
        print(f"DEBUG: Método recebido foi {request.method}") 
        
        if request.method == 'GET':
            print("DEBUG: Mostrando formulário...") 
            return self.render('login', erro=None)
        
        print("DEBUG: Tentando processar login...")
        
        email = request.forms.get('email')
        senha = request.forms.get('senha')
        
        usuario = self.service.autenticar(email, senha)
        
        if usuario:
            print(f"Login Sucesso! Criando cookie para ID {usuario['id']}.") 
            
            # criando um dicionário com o que queremos guardar no cookie (id e se é admin)
            dados_sessao = {
                'id': usuario['id'],
                'admin': usuario.get('admin', False)
            }
            
            # transforma o dicionário em TEXTO p bottle aceitar e não dar erro
            dados_json = json.dumps(dados_sessao)
            
            # CRIANDO O COOKIE ASSINADO
            # acho q 'secret' vai garantir que ninguém consiga falsificar o cookie
            # ADICIONEI path='/' 
            response.set_cookie("user_session", dados_json, secret=Config.SECRET_KEY, path='/')
            
            return self.redirect('/opcoes')
        else:
            return self.render('login', erro="Email ou senha incorretos!")

    def logout(self):
        # DELETANDO O COOKIE 
        # path='/' 
        response.delete_cookie("user_session", path='/')
        return self.redirect('/login')

    def cadastro(self):
        if request.method == 'GET':
            return self.render('cadastro', erro=None)
            
        nome = request.forms.get('nome')
        email = request.forms.get('email')
        senha = request.forms.get('senha')
        
        # tenta criar (admin = false por padrão)
        sucesso, msg = self.service.criar_usuario(nome, email, senha, admin=False)
        
        if sucesso:
            return self.redirect('/login')
        else:
            return self.render('cadastro', erro=msg)

    #*******************métodos d admin
    def list_users(self):
        # busca todos os usuários via service
        users = self.service.get_all()
        # apontando para a pasta admin
        return self.render('admin/users', users=users)

    def add_user(self):
        if request.method == 'GET':
            # exibe o formulário vazio
            # apontando para a pasta admin
            return self.render('admin/user_form', user=None, action="/users/add")
        
        # se for POST (clicou em salvar):
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
            # apontando para a pasta admin
            return self.render('admin/user_form', user=user, action=f"/users/edit/{user_id}")
        
        # se for POST (edição):
        # atualiza o dicionário do usuário com os novos dados do form
        user['nome'] = request.forms.get('nome')
        user['email'] = request.forms.get('email')
        
        # atualiza se é admin também na edição
        user['admin'] = request.forms.get('admin') == 'on'

        nova_senha = request.forms.get('senha')
        
        if nova_senha and nova_senha.strip() != "": # o if verifica se a nova senha não está vazia
            user['senha'] = nova_senha # se estiver vazia, o código ignora e a senha antiga continua
        
        self.service.edit_user(user)
        return self.redirect('/users')

    def delete_user(self, user_id):
        self.service.delete_user(user_id)
        return self.redirect('/users')