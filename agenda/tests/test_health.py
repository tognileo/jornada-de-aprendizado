from fastapi.testclient import TestClient

from app import main

client = TestClient(main.app)


def test_health():
    resposta = client.get("/health")
    assert resposta.status_code == 200
    assert resposta.json()["status"] == "ok"


def test_health_database_conectado(monkeypatch):
    monkeypatch.setattr(main, "testar_conexao", lambda: True)
    resposta = client.get("/health/database")
    assert resposta.status_code == 200


def test_health_database_sem_conexao(monkeypatch):
    monkeypatch.setattr(main, "testar_conexao", lambda: False)
    resposta = client.get("/health/database")
    assert resposta.status_code == 503
