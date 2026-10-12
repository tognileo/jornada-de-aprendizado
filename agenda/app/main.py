from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles

from app.core.config import settings
from app.database.connection import testar_conexao
from app.routes import auth, tarefas, usuarios

app = FastAPI(title=settings.app_name)

app.include_router(usuarios.router)
app.include_router(auth.router)
app.include_router(tarefas.router)


@app.get("/health")
def health():
    return {"status": "ok", "app": settings.app_name}


@app.get("/health/database")
def health_database():
    if not testar_conexao():
        # Mensagem genérica: nunca mostrar senha ou detalhes da conexão
        raise HTTPException(
            status_code=503,
            detail="Não foi possível conectar ao banco de dados.",
        )
    return {"status": "ok", "database": settings.db_name}


# O site (HTML/CSS/JS) é servido pelo próprio FastAPI em http://localhost:8000
# Fica por último para não esconder as rotas da API.
PASTA_FRONT = Path(__file__).resolve().parent.parent / "frontend"
app.mount("/", StaticFiles(directory=PASTA_FRONT, html=True), name="frontend")
