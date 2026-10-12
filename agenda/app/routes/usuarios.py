from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.usuario import UsuarioCadastro, UsuarioResposta
from app.services.usuario_service import EmailJaCadastrado, criar_usuario

router = APIRouter(prefix="/usuarios", tags=["Usuários"])


@router.post("", response_model=UsuarioResposta, status_code=201)
def cadastrar_usuario(dados: UsuarioCadastro, db: Session = Depends(get_db)):
    try:
        return criar_usuario(db, dados)
    except EmailJaCadastrado:
        raise HTTPException(status_code=409, detail="Este e-mail já está cadastrado.")
