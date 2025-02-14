import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException, Header

SECRET_KEY = "K0a0o2uFSibTS1voDdooY68CWDy51QT_LPA_tWdfCbc"

def criar_token(username: str) -> str:
    payload = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(hours=0.025)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def verificar_token(token: str) -> str:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido")

def obter_usuario_logado(Authorization: str = Header(...)):
    #token = Authorization.split(" ")[1]
    token = Authorization # passa so so token do Bearer
    return verificar_token(token)
