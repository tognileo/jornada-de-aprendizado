from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCadastro
from app.services.seguranca import gerar_hash


class EmailJaCadastrado(Exception):
    pass


def criar_usuario(db: Session, dados: UsuarioCadastro) -> Usuario:
    email = dados.email.strip().lower()

    ja_existe = db.scalar(select(Usuario).where(Usuario.email == email))
    if ja_existe:
        raise EmailJaCadastrado()

    usuario = Usuario(
        nome=dados.nome.strip(),
        email=email,
        senha_hash=gerar_hash(dados.senha),
    )
    db.add(usuario)
    try:
        db.commit()
    except IntegrityError:
        # Protege caso dois cadastros com o mesmo e-mail cheguem juntos
        db.rollback()
        raise EmailJaCadastrado()
    db.refresh(usuario)
    return usuario
