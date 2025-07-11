from typing import Optional
from sqlmodel import SQLModel, Field

class Tutorial(SQLModel, table = True):
    id : Optional[int] = Field(default=None, primary_key=True)
    #categoria enum pesquisar como faz
    nome_ferramenta : str
    comandos : str