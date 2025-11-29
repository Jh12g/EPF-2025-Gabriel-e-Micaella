from models.receita_model import ReceitaModel
from models.entidades import EntidadeReceita, EntidadeReceitaPet

class ReceitaService:
    def __init__(self):
        self.model = ReceitaModel()

    def listar_todas(self):
        return self.model.listar_todos()

    def listar_por_categoria(self, categoria):
        todas = self.model.listar_todos()
        return [r for r in todas if r.get('categoria') == categoria] #isso daqui é um loop for 
        # p cada receita f na lista de todas as receitas, ele verifica se a categoria da receita é igual a categoria pedida

    def criar_receita(self, dados_form, autor_id):
        # gera ID
        todos = self.model.listar_todos()
        novo_id = (max([r['id'] for r in todos]) + 1) if todos else 1 #else 1 pq se tiver vazio ele cria o primeiro id 

        # lógica da dificuldade q tava em receitaModels
        # try/except e int() para evitar erro se vier vazio
        try:
            tempo = int(dados_form.get('tempo')) #o usuario pode escrever em forma d texto ai isso força pra int
        except (ValueError, TypeError): #se ele escrever letras ou deixar vazio da erro MAS nao vai quebrar o cod so vai virar 0
            tempo = 0

        if tempo <= 30:
            dificuldade = "Fácil"
        elif tempo <= 60:
            dificuldade = "Médio"
        else:
            dificuldade = "Difícil"

        # separando os dados comuns
        tipo = dados_form.get('tipo', 'padrao') # usuário escolhe tipo de receita (humano ou pet) mas se nao escolher vai por padrao q é humano
        
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
            'status': 'Pendente'
        }

        # decisão de qual classe usar (mae ou filha) 
        if tipo == 'pet':
            # instanciando a classe FILHA
            nova_receita = EntidadeReceitaPet(
                **dados_base, 
                especie=dados_form.get('especie', 'Cachorro'),
                aviso="Verifique alergias do seu pet!"
            )
        else:
            # instanciando a classe maepai
            nova_receita = EntidadeReceita(**dados_base)

        # salva (polimorfismo no model.adicionar)
        self.model.adicionar(nova_receita)
        return True