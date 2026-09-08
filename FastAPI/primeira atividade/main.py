from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def leitura_rota():
    return {"mensagem": "primeira rota rodando"}


@app.get("/sobre")
def sobre ():                                                       
    return {"curso":"jovem programador"},{"leonardo":"16 anos"}



@app.get("/sobre/{nome}")
def sobre_personalizado(nome:str):
    return {"curso": "jovem programador", "leonardo": "16 anos"}

#para rodar abre o terminal e digita: python -m uvicorn main:app --reload

