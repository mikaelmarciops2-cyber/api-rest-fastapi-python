# 🚀 API REST com FastAPI

Uma **API REST** desenvolvida em **Python** utilizando o **FastAPI**, com operações básicas de CRUD para gerenciamento de usuários e documentação automática via Swagger.

## ✨ Funcionalidades

- Criar usuários
- Listar todos os usuários
- Buscar usuário por ID
- Atualizar informações de um usuário
- Remover usuários
- Documentação automática com Swagger UI

## 🛠️ Tecnologias

- Python 3.x
- FastAPI
- Uvicorn
- Pydantic

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/api-rest-fastapi-python.git
cd api-rest-fastapi-python
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

## ▶️ Executando a aplicação

Inicie o servidor com:

```bash
python -m uvicorn main:app --reload
```

Após iniciar, a API estará disponível em:

```
http://127.0.0.1:8000
```

## 📖 Documentação da API

O FastAPI gera automaticamente a documentação da API.

- **Swagger UI:** `http://127.0.0.1:8000/docs`
- **ReDoc:** `http://127.0.0.1:8000/redoc`

## 📌 Rotas disponíveis

| Método | Endpoint | Descrição |
|---------|----------|-----------|
| GET | `/` | Página inicial |
| GET | `/usuarios` | Lista todos os usuários |
| GET | `/usuarios/{id}` | Busca um usuário pelo ID |
| POST | `/usuarios` | Cria um novo usuário |
| PUT | `/usuarios/{id}` | Atualiza um usuário |
| DELETE | `/usuarios/{id}` | Remove um usuário |

## 📁 Estrutura do projeto

```text
api-rest-fastapi-python/
├── main.py            # Arquivo principal da API
├── requirements.txt   # Dependências do projeto
├── .gitignore         # Arquivos ignorados pelo Git
└── README.md          # Documentação
```

## 🚀 Possíveis melhorias

- Persistência de dados com SQLite ou PostgreSQL
- Integração com SQLAlchemy
- Autenticação com JWT
- Validação avançada de dados
- Testes automatizados
- Containerização com Docker

## 👨‍💻 Autor

Projeto desenvolvido por **Mikael Márcio Macêdo Silva**.

### Obs:

Este projeto foi desenvolvido por mim com o auxílio do **ChatGPT (OpenAI)**, utilizado como ferramenta de apoio para esclarecer dúvidas, sugerir melhorias e auxiliar na documentação.

## 📄 Licença

Este projeto está disponível sob a licença **MIT**.
