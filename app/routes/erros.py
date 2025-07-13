#importe de bibliotecas externas
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import List, Optional

#importe de arquivos do projeto
from app.database import get_session
from app.schemas.erros import ErroCreate, ErroRead, ErroUpdate, CategoriaEnum
from app.models.erros import Erro

router = APIRouter(prefix="/erros")

@router.post("/", status_code=status.HTTP_201_CREATED, tags=["Rotas dos Erros"])
def criar_erro(dados : ErroCreate, session : Session = Depends(get_session)):
    novo = Erro(**dados.dict())
    session.add(novo)
    session.commit() #salva no banco de dados
    session.refresh(novo) #pega o objeto como foi salvo no banco de dados
    return novo

@router.get("/", response_model=List[ErroRead], tags=["Rotas dos Erros"])
def listar_erros(session : Session = Depends(get_session)):
    return session.query(Erro).all()


#Rota para barra de pesquisa
@router.get("/buscar", response_model=List[ErroRead], tags=["Filtros"])
def procurar_erro(palavra: str, session : Session = Depends(get_session)):
    procura = select(Erro).where(Erro.palavras_chaves.contains(palavra)) #.contains(palavra): procura registros onde o campo palavras_chaves contém a palavra digitada
    resultados = session.exec(procura).all()
    return resultados

# filtro para retornar os erros em que há ou não interferencia do proxy
@router.get("/proxy", response_model=List[ErroRead], tags=["Filtros"])
def filtrar_erros_por_proxy(proxy : Optional[bool] = None, session : Session = Depends(get_session)):
    filtro = select(Erro)
    if proxy is not None:
        filtro = filtro.where(Erro.proxy == proxy)
    resultados = session.exec(filtro).all()
    return resultados

'''
Exemplo de requisição com o filtro de proxy:
Para buscar apenas erros com proxy = True: GET /erros/proxy?proxy=true
Para buscar erros com proxy = False: GET /erros/proxy?proxy=false
Se não passar nada: GET /erros ou /erros/proxy: retorna todos os erros sem filtro.
'''


# Filtro por categoria de erro (Front e Back)
# Mesma dinamica de requisicao que o filtro do proxy
@router.get("/categoria", response_model=List[ErroRead], tags=["Filtros"])
def filtrar_erros_por_categoria(categoria : Optional[CategoriaEnum] = None, session : Session = Depends(get_session)):
    filtro = select(Erro)
    if categoria is not None: #verifica se categoria foi passada na url
        filtro = filtro.where(Erro.categoria == categoria)
    
    resultados = session.exec(filtro).all()
    return resultados


# Buscar por um erro especifico
@router.get("/{id}", response_model=ErroRead, tags=["Rotas dos Erros"])
def buscar_erro(id : int, session : Session = Depends(get_session)):
    erro = session.get(Erro, id)
    if not erro:
        raise HTTPException(status_code=404, detail="Registro de erro não encontrado!")
    return erro


@router.put("/{id}", tags=["Rotas dos Erros"])
def atualizar_registro_erro(id : int, dados : ErroUpdate, session : Session = Depends(get_session)):
    erro = session.get(Erro, id)
    if not erro:
        raise HTTPException(status_code=404, detail="Registro de erro não encontrado")
    
    dados_dict = dados.dict(exclude_unset=True)
    for chave , valor in dados_dict.items():
        setattr(erro, chave, valor)

    session.add(erro)
    session.commit()
    session.refresh(erro)
    return erro

@router.delete("/{id}", status_code=status.HTTP_200_OK, tags=["Rotas dos Erros"])
def deletar_erro(id : int, session : Session = Depends(get_session)):
    erro = session.get(Erro, id)
    if not erro:
        raise HTTPException(status_code=404, detail="Registro de erro não encontrado")
    
    session.delete(erro)
    session.commit()
    return {"mensagem":"Registro de erro deletado com sucesso"}