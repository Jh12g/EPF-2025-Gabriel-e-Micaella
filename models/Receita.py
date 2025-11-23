from services.BaseAbstrata import BaseAbstrata

class Receita(BaseAbstrata):
    def __init__(self, id=None, titulo="", ingredientes="", preparo="", categoria="", tempo=0, status="Pendente", autorId=None):
        
        super().__init__('data/receitas.json')
        
        self.id = id
        self.titulo = titulo
        self.ingredientes = ingredientes
        self.preparo = preparo
        self.categoria = categoria
        self.tempo = tempo  # em minutos
        self.status = status
        self.autorId = autorId

        
    def buscarID(self, id):
        for r in self._dados:
            if r['id'] == id:
                return r
        return None

    def tradutorJ(self):
        
        return {
            'id': self.id,
            'titulo': self.titulo,
            'ingredientes': self.ingredientes,
            'preparo': self.preparo,
            'categoria': self.categoria,
            'tempo': self.tempo,
            'status': self.status,
            'autorId': self.autorId,
            'tipo': 'padrao' 
        }

    def buscarStatus(self, status):
        return [r for r in self._dados if r.get('status') == status]

    def calcularDificuldade(self):
        
        if self.tempo <= 30:
            return "Fácil"
        elif self.tempo <= 60:
            return "Médio"
        else:
            return "Difícil"

    def avisoSeguranca(self):
        print("Atenção: Cuidado mexendo facas e fogo ☠️")