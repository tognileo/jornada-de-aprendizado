from fastapi.testclient import TestClient

from app.database.session import get_db
from app.main import app
from app.services.seguranca import criar_token, gerar_hash, ler_token, verificar_senha


def _sem_banco():
    yield None


app.dependency_overrides[get_db] = _sem_banco
client = TestClient(app)


def test_verificar_senha():
    h = gerar_hash("senha12345")
    assert verificar_senha("senha12345", h)
    assert not verificar_senha("outra-senha", h)


def test_token_valido_e_adulterado():
    token = criar_token(7)
    assert ler_token(token) == 7
    assert ler_token(token[:-1] + "0") is None
    assert ler_token("lixo") is None


def test_tarefas_exigem_login():
    assert client.get("/tarefas").status_code == 401
    assert client.post("/tarefas", json={}).status_code == 401


def test_frontend_e_servido():
    resposta = client.get("/")
    assert resposta.status_code == 200 and "Meu Dia" in resposta.text
