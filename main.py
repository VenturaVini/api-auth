import os
from fastapi import FastAPI
from routes import auth, produtos

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(produtos.router, tags=["Produtos"])

@app.get("/env")
def read_env():
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    CHAT_ID = os.getenv("CHAT_ID")
    SECRET_KEY = os.getenv('SECRET_KEY')
    return {
        "BOT_TOKEN": BOT_TOKEN,
        "CHAT_ID": CHAT_ID,
        "SECRET_KEY": SECRET_KEY
    }

if __name__ == "__main__":
    port = int(os.getenv("PORT", 7000))
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
