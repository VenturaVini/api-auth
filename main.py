from fastapi import FastAPI
from routes import auth, produtos

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(produtos.router, tags=["Produtos"])

if __name__ == "__main__":
    import uvicorn
    import os
    #uvicorn.run(app, host="0.0.0.0", port=7000)


    port = int(os.getenv("PORT", 7000))  # Usa a porta definida pelo Railway
    uvicorn.run(app, host="0.0.0.0", port=port)