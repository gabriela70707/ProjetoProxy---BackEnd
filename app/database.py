#Gerencia a conexão com o banco de dados
#Esse arquivo cuida da criação do banco de dados e das sessoes de acesso

from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = 'sqlite:///./projeto_proxy.db'

engine = create_engine(DATABASE_URL, echo=True)

def criar_banco(): #cria as tabelas do banco baseadas nos models
    SQLModel.metadata.create_all(engine)


def get_session(): #pega uma sessão do banco de dados
    with Session(engine) as session:
        yield session