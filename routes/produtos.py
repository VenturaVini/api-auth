from fastapi import APIRouter, Depends, HTTPException
from models.produto import Produto
from database.db import lista_produtos
from security.auth_handler import obter_usuario_logado

router = APIRouter()

@router.get("/")
def listar_produtos():
    return {"lista_produtos": lista_produtos}

@router.post("/produtos/", dependencies=[Depends(obter_usuario_logado)])
def adicionar_produto(produto: Produto):
    for p in lista_produtos["produtos"]:
        if p["id"] == produto.id:
            raise HTTPException(status_code=400, detail="ID já existe")
    
    lista_produtos["produtos"].append(produto.dict())
    return {"mensagem": "Produto adicionado com sucesso"}
