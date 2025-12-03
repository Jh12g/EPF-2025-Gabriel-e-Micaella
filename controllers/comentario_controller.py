from controllers.base_controller import BaseController
from services.comentario_service import ComentarioService
from bottle import request

class ComentarioController(BaseController):
    
    def __init__(self, app):
        super().__init__(app)
        
        # conectando controller e service
        self.comentario_service = ComentarioService()
        self.setup_routes()

    def postarComent(self):
        # verifica se tá logado antes de tudo (usando met do cookie omg)
        usuario = self.get_usuario_logado()
        if not usuario:
            return self.redirect('/login')

        if request.method == 'POST':
            texto = request.forms.get('texto')
            nota = request.forms.get('nota') 
            
            #segurança autor_id agora vem do cookie
            try:
                receita_id = int(request.forms.get('receita_id'))
                autor_id = usuario['id'] 
                
            except (ValueError, TypeError):
                print("Erro: IDs inválidos")
                return

            # chama o método do Service
            # criarComentario e variavel service certas agr
            self.comentario_service.criarComentario(texto, autor_id, receita_id, nota)

            # redireciona o usuário de volta p receita específica
            return self.redirect(f'/receita/{receita_id}')

    # admin pode apagar coment
    def deletar_comentario(self, id):
        # verifica se tá logado
        usuario = self.get_usuario_logado()
        if not usuario: return self.redirect('/login')

        # verifica se é admin
        if not usuario.get('admin', False):
            return self.redirect('/opcoes') # se não for admin, chuta fora

        # busca o comentário antes de apagar (pra saber pra qual receita voltar)
        comentario = self.comentario_service.buscar_por_id(id)
        
        receita_id = 1 # fallback se der erro
        if comentario:
            receita_id = comentario['receita_id']
            # apaga
            self.comentario_service.excluir(id)

        # volta pra receita
        return self.redirect(f'/receita/{receita_id}')

    def setup_routes(self): # define a rota POST que o formulário HTML vai chamar
        self.app.route('/comentar', method='POST', callback=self.postarComent)
        self.app.route('/comentarios/delete/<id:int>', method='POST', callback=self.deletar_comentario)