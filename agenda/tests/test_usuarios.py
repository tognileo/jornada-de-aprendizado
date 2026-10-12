from datetime import datetime
from types import SimpleNamespace

from fastapi.testclient import TestClient

from app.main import app
from app.routes import usuarios
from app.database.session import get_db
from app.services.seguranca import gerar_hash
from app.services.usuario_service import EmailJaCadastrado

DADOS_OK = {"nome": "Leo", "email": "leo@exemplo.com", "senha": "senha12345"}


def _sem_banco():
    # Estes testes não usam o MySQL de verdade
    yield None


app.dependency_overrides[get_db] = _sem_banco
client = TestClient(app)


def test_hash_nao_guarda_a_senha_pura():
    h1 = gerar_hash("senha12345")
    h2 = gerar_hash("senha12345")
    assert "senha12345" not in h1
    assert h1 != h2  # o 'sal' faz cada hash ser diferente


def test_cadastro_com_senha_curta_e_recusado():
    resposta = client.post("/usuarios", json={**DADOS_OK, "senha": "123"})
    assert resposta.status_code == 422


def test_cadastro_com_email_invalido_e_recusado():
    resposta = client.post("/usuarios", json={**DADOS_OK, "email": "isso-nao-e-email"})
    assert resposta.status_code == 422


def test_cadastro_ok_nao_devolve_senha(monkeypatch):
    falso = SimpleNamespace(
        id=1, nome="Leo", email="leo@exemplo.com", criado_em=datetime.now()
    )
    monkeypatch.setattr(usuarios, "criar_usuario", lambda db, dados: falso)

    resposta = client.post("/usuarios", json=DADOS_OK)

    assert resposta.status_code == 201
    corpo = resposta.json()
    assert corpo["email"] == "leo@exemplo.com"
    assert "senha" not in corpo
    assert "senha_hash" not in corpo


def test_cadastro_com_email_repetido_retorna_409(monkeypatch):
    def repetido(db, dados):
        raise EmailJaCadastrado()

    monkeypatch.setattr(usuarios, "criar_usuario", repetido)
    resposta = client.post("/usuarios", json=DADOS_OK)
    assert resposta.status_code == 409
