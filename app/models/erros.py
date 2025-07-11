from typing import Optional
from sqlmodel import SQLModel, Field

class Erro(SQLModel, table = True):
    id : Optional[int] = Field(default=None, primary_key=True)
    #categoria (selação ENUM) pesquisar como faz
    nome_ferramenta : str
    descricao_erro : str
    descricao_solucao : str
    palavras_chaves : str
    proxy : bool #true se o proxy tiver relação com o erro false se não tiver