#importe de bibliotecas externas
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import List, Optional

#importe de arquivos do projeto
from app.database import get_session
from app.models.tutoriais import Tutorial
from app.schemas.tutoriais import TutorialCreate, TutorialRead, TutorialUpdate, CategoriaEnum

router = APIRouter(prefix="/tutoriais")

@router.post("/", status_code=status.HTTP_201_CREATED, tags=["Rotas de Tutoriais"])
def criar_tutorial(dados : TutorialCreate, session : Session = Depends(get_session)):
    tutorial = Tutorial(**dados.dict())
    session.add(tutorial)
    session.commit()
    session.refresh(tutorial)
    return tutorial

@router.get("/", response_model=List[TutorialRead], tags=["Rotas de Tutoriais"])
def listar_tutoriais(session : Session = Depends(get_session)):
    return session.query(Tutorial).all()



#Rota para barra de pesquisa
@router.get("/buscar", response_model=List[TutorialRead], tags=["Filtros"])
def procurar_tutorial(palavra: str, session : Session = Depends(get_session)):
    procura = select(Tutorial).where(Tutorial.palavras_chaves.contains(palavra)) #.contains(palavra): procura registros onde o campo palavras_chaves contém a palavra digitada
    resultados = session.exec(procura).all() #executa a busca e retorna como uma lista
    return resultados

#filtro por categoria (Front - Back)
@router.get("/categoria", response_model=List[TutorialRead], tags=["Filtros"])
def filtrar_tutoriais_por_categoria(categoria : Optional[CategoriaEnum] = None, session : Session = Depends(get_session)):
    filtro = select(Tutorial)
    if categoria is not None: #verifica se categoria foi passada na url
        filtro = filtro.where(Tutorial.categoria == categoria)
    
    resultados = session.exec(filtro).all()
    return resultados


# Buscar por um tutorial especifico
@router.get("/{id}", response_model=TutorialRead, tags=["Rotas de Tutoriais"])
def buscar_tutorial(id : int, session : Session = Depends(get_session)):
    tutorial = session.get(Tutorial, id)
    if not tutorial:
        raise HTTPException(status_code=404, detail="Registro de tutorial não encontrado!")
    return tutorial


@router.put("/{id}", tags=["Rotas de Tutoriais"])
def atualizar_registro_tutorial(id : int, dados : TutorialUpdate, session : Session = Depends(get_session)):
    tutorial = session.get(Tutorial, id)
    if not tutorial:
        raise HTTPException(status_code=404, detail="Registro de tutorial não encontrado!")
    dados_dict = dados.dict(exclude_unset=True) #exclude_unset=True ignora os campos que nao foram passados
    for chave, valor in dados_dict.items():
        setattr(tutorial, chave, valor) #o mesmo que fazer tutorial.chave = valor
    
    session.add(tutorial)
    session.commit()
    session.refresh(tutorial)
    return tutorial

@router.delete("/{id}", status_code=status.HTTP_200_OK, tags=["Rotas de Tutoriais"])
def deletar_registro_tutorial(id : int, session : Session = Depends(get_session)):
    tutorial = session.get(Tutorial, id)
    if not tutorial:
        raise HTTPException(status_code=404, detail="Registro de tutorial não encontrado!")
    
    session.delete(tutorial)
    session.commit()
    return {"mensagem":"Registro de tutorial deletado com sucesso!"}