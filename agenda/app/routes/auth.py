from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.usuario import Usuario
from app.schemas.tarefa import LoginDados
from app.schemas.usuario import UsuarioResposta
from app.services.seguranca import criar_token, ler_token, verificar_senha

router = APIRouter(prefix="/auth", tags=["Login"])


def usuario_atual(authorization: str = Header(default=""), db: Session = Depends(get_db)):
    """Descobre quem está logado a partir do token enviado pelo navegador."""
    uid = ler_token(authorization.removeprefix("Bearer "))
    usuario = db.get(Usuario, uid) if uid else None
    if not usuario:
        raise HTTPException(status_code=401, detail="Sessão inválida. Entre novamente.")
    return usuario


@router.post("/login")
def login(dados: LoginDados, db: Session = Depends(get_db)):
    usuario = db.scalar(select(Usuario).where(Usuario.email == dados.email.strip().lower()))
    if not usuario or not verificar_senha(dados.senha, usuario.senha_hash):
        raise HTTPException(status_code=401, detail="E-mail ou senha incorretos.")
    return {"token": criar_token(usuario.id), "usuario": UsuarioResposta.model_validate(usuario)}


@router.get("/eu", response_model=UsuarioResposta)
def quem_sou_eu(usuario: Usuario = Depends(usuario_atual)):
    return usuario
