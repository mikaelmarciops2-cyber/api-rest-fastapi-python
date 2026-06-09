# API REST com FastAPI

Projeto de API REST desenvolvido em Python utilizando FastAPI.

## Funcionalidades

- Criar usuários
- Listar usuários
- Buscar usuário por ID
- Atualizar usuário
- Remover usuário
- Documentação automática com Swagger

## Tecnologias

- Python 3
- FastAPI
- Uvicorn
- Pydantic

## Instalação

```bash
python -m pip install -r requirements.txt
```

Executar:
python -m uvicorn main:app --reload
Documentação

Acesse:

http://127.0.0.1:8000/docs

Rotas:
Método	      Rota	      Descrição
GET	      /	Página        inicial
GET	      /usuarios	      Listar usuários
GET	     /usuarios/{id}	  Buscar usuário
POST	   /usuarios	      Criar usuário
PUT	     /usuarios/{id}	  Atualizar usuário
DELETE	  /usuarios/{id}	Remover usuário

Estrutura:
api-rest-fastapi-python/
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
