from fastapi import APIRouter, HTTPException
from models.usuario import Usuario
from security.hash import gerar_hash_senha, verificar_senha
from security.auth_handler import criar_token
from database.db import usuarios_db

router = APIRouter()

@router.post("/register")
def registrar_usuario(usuario: Usuario):
    if usuario.username in usuarios_db:
        raise HTTPException(status_code=400, detail="Usuário já cadastrado")
    
    usuarios_db[usuario.username] = gerar_hash_senha(usuario.senha)
    return {"mensagem": "Usuário registrado com sucesso"}

@router.post("/login")
def login(usuario: Usuario):
    if usuario.username not in usuarios_db:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    hash_senha = usuarios_db[usuario.username]
    if not verificar_senha(usuario.senha, hash_senha):
        raise HTTPException(status_code=401, detail="Senha incorreta")
    
    token = criar_token(usuario.username)
    return {"access_token": token}
