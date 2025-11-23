from models.Receita import Receita

class ReceitaPet(Receita):
    def __init__(self, id=None, titulo="", ingredientes="", preparo="", categoria="", tempo=0, status="Pendente", autorId=None, especie="Cachorro"):
        super().__init__(id, titulo, ingredientes, preparo, categoria, tempo, status, autorId)
        self.especie = especie

    def tradutorJ(self):
        dados = super().tradutorJ()
        dados['especie'] = self.especie
        dados['tipo'] = 'pet' # Marca como pet no JSON
        return dados

    def avisoSeguranca(self):
        print(f"Atenção: Verifique se o animal ({self.especie}) não é alérgico a algum dos ingredientes da receita.")