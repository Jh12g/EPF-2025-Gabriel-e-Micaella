from bottle import static_file, template, HTTPResponse, response, request, redirect
from config import Config  # import necessário p cookies
import json

class BaseController:
    def __init__(self, app): #guarda a aplicação bootle 
        self.app = app
        self._setup_base_routes() #configura as rotas

    def _setup_base_routes(self): #define as rotas básicas que todos os controllers herdam 
        
        self.app.route('/static/<filename:path>', callback=self.serve_static) # rota para arquivos estáticos (da pasta static)
        
        # rota da página inicial (landing)
        self.app.route('/', callback=self.home_landing)
        self.app.route('/helper', method='GET', callback=self.helper)

    #**********método de cookie***********
    def get_usuario_logado(self):
        # PRINT DE DEBUG PQ NAO TA DANDO CERTO: avisa que tentou ler
        print("DEBUG: Tentando ler o cookie 'user_session'...")
        
        cookie_valor = request.get_cookie("user_session", secret=Config.SECRET_KEY)
        
        # PRINT DE DEBUG: mostra o que achou (ou se achou nada)
        print(f"DEBUG: Valor bruto encontrado no cookie: {cookie_valor}")
        
        if cookie_valor:
            try:
                dados = json.loads(cookie_valor)
                # PRINT DE DEBUG: sucesso ao converter
                print(f"DEBUG: Cookie convertido com sucesso: {dados}")
                return dados
            except json.JSONDecodeError:
                print("DEBUG: ERRO CRÍTICO! O cookie existe mas não é um JSON válido.")
                return None
        
        print("DEBUG: Nenhum cookie válido encontrado.")
        return None

    def render(self, filename, **kwargs): #,étodo auxiliar para renderizar templates
        
        # FORÇA O NAVEGADOR A NÃO CACHEAR 
        response.set_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        response.set_header('Pragma', 'no-cache')
        response.set_header('Expires', '0')

        # TENTA ler o cookie
        dados_usuario = self.get_usuario_logado()
        
        #verifica se retornou algo válido
        logged_in = dados_usuario is not None
        is_admin = False
        
        if logged_in:
            # o cookie guarda um dicionário d dados (tipo id etc)
            is_admin = dados_usuario.get('admin', False)

        # manda essas informações pro HTML
        kwargs['logado'] = logged_in
        kwargs['is_admin'] = is_admin
        
        return template(filename, **kwargs)

    # agr só os métodos de rota arrumados   
    def serve_static(self, filename): #serve arquivos estáticos da pasta static 
        return static_file(filename, root='./static')

    def home_landing(self): #renderiza a landing (pag inicial)
        return self.render('landing')

    def helper(self): #Renderiza a página de debug/ajuda
        return self.render('helper-final')

    def redirect(self, url): #redirecionamento
        # usando o redirect nativo do Bottle. 
        # ele aborta a execução MAS leva os cookies junto com ele 
        return redirect(url)