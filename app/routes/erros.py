#importe de bibliotecas externas
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List

#importe de arquivos do projeto
from app.database import get_session
from app.schemas.erros import ErroCreate, ErroRead
from app.models.erros import Erro

router = APIRouter(prefix="/erros")

@router.post("/", status_code=status.HTTP_201_CREATED)
def criar_erro(dados : ErroCreate, session : Session = Depends(get_session)):
    novo = Erro(**dados.dict())
    session.add(novo)
    session.commit() #salva no banco de dados
    session.refresh(novo) #pega o objeto como foi salvo no banco de dados
    return novo

@router.get("/", response_model=List[ErroRead])
def listar_erros(session : Session = Depends(get_session)):
    return session.query(Erro).all()


@router.delete("/{id}", status_code=status.HTTP_200_OK)
def deletar_erro(id : int, session : Session = Depends(get_session)):
    erro = session.get(Erro, id)
    if not erro:
        raise HTTPException(status_code=404, detail="Registro de erro não encontrado")
    
    session.delete(erro)
    session.commit()
    return {"mensagem":"Registro de erro deletado com sucesso"}