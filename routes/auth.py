from fastapi import APIRouter, HTTPException
from models.usuario import Usuario
from security.hash import gerar_hash_senha, verificar_senha
from security.auth_handler import criar_token
from database.db import usuarios_db
from service.utils.bot_telegram import enviar_mensagem

router = APIRouter()

@router.post("/register")
def registrar_usuario(usuario: Usuario):
    if usuario.username in usuarios_db:
        raise HTTPException(status_code=400, detail="Usuário já cadastrado")
    
    usuarios_db[usuario.username] = gerar_hash_senha(usuario.senha)
    enviar_mensagem(f'Novo Usuário Cadastrado! {usuario.username}')
    return {"mensagem": "Usuário registrado com sucesso"}

@router.post("/login")
def login(usuario: Usuario):
    if usuario.username not in usuarios_db:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    hash_senha = usuarios_db[usuario.username]
    if not verificar_senha(usuario.senha, hash_senha):
        raise HTTPException(status_code=401, detail="Senha incorreta")
    # Acesso login e senha valido...
    
    token = criar_token(usuario.username)
    enviar_mensagem(f'Usuário logado no sistema agora: {usuario.username}')
    return {"access_token": token}
