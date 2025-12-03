from models.comentario_model import ComentarioModel
from models.entidades import EntidadeComentario
from services.usuario_service import UsuarioService

class ComentarioService:
    def __init__(self):
        self.model = ComentarioModel()
        self.usuario_service = UsuarioService() 

    def criarComentario(self, texto, autor, receita, nota): # p receber nota e os dados, gerando um id
        try:
            todos = self.model.listar_todos()
            novo_id = 1
            if todos:
                novo_id = max(c['id'] for c in todos) + 1

            # busca o nome do usuário para salvar junto
            nome_autor = self.usuario_service.obter_nome_por_id(autor)

            # instancia o objeto comentario
            novo_comentario = EntidadeComentario(
                id=novo_id,
                texto=texto,
                autor_id=autor,
                receita_id=receita,
                # add coisa pra deixar a nota 
                nome_autor=nome_autor,
                nota=int(nota)
            )

            # acessa a lista interna d dados da base e salva
            self.model.dados.append(novo_comentario.to_dict())
            self.model.salvar() # persiste no disco
            return True
        except Exception as e:
            print(f"Erro ao criar comentário: {e}")
            return False

    # CONFERIR MELHOR DEPOIS!!!!

    def listar_por_receita(self, receita_id):
        todos = self.model.listar_todos()
        return [c for c in todos if c['receita_id'] == receita_id]
    
    def editar(self, id_comentario, novo_texto):
        """
        Busca um comentário pelo ID e atualiza seu texto.
        """
        comentario = self.model.buscar_por_id(id_comentario)
        if comentario:
            # gabriel, como em python dicionários são passados por referência, mudar aqui muda direto na lista self.model.dados
            comentario['texto'] = novo_texto
            
            # manda salvar a lista atualizada no arquivo
            self.model.salvar()
            return True
        return False
    
    def buscar_por_id(self, id): #retorna um comentário específico pelo id
        return self.model.buscar_por_id(id)

    def excluir(self, id_comentario): 
        comentario = self.model.buscar_por_id(id_comentario)
        
        if comentario:
            # remove o item da lista
            self.model.dados.remove(comentario)
            # salva a lista sem o item
            self.model.salvar()
            return True
        return False