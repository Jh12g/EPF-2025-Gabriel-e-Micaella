import abc
import json
from pathlib import Path


class BaseAbstrata(abc.ABC):
    
    _caminhoArquivo: Path
    _dados: list
    
    def __init__(self, caminho_arquivo: str):
     
        self._caminhoArquivo = Path(caminho_arquivo)
        self._dados = []
        self.carregar()

    

    def carregar(self) -> None:
      
        try:
            with open(self._caminhoArquivo, 'r', encoding='utf-8') as f:
                self._dados = json.load(f)
        except FileNotFoundError:
            
            print(f"Arquivo {self._caminhoArquivo.name} não encontrado.")
            self.salvar()
        except json.JSONDecodeError:
            print("Erro")
            self._dados = []

    def salvar(self) -> None:
        

        self._caminhoArquivo.parent.mkdir(parents=True, exist_ok=True) 
        with open(self._caminhoArquivo, 'w', encoding='utf-8') as f:
            
            json.dump(self._dados, f, indent=4, ensure_ascii=False)
            
    
    @abc.abstractmethod
    def buscarID(self, id: int):
        
        pass

    def retornarTudo(self) -> list:
        
        return self._dados

