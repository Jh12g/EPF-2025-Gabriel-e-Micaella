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
            todos = self.model.listar_todos()
            novo_id = 1
            if todos:
                novo_id = max(c['id'] for c in todos) + 1

            # Instancia o objeto Comentario
            novo_comentario = EntidadeComentario(
                id=novo_id,
                texto=texto,
                autor_id=autor,
                receita_id=receita
            )

            # Acessa a lista interna da BaseAbstrata (_dados) e salva
            self.model.dados.append(novo_comentario.to_dict())
            self.model.salvar() # Persiste no disco
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
            
            # 3. Manda salvar a lista atualizada no arquivo
            self.model.salvar()
            return True
        return False

    def excluir(self, id_comentario):
        """
        Remove um comentário da lista e atualiza o arquivo.
        """
        comentario = self.model.buscar_por_id(id_comentario)
        
        if comentario:
            # remove o item da lista
            self.model.dados.remove(comentario)
            # salva a lista sem o item
            self.model.salvar()
            return True
        return False