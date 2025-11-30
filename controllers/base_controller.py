from bottle import static_file, template, HTTPResponse, response, request
import sessao #importando memória

class BaseController:
    def __init__(self, app): #guarda a aplicação bootle 
        self.app = app
        self._setup_base_routes() # configura as rotas

    def _setup_base_routes(self):
        """ define as rotas básicas que todos os controllers herdam """
        
        # rota para arquivos estáticos (da pasta static)
        self.app.route('/static/<filename:path>', callback=self.serve_static)
        
        # rota da página inicial (landing)
        self.app.route('/', callback=self.home_landing)
        self.app.route('/helper', method='GET', callback=self.helper)

    def serve_static(self, filename): #serve arquivos estáticos da pasta static 
        return static_file(filename, root='./static')

    def home_landing(self): #renderiza a landing (pag inicial)
        return self.render('landing')

    def helper(self): #Renderiza a página de debug/ajuda
        return self.render('helper-final')

    def render(self, filename, **kwargs): #,étodo auxiliar para renderizar templates

        logged_in = sessao.usuarios_logados.get('atual') is not None # verifica se tem alguém logado
        is_admin = sessao.usuarios_logados.get('eh_admin') is True  # verifica se esse alguém é admin
        
        # manda essas informações para o HTML
        kwargs['logado'] = logged_in
        kwargs['is_admin'] = is_admin
        
        return template(filename, **kwargs)

    def redirect(self, url): #redirecionamento
        return response.set_header('Location', url) or HTTPResponse(status=302, headers={'Location': url})