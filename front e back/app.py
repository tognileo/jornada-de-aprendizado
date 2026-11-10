
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from conexao import conectar

app = FastAPI()


class Pessoa(BaseModel):
    nome: str
    cidade: str
    email: str
    telefone: str
    rua: str
    numero_casa: str
    complemento: str
    bairro: str
    cep: str


@app.get("/pessoas")
def listar_pessoas():
    banco = conectar()
    cursor = banco.cursor(dictionary=True)

    cursor.execute("SELECT * FROM cadastro ORDER BY id")
    pessoas = cursor.fetchall()

    cursor.close()
    banco.close()

    return pessoas


@app.post("/pessoas")
def cadastrar_pessoa(pessoa: Pessoa):
    banco = conectar()
    cursor = banco.cursor()

    sql = "INSERT INTO cadastro (nome, cidade,email,telefone,rua,numero_casa,complemento,bairro,cep) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, (pessoa.nome, pessoa.cidade, pessoa.email, pessoa.telefone, pessoa.rua, pessoa.numero_casa, pessoa.complemento, pessoa.bairro, pessoa.cep))

    banco.commit()
    cursor.close()
    banco.close()

    return {"mensagem": "Pessoa cadastrada com sucesso"}


@app.put("/pessoas/{id}")
def atualizar_pessoa(id: int, pessoa: Pessoa):
    banco = conectar()
    cursor = banco.cursor()

    sql = """
        UPDATE cadastro
        SET nome = %s, cidade = %s, email = %s, telefone = %s, rua = %s, numero_casa = %s, complemento = %s, bairro = %s, cep = %s 
        WHERE id = %s

    """
    cursor.execute(sql, (pessoa.nome, pessoa.cidade,pessoa.email,pessoa.telefone, pessoa.rua, pessoa.numero_casa, pessoa.complemento, pessoa.bairro, pessoa.cep,id))

    banco.commit()
    cursor.close()
    banco.close()

    return {"mensagem": "Pessoa atualizada com sucesso"}


@app.delete("/pessoas/{id}")
def excluir_pessoa(id: int):
    banco = conectar()
    cursor = banco.cursor()

    cursor.execute("DELETE FROM cadastro WHERE id = %s", (id,))

    banco.commit()
    cursor.close()
    banco.close()

    return {"mensagem": "Pessoa excluída com sucesso"}


app.mount(
    "/",
    StaticFiles(directory="static", html=True),
    name="static"
)

