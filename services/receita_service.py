from models.receita_model import ReceitaModel
from models.entidades import EntidadeReceita, EntidadeReceitaPet

class ReceitaService:
    def __init__(self):
        self.model = ReceitaModel()

    def listar_todas(self):
        return self.model.listar_todos()

    def listar_por_categoria(self, categoria):
        todas = self.model.listar_todos()
        return [r for r in todas if r.get('categoria') == categoria]

    def criar_receita(self, dados_form, autor_id):
        # gera ID
        todos = self.model.listar_todos()
        novo_id = (max([r['id'] for r in todos]) + 1) if todos else 1

        # lógica da dificuldade q tava em receitaModels
        tempo = int(dados_form.get('tempo'))
        if tempo <= 30:
            dificuldade = "Fácil"
        elif tempo <= 60:
            dificuldade = "Médio"
        else:
            dificuldade = "Difícil"

        # separando os dados comuns
        tipo = dados_form.get('tipo_receita', 'padrao')
        
        dados_base = {
            'id': novo_id,
            'titulo': dados_form.get('titulo'),
            'ingredientes': dados_form.get('ingredientes'),
            'preparo': dados_form.get('preparo'),
            'categoria': dados_form.get('categoria'),
            'tempo': tempo,
            'dificuldade': dificuldade,
            'autor_id': autor_id,
            'tipo': tipo
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