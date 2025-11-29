from bottle import Bottle
from controllers.usuario_controller import user_routes

def init_controllers(app: Bottle):
    app.merge(user_routes)
