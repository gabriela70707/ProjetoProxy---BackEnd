# 🧠 Centralizador de Erros e Tutoriais para Devs

Este projeto foi criado com o objetivo de reunir e organizar os erros mais comuns que acontecem em projetos de programação — tanto no **Back-End** quanto no **Front-End** — e fornecer **tutoriais práticos** sobre como iniciar projetos nas principais stacks.

Você encontrará:
- 📋 Registros de erros com descrição, solução e palavras-chave.
- 📚 Tutoriais como "Como iniciar um projeto em React" ou "Configurando um projeto FastAPI".
- 🔎 Filtros por categoria (Front ou Back), pesquisa por palavras-chave e identificação de erros relacionados a **proxy**.

---

## 🚀 Como rodar o projeto

1. Crie e ative um ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate      # Windows

2. Instale as dependências
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o servidor:
   ```bash
   uvicorn app.main:app --reload
   ```

### 🧭 Obs:

app = nome da pasta principal

main = nome do arquivo com a instância da aplicação

app (último) = instância do FastAPI

## 📄 Documentação da API
A documentação interativa está disponível em:
http://127.0.0.1:8000/docs

Lá você pode testar os endpoints, ver os campos esperados e navegar por todas as funcionalidades.

## ✨ Funcionalidades principais

Registro de erros com categorização (Front-End ou Back-End)

Busca por palavras-chave

Filtro por interferência de proxy

Registro de tutoriais técnicos

Atualização e exclusão de registros

Documentação automática com Swagger

## 🛠 Tecnologias usadas

FastAPI – API rápida e moderna

SQLModel – ORM leve e poderoso

Uvicorn – Servidor ASGI

Pydantic – Validação de dados

Python 3.11+
