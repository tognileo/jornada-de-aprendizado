from datetime import date
from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, Field

Prioridade = Literal["baixa", "media", "alta"]
Status = Literal["pendente", "em_andamento", "concluida"]


class TarefaNova(BaseModel):
    titulo: str = Field(min_length=1, max_length=150)
    descricao: Optional[str] = Field(default=None, max_length=2000)
    categoria: Optional[str] = Field(default=None, max_length=50)
    prioridade: Prioridade = "media"
    data_prevista: date
    tempo_estimado_min: int = Field(default=30, ge=0, le=1440)


class TarefaEdicao(BaseModel):
    """Todos os campos são opcionais: só muda o que for enviado."""

    titulo: Optional[str] = Field(default=None, min_length=1, max_length=150)
    descricao: Optional[str] = Field(default=None, max_length=2000)
    categoria: Optional[str] = Field(default=None, max_length=50)
    prioridade: Optional[Prioridade] = None
    data_prevista: Optional[date] = None
    tempo_estimado_min: Optional[int] = Field(default=None, ge=0, le=1440)
    status: Optional[Status] = None


class TarefaResposta(TarefaNova):
    model_config = ConfigDict(from_attributes=True)

    id: int
    status: Status


class LoginDados(BaseModel):
    email: str = Field(max_length=150)
    senha: str = Field(max_length=128)
