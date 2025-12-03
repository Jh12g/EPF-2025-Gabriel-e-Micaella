from bottle import Bottle, request
from .base_controller import BaseController
from services.receita_service import ReceitaService
from services.comentario_service import ComentarioService 

class ReceitaController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.receita_service = ReceitaService()
        self.comentario_service = ComentarioService() # inicia o service de comentários
        self.setup_routes() # chamando setup_routes que define as rotas

    def esta_logado(self):
        # verifica se tem alguém logado (agora usando COOKIE)
        return self.get_usuario_logado() is not None

    def opcoes(self):
        if not self.esta_logado(): return self.redirect('/login')
        return self.render('usuario/painel_opcoes') # renderiza o painel de botões

    # *******métodos de ação do admin********
    def aprovar(self, id):
        if not self.esta_logado(): return self.redirect('/login')
        self.receita_service.aprovar_receita(id)
        return self.redirect('/admin')

    def excluir(self, id):
        if not self.esta_logado(): return self.redirect('/login')
        self.receita_service.excluir_receita(id)
        return self.redirect('/admin')

    def editar(self, id):
        if not self.esta_logado(): return self.redirect('/login')
        
        receita = self.receita_service.buscar_por_id(id) # busca a receita para preencher o formulário
        
        if request.method == 'GET':
            # reutiliza o formulário de cadastro, mas enviando a receita p preencher
            return self.render('usuario/receita_form', titulo_pagina="Editar Receita", receita=receita)
        
        else:
            # POST - salvar edição
            dados_form = {
                'id': id,
                'titulo': request.forms.get('titulo'),
                'ingredientes': request.forms.get('ingredientes'),
                'preparo': request.forms.get('preparo'),
                'categoria': request.forms.get('categoria'),
                'tempo': int(request.forms.get('tempo')),
                'tipo': request.forms.get('tipo', 'padrao'),
                'especie': request.forms.get('especie', ''),
                'status': receita['status'],
                'autor_id': receita['autor_id'],
                # aq mantém a imagem antiga se não enviou nova, ou atualiza
                'imagem': request.forms.get('imagem') or receita.get('imagem'),
                'dificuldade': 'Recalcular...'
            }
            
            if dados_form['tempo'] <= 30: dados_form['dificuldade'] = "Fácil"
            elif dados_form['tempo'] <= 60: dados_form['dificuldade'] = "Médio"
            else: dados_form['dificuldade'] = "Difícil"

            self.receita_service.editar_receita(dados_form)
            return self.redirect('/admin')

    # ve detalhes da receita tipo o ifood
    def ver_receita(self, id):
        if not self.esta_logado(): return self.redirect('/login')
        
        receita = self.receita_service.buscar_por_id(id)
        if not receita: return self.redirect('/opcoes')

        # carrega os comentários dessa receita
        comentarios = self.comentario_service.listar_por_receita(id)
            
        # manda 'receita' E 'comentarios' para o HTML
        return self.render('usuario/ver_receita', receita=receita, comentarios=comentarios)

    # métodos do cardápio
    def cardapioCafe(self):
        if not self.esta_logado(): return self.redirect('/login')
        dados = self.receita_service.listar_por_categoria('Cafe')
        return self.render('usuario/lista_receitas', receitas=dados, titulo='Café da Manhã')

    def cardapioAlmoco(self):
        if not self.esta_logado(): return self.redirect('/login')
        dados = self.receita_service.listar_por_categoria('Almoco')
        return self.render('usuario/lista_receitas', receitas=dados, titulo='Almoço')

    def cardapioLanche(self):
        if not self.esta_logado(): return self.redirect('/login')
        dados = self.receita_service.listar_por_categoria('Lanche')
        return self.render('usuario/lista_receitas', receitas=dados, titulo='Lanche')

    def cardapioJanta(self):
        if not self.esta_logado(): return self.redirect('/login')
        dados = self.receita_service.listar_por_categoria('Janta')
        return self.render('usuario/lista_receitas', receitas=dados, titulo='Jantar')

    def cardapioPetisco(self):
        if not self.esta_logado(): return self.redirect('/login')
        dados = self.receita_service.listar_por_categoria('Petisco')
        return self.render('usuario/lista_receitas', receitas=dados, titulo='Petiscos')

    def cardapioGato(self):
        if not self.esta_logado(): return self.redirect('/login')
        dados = self.receita_service.listar_por_categoria('Gato')
        msg_alerta = "Cuidado! Tenha certeza que seu animal não tem nenhuma alergia. Verifique os ingredientes e dê pequenas porções inicialmente."
        return self.render('usuario/lista_receitas', receitas=dados, titulo='Receitas para Gatos', aviso=msg_alerta)

    def cardapioCachorro(self):
        if not self.esta_logado(): return self.redirect('/login')
        dados = self.receita_service.listar_por_categoria('Cachorro')
        msg_alerta = "Cuidado! Tenha certeza que seu animal não tem nenhuma alergia. Verifique os ingredientes e dê pequenas porções inicialmente."
        return self.render('usuario/lista_receitas', receitas=dados, titulo='Receitas para Cachorros', aviso=msg_alerta)

    def sugerir(self):
        if not self.esta_logado(): return self.redirect('/login')
        return self.render('usuario/receita_form', titulo_pagina="Sugerir uma Receita")

    def admin(self):
        if not self.esta_logado(): return self.redirect('/login')
        todas_receitas = self.receita_service.listar_todas()
        return self.render('admin/dashboard', receitas=todas_receitas)

    def novaReceita(self):
        if not self.esta_logado(): return self.redirect('/login')

        # parte das novas receitas
        # se for GET: mostra o formulário
        # se for POST: recebe os dados e chama o criarReceita do Service
        
        if request.method == 'GET':
            return self.render('usuario/receita_form')
        else:
            # captura os dados do formulário
            dados_form = {
                'titulo': request.forms.get('titulo'),
                'ingredientes': request.forms.get('ingredientes'),
                'preparo': request.forms.get('preparo'),
                'categoria': request.forms.get('categoria'),
                'tempo': request.forms.get('tempo'),
                'tipo': request.forms.get('tipo', 'padrao'),
                'especie': request.forms.get('especie', ''),
                # captura a imagem (ou usa padrão)
                # o .strip() remove espaços vazios antes e depois do link 
                'imagem': request.forms.get('imagem', '').strip() or "https://placehold.co/600x400?text=Sem+Foto"
            }

            # pega id do usuário logado (AGORA PELO COOKIE)
            dados_usuario = self.get_usuario_logado()
            autor_id = dados_usuario['id'] if dados_usuario else 1

            # salvando
            self.receita_service.criar_receita(dados_form, autor_id)
            
            # verifica se quem tá logado é admin (PELO COOKIE)
            eh_admin = dados_usuario.get('admin', False) if dados_usuario else False

            if eh_admin:
                return self.redirect('/admin')  # admin vai ver a lista de gestão
            else:
                return self.redirect('/opcoes') # usuário volta pro menu
        
    # Parte que nao entendi bem, estudar mais sobre (confuso)

    #explicacao p gabriel 
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
        self.app.route('/opcoes', method='GET', callback=self.opcoes)

        # rotas de rardápio
        self.app.route('/cafe', method='GET', callback=self.cardapioCafe)
        self.app.route('/almoco', method='GET', callback=self.cardapioAlmoco)
        self.app.route('/lanche', method='GET', callback=self.cardapioLanche)
        self.app.route('/petisco', method='GET', callback=self.cardapioPetisco)
        self.app.route('/janta', method='GET', callback=self.cardapioJanta)
        
        # rotas PET
        self.app.route('/gato', method='GET', callback=self.cardapioGato)
        self.app.route('/cachorro', method='GET', callback=self.cardapioCachorro)
        
        
        self.app.route('/receita/<id:int>', method='GET', callback=self.ver_receita) # rota de detalhes
        self.app.route('/sugerir', method='GET', callback=self.sugerir)
        self.app.route('/admin', method='GET', callback=self.admin)
        self.app.route('/nova_receita', method=['GET', 'POST'], callback=self.novaReceita)
        
        # rotas d aprovar, deletar, editar
        self.app.route('/receitas/aprovar/<id:int>', method='POST', callback=self.aprovar)
        self.app.route('/receitas/delete/<id:int>', method='POST', callback=self.excluir)
        self.app.route('/receitas/editar/<id:int>', method=['GET', 'POST'], callback=self.editar)