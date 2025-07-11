from pydantic import BaseModel

class TutorialCreate(BaseModel):
    #categoria enum pesquisar como faz
    nome_ferramenta : str
    comandos : str

class TutorialRead(BaseModel):
    id : int
    #categoria enum pesquisar como faz
    nome_ferramenta : str
    comandos : str

    class Config:
        orm_mode = True