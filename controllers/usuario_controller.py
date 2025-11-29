from bottle import request, response  
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
        # met GET é o tipo d acesso permitido q é padrao p quando alguem so quer ver conteudo
        # callback é a instrução principal pra executar a função 
        # get = visualizar, post = tipo quando o usuário quer salvar 

        self.app.route('/users', method='GET', callback=self.list_users)
        self.app.route('/users/add', method=['GET', 'POST'], callback=self.add_user)
        self.app.route('/users/edit/<user_id:int>', method=['GET', 'POST'], callback=self.edit_user)
        self.app.route('/users/delete/<user_id:int>', method='POST', callback=self.delete_user)
        self.app.route('/login', method=['GET', 'POST'], callback=self.login)
        self.app.route('/cadastro', method=['GET', 'POST'], callback=self.cadastro)
        self.app.route('/logout', method='GET', callback=self.logout)

        def login(self): #verifica se o usuário ta apenas entrando na página (get)
                if request.method == 'GET':
            # mostra o formulário de login limpo (sem erros)
                    return self.render('login', erro=None)
        
        # agora POST pq o usuário clicou no botão d entrar
        email = request.forms.get('email')
        senha = request.forms.get('senha')
        
        # chama o service p verificar se esse email e senha existem
        usuario = self.service.autenticar(email, senha)
        
        # se o service retornou um usuário (login correto)
        if usuario:
            # cria um "crachá" (cookie) no navegador do usuário com o ID dele
            response.set_cookie("session_id", str(usuario['id']), secret='segredo_super_secreto_do_projeto_oo')
            
            # redireciona o usuário para a página inicial do sistema 
            return self.redirect('/opcoes')
        else:
            # se o login falhou (usuário vazio), carrega a tela de login de novo e enviando uma mensagem de erro para aparecer no alerta vermelho
            return self.render('login', erro="Email ou senha incorretos!")

    def cadastro(self):
        # verifica se o usuário está apenas entrando na página de cadastro (get)
        if request.method == 'GET':
            # mostra o formulário de cadastro limpo
            return self.render('cadastro', erro=None)
            
        # POST: o usuário preencheu e enviou
        nome = request.forms.get('nome')
        email = request.forms.get('email')
        senha = request.forms.get('senha')
        
        # chama o Service para tentar criar
        # passa admin=false pois cadastro público não é chefe
        # o service retorna duas coisas: true/false (sucesso) e uma Mensagem (msg)
        sucesso, msg = self.service.criar_usuario(nome, email, senha, admin=False)
        
        if sucesso:
            # se criou com sucesso, manda ele para a tela de login para entrar
            return self.redirect('/login')
        else:
            # se deu erro (tipo por ex: email já existe), recarrega a página mostrando o erro
            return self.render('cadastro', erro=msg)

    def logout(self):
        # apaga o cookie do navegador desconectando o usuário
        response.delete_cookie("session_id")
        
        # manda ele de volta para a tela de login
        return self.redirect('/login')

    def list_users(self):
        # busca todos os usuários via service
        users = self.service.get_all()
        # apontando para a pasta admin com user.tpl (tpl é um arquivo q mistura html e python, se fizesse so html puro ia ter q escrever TODAS as info. com tpl eu so rodo o python, ele preenche as lacunas - tipo nome: {nome} vai ser nome: maria - e gera o html final
        return self.render('admin/users', users=users) 

    def add_user(self):
        if request.method == 'GET':
            # exibe o formulário vazio
            # apontando para a pasta admin onde está o user_form.tpl
            return self.render('admin/user_form', user=None, action="/users/add")
        
        # se for POST (clicou em Salvar):
        # pega os dados que vieram do HTML
        # n esquecer q no html tem q ta esses nomes
        nome = request.forms.get('nome')
        email = request.forms.get('email')
        senha = request.forms.get('senha')
        admin = request.forms.get('admin') == 'on' # exemplo p checkbox

        sucesso, mensagem = self.service.criar_usuario(nome, email, senha, admin) # manda o service criar
        
        return self.redirect('/users') # redireciona

    def edit_user(self, user_id):
        # busca o usuário antigo para preencher o formulário
        user = self.service.get_by_id(user_id)
        if not user:
            return "Usuário não encontrado"

        if request.method == 'GET':
            # apontando p a pasta admin d view
            return self.render('admin/user_form', user=user, action=f"/users/edit/{user_id}")
        
        # se for POST (edição):
        # atualiza o dicionário do usuário com os novos dados do form
        user['nome'] = request.forms.get('nome')
        user['email'] = request.forms.get('email')
        user['admin'] = request.forms.get('admin') == 'on'

        nova_senha = request.forms.get('senha')
        
        if nova_senha and nova_senha.strip() != "": # o if verifica se a nova senha não está vazia
            user['senha'] = nova_senha # se estiver vazia, o código ignora e a senha antiga 
        
        
        self.service.edit_user(user)
        return self.redirect('/users')

    def delete_user(self, user_id):
        self.service.delete_user(user_id)
        return self.redirect('/users')