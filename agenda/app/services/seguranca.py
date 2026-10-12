import hashlib
import hmac
import os
import time

from app.core.config import settings

ITERACOES = 600_000


def gerar_hash(senha: str) -> str:
    """Transforma a senha em um hash com 'sal' (valor aleatório).

    O mesmo texto gera hashes diferentes a cada vez, e não dá para
    voltar do hash para a senha original.
    """
    sal = os.urandom(16)
    hash_bytes = hashlib.pbkdf2_hmac("sha256", senha.encode("utf-8"), sal, ITERACOES)
    return f"pbkdf2_sha256${ITERACOES}${sal.hex()}${hash_bytes.hex()}"


def verificar_senha(senha: str, senha_hash: str) -> bool:
    try:
        _, iteracoes, sal, esperado = senha_hash.split("$")
        calculado = hashlib.pbkdf2_hmac(
            "sha256", senha.encode("utf-8"), bytes.fromhex(sal), int(iteracoes)
        )
        return hmac.compare_digest(calculado.hex(), esperado)
    except ValueError:
        return False


# Token de login: "id.validade.assinatura" (assinado com a SECRET_KEY do .env)
def _assinar(texto: str) -> str:
    chave = settings.secret_key.encode("utf-8")
    return hmac.new(chave, texto.encode("utf-8"), hashlib.sha256).hexdigest()


def criar_token(usuario_id: int, horas: int = 12) -> str:
    texto = f"{usuario_id}.{int(time.time()) + horas * 3600}"
    return f"{texto}.{_assinar(texto)}"


def ler_token(token: str):
    """Devolve o id do usuário se o token for válido, senão None."""
    try:
        uid, validade, assinatura = token.split(".")
        if not hmac.compare_digest(_assinar(f"{uid}.{validade}"), assinatura):
            return None
        return int(uid) if int(validade) > time.time() else None
    except ValueError:
        return None
