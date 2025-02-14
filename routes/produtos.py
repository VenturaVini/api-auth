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


@router.put("/produtos/{produtoid}", dependencies=[ Depends(obter_usuario_logado)])
def modificar_produto( produto_id: int, produto: dict):
    
    for index, p in enumerate(lista_produtos['produtos']):
        if p['id'] == produto_id:
            lista_produtos['produtos'][index] = produto.dict()
            return({'mensagem':'Produto atualizado com sucesso'})
        
    raise HTTPException(status_code= 404, detail="Produto não encontrado")


@router.delete("/produtos/{produtoid}", dependencies=[Depends(obter_usuario_logado)])
def remover_produto(produtoid : int):

    for index, p in enumerate(lista_produtos['produto']):
        if p['id'] == produtoid:
            del lista_produtos['produtos'][index]
            return {'mensagem': 'Produto removido com sucesso'}
        
    raise HTTPException(status_code= 404, detail= 'Produto não encontrado')
