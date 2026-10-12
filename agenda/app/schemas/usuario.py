from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class UsuarioCadastro(BaseModel):
    """Dados que o usuário envia para criar a conta."""

    nome: str = Field(min_length=2, max_length=100)
    email: str = Field(max_length=150, pattern=r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
    senha: str = Field(min_length=8, max_length=128)


class UsuarioResposta(BaseModel):
    """Dados que a API devolve. Repare: NÃO tem senha nem senha_hash."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    nome: str
    email: str
    criado_em: datetime
