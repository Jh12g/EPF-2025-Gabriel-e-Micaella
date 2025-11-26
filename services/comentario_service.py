from models.comentario_model import ComentarioModel
from models.entidades import EntidadeComentario

class ComentarioService:
    def __init__(self):
        self.model = ComentarioModel()

    def criarComentario(self, texto, autor, receita):
        """
        Recebe os dados brutos, gera um ID sequencial .
        """
        try:
            # gerador de ID  
            todos = self.comentarioModel.retornarTudo()
            novo_id = 1
            if todos:
                novo_id = max(c['id'] for c in todos) + 1

            # Instancia o objeto Comentario
            novo_comentario = EntidadeComentario(
                id=novo_id,
                texto=texto,
                autor=autor,
                receita=receita
            )

            # Acessa a lista interna da BaseAbstrata (_dados) e salva
            self.comentarioModel._dados.append(novo_comentario.tradutorJ())
            self.comentarioModel.salvar() # Persiste no disco
            return True
        except Exception as e:
            print(f"Erro ao criar comentário: {e}")
            return False

    # CONFERIR MELHOR DEPOIS!!!!

    def listarPorReceita(self, receita_alvo):
        """
        Filtra os comentários para mostrar apenas os de uma receita específica.
        """
        todos = self.comentarioModel.retornarTudo()
        # List Comprehension: cria uma nova lista apenas com os itens que passam no teste (if)
        return [c for c in todos if c['receita'] == receita_alvo]

    def editar(self, id_comentario, novo_texto):
        """
        Busca um comentário pelo ID e atualiza seu texto.
        """
        comentario_dict = self.comentarioModel.buscarID(id_comentario)
        if comentario_dict:
            comentario_dict['texto'] = novo_texto
            self.comentarioModel.salvar() # Salva a alteração no arquivo
            return True
        return False

    def excluir(self, id_comentario):
        """
        Remove um comentário da lista e atualiza o arquivo.
        """
        comentario_dict = self.comentarioModel.buscarID(id_comentario)
        if comentario_dict:
            self.comentarioModel._dados.remove(comentario_dict)
            self.comentarioModel.salvar()
            return True
        return False