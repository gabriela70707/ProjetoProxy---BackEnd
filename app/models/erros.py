from typing import Optional
from sqlmodel import SQLModel, Field
from enum import Enum
from sqlalchemy import Column, Enum as SQLEnum #colocando o nome SQLEnum para evitar confusão entre o enum do python e a do sqlalchemy

class CategoriaEnum(str, Enum):
    FRONT_END = "Front-End"
    BACK_END = "Back-End"


class Erro(SQLModel, table = True):
    id : Optional[int] = Field(default=None, primary_key=True)
    categoria : CategoriaEnum = Field(sa_column=Column(SQLEnum(CategoriaEnum)))
    nome_ferramenta : str
    descricao_erro : str
    descricao_solucao : str
    palavras_chaves : str
    proxy : bool #true se o proxy tiver relação com o erro false se não tiver