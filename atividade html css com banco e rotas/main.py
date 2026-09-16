from database import session_local
from fastapi import FastAPI
from pydantic import BaseModel
from classe import Produto
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/produto")
def produto_rota():
    session = session_local()
    cliente = session.query(Produto).all()
    resultado = [{"cpf":i.cpf,
                   "nome":i.nome,
                   "email":i.email,
                   "senha":i.senha,
                   "data_cadastro":i.data_cadastro}for i in cliente]

    return resultado












































