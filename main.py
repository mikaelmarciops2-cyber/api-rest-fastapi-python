from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Modelo 
class Usuario(BaseModel):
    nome: str

# Banco de memória
@app.get("/")
def inicio():
    return {"mensagem": "API funcionando!"}

# Listar usuários
@app.get("/usuarios")
def listar_usuarios():
    return usuarios

# Buscar usuários por ID
@app.get("/usuarios/{id}")
def buscar_usuarios(id: int):

    if id < 0 or id >= len(usuarios):
      raise HTTPException(status_code=404, detail="Usuário não encontrado")

      return usuarios[id]

# Criar usuário
@app.post("/usuarios")
def criar_usuarios(usuario: Usuario):

    usuarios.append(usuario.dict())

    return {
        "mensagem": "Usuário criado com sucesso",
        "usuario": usuario
    }  

# Atualizar usuário
@app.put("/usuarios/{id}")
def atualizar_usuario(id: int, usuario: Usuario):

    if id < 0 or id >= len(usuarios):
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

        usuarios[id] = usuario.dict()

        return {
            "mensagem": "Usuário atualizado com sucesso",
            "usuario": usuarios[id]
        }

# Deletar usuário
@app.delete("/usuarios/{id}")
def deletar_usuario(id: int):

    if id < 0 or id >= len(usuarios):
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    removido = usuarios.pop(id)

    return {
        "mensagem": "Usuário deletado com sucesso",
        "usuario": removido
    }