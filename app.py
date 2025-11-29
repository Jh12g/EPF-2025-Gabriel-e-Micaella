from bottle import Bottle
# importando os meus controllers 
from controllers.usuario_controller import UserController
from controllers.receita_controller import ReceitaController
from controllers.comentario_controller import ComentarioController

class App:
    def __init__(self):
        # cria a aplicação Bottle
        self.app = Bottle()
        self.setup_routes()

    def setup_routes(self):
        print("🔧 Configurando Rotas...")
        
        # ao instanciar os controllers passando 'self.app',  eles injetam as rotas automaticamente (por causa do super init)
        self.user_controller = UserController(self.app)
        self.receita_controller = ReceitaController(self.app)
        self.comentario_controller = ComentarioController(self.app)
        
        print("✅ Rotas Carregadas!")

    def get_app(self):
        return self.app