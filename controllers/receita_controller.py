from bottle import Bottle, request
from .base_controller import BaseController
from services.receita_service import ReceitaService

class ReceitaController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.receita_service = ReceitaService() 
        self.setup_routes() # chamando setup_routes que define as rotas


    def cardapioCafe(self):
        # Lista de receitas do cafe da manha
        dados = self.receita_service.listar_por_categoria('Cafe')
        # render (do BaseController)
        return self.render('lista_receitas', receitas=dados, titulo='Café da Manhã')

    def cardapioAlmoco(self):
        # Lista de receitas do almoço
        dados = self.__receita_service.listarCategoria('Almoco')
        self.renderizacao('lista_receitas', {'receitas': dados, 'titulo': 'Almoço'})

    def cardapioLanche(self):
        # Lista de receitas do lanche
        dados = self.__receita_service.listarCategoria('Lanche')
        self.renderizacao('lista_receitas', {'receitas': dados, 'titulo': 'Lanche'})

    def cardapioJanta(self):
        # Lista de receitas do jantar
        dados = self.__receita_service.listarCategoria('Janta')
        self.renderizacao('lista_receitas', {'receitas': dados, 'titulo': 'Jantar'})

    def cardapioPetisco(self):
        # Lista de receitas dos petiscos
        dados = self.__receita_service.listarCategoria('Petisco')
        self.renderizacao('lista_receitas', {'receitas': dados, 'titulo': 'Petiscos'})

    def cardapioGato(self):
        # Lista de receitas de comida para gato
        dados = self.__receita_service.listarCategoria('Gato')
        self.renderizacao('lista_receitas', {'receitas': dados, 'titulo': 'Receitas para Gatos'})

    def cardapioCachorro(self):
         # Lista de receitas de comida para gato
        dados = self.__receita_service.listarCategoria('Cachorro')
        self.renderizacao('lista_receitas', {'receitas': dados, 'titulo': 'Receitas para Cachorros'})

    def sugerir(self):
         # pagina de sugestõess
       return self.render('receita_form', titulo_pagina="Sugerir uma Receita") #p funcionar com receita_form.tpl

    def admin(self):
        # Parte do adm
        todas_receitas = self.receita_service.listar_todas()
        return self.render('admin_dashboard', receitas=todas_receitas)

    def novaReceita(self):
        # parte das novas receitas
        # Se for GET: Mostra o formulário. 
        # Se for POST: Recebe os dados e chama o criarReceita do Service. (parte importante)
        
        if request.method == 'GET':
            return self.render('receita_form')
        else:
            # Captura os dados do formulário
            # empacotando em um dicionário para enviar ao service
            dados_form = {
                'titulo': request.forms.get('titulo'),
                'ingredientes': request.forms.get('ingredientes'),
                'preparo': request.forms.get('preparo'),
                'categoria': request.forms.get('categoria'),
                'tempo': request.forms.get('tempo'),
                'tipo': request.forms.get('tipo', 'padrao'),
                'especie': request.forms.get('especie', '')
            }

            # ID provisório so pra testar 
            #TEM Q APAGAR ISSO DEPOIS E TROCAR PELA LÓGICA DO USUARIO Q TA LOGADO 
            autor_id = 1

            '''
            QUANDO o login estiver pronto: no topo do arquivo from bottle import request, redirect

            ai dentro desse método: apagar o id provisorio e botar esse definitivo

             # tenta pegar o ID do cookie seguro
             usuario_logado_id = request.get_cookie("session_id", secret='sua-chave-secreta-aqui')

            if not usuario_logado_id:
            # se não tem ninguém logado, chuta ele para a tela de login
            return self.redirect('/login')

            # ai usa o ID real
            self.receita_service.criar_receita(dados_form, int(usuario_logado_id))
            '''

            # chamando o método criarReceita do Service e passando o dicionário e o ID
            self.receita_service.criar_receita(dados_form, autor_id)
           
            # usa o método redirecionar do BaseController
            return self.redirect('/admin')
        
    # Parte que nao entendi bem, estudar mais sobre (confuso)

    #explicacao p gabriel tb 
    #essa parte do cod é tipo um mapa, o setup_routes conecta os endreços url q o usuario digita com a função python q deve responder a esses endereços
    # esse def é o mét chamado quando o sistema inicia 
    # self.app é o bottle (servidor web) 
    # os argumentos tipo /cafe e /almoco é o endereço url
    #met GET é o tipo d acesso permitido q é padrao p quando alguem so quer ver conteudo
    # callback é a instrução principal pra executar a função 
    # get = visualizar, post = tipo quando o usuário quer salvar 
    # OU SEJA routes organiza o tráfego d cada url
    
    def setup_routes(self):
        """
        Mapeia as URLs para os métodos da classe.
        Usa o objeto 'app' que vem herdado do BaseController.
        """
        # Rotas de Cardápio
        self.app.route('/cafe', method='GET', callback=self.cardapioCafe)
        self.app.route('/almoco', method='GET', callback=self.cardapioAlmoco)
        self.app.route('/lanche', method='GET', callback=self.cardapioLanche)
        self.app.route('/petisco', method='GET', callback=self.cardapioPetisco)
        self.app.route('/janta', method='GET', callback=self.cardapioJanta)
       
        # Rotas Pet
        self.app.route('/gato', method='GET', callback=self.cardapioGato)
        self.app.route('/cachorro', method='GET', callback=self.cardapioCachorro)
       
        # Outras rotas
        self.app.route('/sugerir', method='GET', callback=self.sugerir)
        self.app.route('/admin', method='GET', callback=self.admin)
        self.app.route('/nova_receita', method=['GET', 'POST'], callback=self.novaReceita)