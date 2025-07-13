from typing import Optional
from sqlmodel import SQLModel, Field
from enum import Enum
from sqlalchemy import Column, Enum as SQLEnum

class CategoriaEnum(str, Enum):
    FRONT_END = "Front-End"
    BACK_END = "Back-End"

class Tutorial(SQLModel, table = True):
    id : Optional[int] = Field(default=None, primary_key=True)
    categoria : CategoriaEnum = Field(sa_column=Column(SQLEnum(CategoriaEnum)))
    nome_ferramenta : str
    comandos : str
    palavras_chaves : str