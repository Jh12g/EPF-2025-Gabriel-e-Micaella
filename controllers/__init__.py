from bottle import Bottle
# importando todos os controllers, isso aq serve pra "centralizar" e iniciar tudo primeiro registrando as rotas
from controllers.usuario_controller import UserController
from controllers.receita_controller import ReceitaController
from controllers.comentario_controller import ComentarioController

def init_controllers(app: Bottle):
    
    print('Carregando UsuarioController...')
    UserController(app)
    
    print('Carregando ReceitaController...')
    ReceitaController(app)
    
    print('Carregando ComentarioController...')
    ComentarioController(app)