#importe de bibliotecas externas
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#importe dos arquivos criados no projeto
from .database import criar_banco
from app.routes import erros, tutoriais

app = FastAPI()

#configuração do cors para permitir a conexão com o front-end
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"]
)

#Essa função é executada automaticamente assim que o servidor inicia
@app.on_event("startup") #garente que o banco de dados e as tabelas vão ser criadas quando o banco iniciar
def on_startup():
    criar_banco()

@app.get("/")
def root():
    return {"mensagem":"API está rodando!!"}


#inclusão das rotas:
app.include_router(erros.router)
