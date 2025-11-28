from bottle import Bottle, request
from .base_controller import BaseController
from services.comentario_service import ComentarioService


class ComentarioController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.setup_routes()
        self.comentario_service = ComentarioService()

   # Terminar Classe 