from bottle import Bottle, request
from .base_controller import BaseController
from services.receita_service import ReceitaService

class ReceitaController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.setup_routes()
        self.receita_service = ReceitaService()


    def cardapioCafe(self):
        # Lista de receitas do cafe da manha
        dados = self.__receita_service.listarCategoria('Cafe')
        self.renderizacao('lista_receitas', {'receitas': dados, 'titulo': 'Café da Manhã'})

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
        self.renderizacao('sugestao_form')

    def admin(self):
        # Parte do adm
        todas_receitas = self.__receita_service.listarTodas()
        self.renderizacao('admin_dashboard', {'receitas': todas_receitas})

    def novaReceita(self):
        # parte das novas receitas
        # Se for GET: Mostra o formulário. 
        # Se for POST: Recebe os dados e chama o criarReceita do Service. (parte importante)
        
        if request.method == 'GET':
            self.renderizacao('receita_form')
        else:
            # Captura os dados do formulário
            titulo = request.forms.get('titulo')
            ingredientes = request.forms.get('ingredientes')
            preparo = request.forms.get('preparo')
            categoria = request.forms.get('categoria')
            tempo = request.forms.get('tempo')
            
            # Chama o método criarReceita do Service (conforme diagrama)
            self.__receita_service.criarReceita(
                titulo, ingredientes, preparo, categoria, tempo
            )
            
            # Usa o método redirecionar do BaseController
            self.redirecionar('/admin')

    # Parte que nao entendi bem, estudar mais sobre (confuso)

    def rotas(self):
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