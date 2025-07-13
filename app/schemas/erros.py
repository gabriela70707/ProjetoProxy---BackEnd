from pydantic import BaseModel
from typing import Optional
from enum import Enum

class CategoriaEnum(str, Enum):
    FRONT_END = "Front-End"
    BACK_END = "Back-End"

class ErroBase(BaseModel):
    categoria : CategoriaEnum
    nome_ferramenta : str
    descricao_erro : str
    descricao_solucao : str
    palavras_chaves : str
    proxy : bool #true se o proxy tiver relação com o erro false se não tiver

class ErroCreate(ErroBase):
    pass

class ErroUpdate(BaseModel):
    categoria : Optional[CategoriaEnum] = None
    nome_ferramenta : Optional[str] = None
    descricao_erro : Optional[str] = None
    descricao_solucao : Optional[str] = None
    palavras_chaves : Optional[str] = None
    proxy : Optional[bool] = None #true se o proxy tiver relação com o erro false se não tiver

class ErroRead(ErroBase):
    id : int

    class Config:  #permitir retornar um objeto diretamente
        orm_mode = True