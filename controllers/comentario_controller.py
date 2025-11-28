from controllers.base_controller import BaseController
from services.comentario_service import ComentarioService
from bottle import request, redirect

class ComentarioController(BaseController):
    
    def __init__(self):
        super().__init__()
        
        # Isso conecta o Controller ao Service 
        self.__comentario_service = ComentarioService()
        self.rotas()

    def postarComent(self):
        if request.method == 'POST':
            texto = request.forms.get('texto')
            autor_id = request.forms.get('autor_id')
            receita_id = request.forms.get('receita_id')
            
            # Conversão de segurança 
            try:
                autor_id = int(request.forms.get('autor_id'))
                receita_id = int(request.forms.get('receita_id'))
            except (ValueError, TypeError):
                print("Erro: IDs inválidos")
            return

            # Chama o método do Service 
            sucesso = self.__comentario_service.criarComentario(texto, autor_id, receita_id)

            # Redireciona o usuário de volta para a página anterior
            # Se não conseguir descobrir a anterior, vai para a home '/'
            back_url = request.headers.get('Referer', '/')
            self.redirecionar(back_url)

    def rotas(self):
        """
        Define a rota POST que o formulário HTML vai chamar.
        """
        # A rota '/comentar' deve estar no 'action' do seu formulário
        self.app.route('/comentar', method='POST', callback=self.postarComent)