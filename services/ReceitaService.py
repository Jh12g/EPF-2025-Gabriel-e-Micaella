from models.Receita import Receita
from models.ReceitaPet import ReceitaPet

class ReceitaService:
    def __init__(self):
        
        self._receitaModel = Receita()

    def criarReceita(self, dados, eh_pet=False):
      
        try:
           
            todos = self._receitaModel.retornarTudo()
            novo_id = 1
            if todos:
                novo_id = max(r['id'] for r in todos) + 1

            if eh_pet:
                nova_receita = ReceitaPet(
                    id=novo_id,
                    titulo=dados['titulo'],
                    ingredientes=dados['ingredientes'],
                    preparo=dados['preparo'],
                    categoria=dados['categoria'],
                    tempo=int(dados['tempo']),
                    autorId=dados['autorId'],
                    especie=dados.get('especie', 'Cachorro')
                )
            else:
                nova_receita = Receita(
                    id=novo_id,
                    titulo=dados['titulo'],
                    ingredientes=dados['ingredientes'],
                    preparo=dados['preparo'],
                    categoria=dados['categoria'],
                    tempo=int(dados['tempo']),
                    autorId=dados['autorId']
                )

            self._receitaModel._dados.append(nova_receita.tradutorJ())
            self._receitaModel.salvar()
            return True
        except Exception as e:
            print(f"Erro ao fazer a receita: {e}")
            return False

    def listagem(self): # Equivalente ao listarTodas do diagrama
        return self._receitaModel.retornarTudo()

    def listarCategoria(self, categoria):
        todas = self._receitaModel.retornarTudo()
        return [r for r in todas if r['categoria'] == categoria]

    def filtragem(self, termo):
        todas = self._receitaModel.retornarTudo()
        return [r for r in todas if termo.lower() in r['titulo'].lower()]

    def pendencia(self):
        return self._receitaModel.buscarStatus('Pendente')

    def mundacaEstatus(self, id, novo_status):
        receita_dict = self._receitaModel.buscarID(id)
        if receita_dict:
            receita_dict['status'] = novo_status
            self._receitaModel.salvar() 
            return True
        return False

    def Cores(self):
        
        return {
            "Pendente": "Laranja",
            "Aprovado": "Verde",
            "Rejeitado": "Vermelho"
        }