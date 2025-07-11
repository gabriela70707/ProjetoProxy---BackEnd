from pydantic import BaseModel

class ErroCreate(BaseModel):
    #categoria (selação ENUM) pesquisar como faz
    nome_ferramenta : str
    descricao_erro : str
    descricao_solucao : str
    palavras_chaves : str
    proxy : bool #true se o proxy tiver relação com o erro false se não tiver

class ErroRead(BaseModel):
    id : int
    #categoria (selação ENUM) pesquisar como faz
    nome_ferramenta : str
    descricao_erro : str
    descricao_solucao : str
    palavras_chaves : str
    proxy : bool #true se o proxy tiver relação com o erro false se não tiver

    class Config:  #permitir retornar um objeto diretamente
        orm_mode = True