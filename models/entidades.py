from dataclasses import dataclass, asdict

# ent. de receita
@dataclass
class EntidadeReceita: # classe p separar a lógica d salvar arquivo, igual o prof fez com user
    id: int
    titulo: str
    ingredientes: str
    preparo: str
    categoria: str
    tempo: int
    autor_id: int
    dificuldade: str = "Não calculada"
    status: str = "Pendente"
    tipo: str = "padrao" # padrao ou pet

    def to_dict(self): 
        return asdict(self)
    
    def exibir_info(self):
        return f"Receita: {self.titulo}"

# classe filha ds receita
@dataclass
class EntidadeReceitaPet(EntidadeReceita):
    # atributos exclusivos da filha
    especie: str = "Cachorro" # so usado se for Pet
    aviso: str = "Verifique alergias" # também
    
    # polimorfismo do dict
    def to_dict(self):
        # pega os dados como se fosse uma receita normal
        dados = super().to_dict()
        
        # adiciona a marcação de que é Pet e a espécie
        dados['tipo'] = 'pet'
        dados['especie'] = self.especie
        
        return dados

    def aviso_seguranca(self):
        return f"Atenção: Verifique se o animal ({self.especie}) não é alérgico."

# ent. de usuario
@dataclass
class EntidadeUsuario:
    id: int
    nome: str
    email: str
    senha: str
    admin: bool = False

    def to_dict(self):
        return asdict(self)
    
@dataclass
class EntidadeComentario:

    id: int
    texto: str
    autorid: int
    receitaid: int

    def to_dict(self):
        return asdict(self)

@dataclass
class EntidadeComentario:
    def __init__(self, id, texto, autor, receita):
        self.id = id
        self.texto = texto
        self.autor_id = autor
        self.receita_id = receita

    def tradutorJ(self):
        # Retorna dicionário para salvar no JSON
        return {
            "id": self.id,
            "texto": self.texto,
            "autorId": self.autor_id,
            "receitaId": self.receita_id
        }