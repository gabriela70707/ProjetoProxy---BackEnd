from pydantic import BaseModel
from enum import Enum
from typing import Optional

class CategoriaEnum(str, Enum):
    FRONT_END = "Front-End"
    BACK_END = "Back-End"


class TutorialBase(BaseModel):
    categoria : CategoriaEnum
    nome_ferramenta : str
    comandos : str
    palavras_chaves : str

class TutorialCreate(TutorialBase):
    pass

class TutorialUpdate(BaseModel):
    categoria : Optional[CategoriaEnum] = None
    nome_ferramenta : Optional[str] = None
    comandos : Optional[str] = None
    palavras_chaves : Optional[str] = None

class TutorialRead(TutorialBase):
    id : int

    class Config:
        orm_mode = True