from models.receita_model import ReceitaModel
from models.entidades import EntidadeReceita, EntidadeReceitaPet

class ReceitaService:
    def __init__(self):
        self.model = ReceitaModel()

    def listar_todas(self):
        return self.model.listar_todos()

    def listar_por_categoria(self, categoria):
        todas = self.model.listar_todos()
        
        # filtro pra que as receitas com status d 'pendente' fiquem invisíveis no cardápio
        return [r for r in todas if r.get('categoria') == categoria and r.get('status') == 'Ativo']
    
    # busca uma receita específica p editar
    def buscar_por_id(self, id):
        return self.model.buscar_por_id(id)

    # muda o status de Pendente p ativo
    def aprovar_receita(self, id):
        receita = self.model.buscar_por_id(id)
        if receita:
            receita['status'] = 'Ativo' # muda o status
            self.model.atualizar(receita) # salva no JSON
            return True
        return False

    # salva a receita editada
    def editar_receita(self, receita_atualizada_dict):
        # garante que o status se mantenha ou mude conforme regra
        self.model.atualizar(receita_atualizada_dict)

    # met de excluir
    def excluir_receita(self, id):
        self.model.excluir(id)

    def criar_receita(self, dados_form, autor_id):
        # met q gera ID
        todos = self.model.listar_todos()
        novo_id = (max([r['id'] for r in todos]) + 1) if todos else 1

        # lógica da dificuldade q tava em receitaModels
        try:
            tempo = int(dados_form.get('tempo'))
        except (ValueError, TypeError):
            tempo = 0
            
        if tempo <= 30:
            dificuldade = "Fácil"
        elif tempo <= 60:
            dificuldade = "Médio"
        else:
            dificuldade = "Difícil"

        # separando os dados comuns
        tipo = dados_form.get('tipo', 'padrao')
       
        dados_base = {
            'id': novo_id,
            'titulo': dados_form.get('titulo'),
            'ingredientes': dados_form.get('ingredientes'),
            'preparo': dados_form.get('preparo'),
            'categoria': dados_form.get('categoria'),
            'tempo': tempo,
            'dificuldade': dificuldade,
            'autor_id': autor_id,
            'tipo': tipo,
            'status': 'Pendente', # é padrao q toda receita começa pendente (((tentar add algo assim com foto)))
            
            # img salva no banco
            'imagem': dados_form.get('imagem')
        }

        # decisão de qual classe usar (mae ou filha)
        if tipo == 'pet':
            # instanciando a classe FILHA
            nova_receita = EntidadeReceitaPet(
                **dados_base, # passa todos os dados comuns
                especie=dados_form.get('especie'),
                aviso="Verifique alergias do seu pet!"
            )
        else:
            # instanciando a classe maeoai
            nova_receita = EntidadeReceita(**dados_base)

        # salva (polimorfismo no model.adicionar)
        self.model.adicionar(nova_receita)
        return True