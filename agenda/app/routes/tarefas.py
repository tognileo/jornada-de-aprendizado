from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.tarefa import Tarefa
from app.models.usuario import Usuario
from app.routes.auth import usuario_atual
from app.schemas.tarefa import TarefaEdicao, TarefaNova, TarefaResposta

router = APIRouter(prefix="/tarefas", tags=["Tarefas"])


def _buscar(db: Session, usuario: Usuario, tarefa_id: int) -> Tarefa:
    tarefa = db.get(Tarefa, tarefa_id)
    if not tarefa or tarefa.usuario_id != usuario.id:  # só enxerga as próprias
        raise HTTPException(status_code=404, detail="Tarefa não encontrada.")
    return tarefa


def _salvar(db: Session, tarefa: Tarefa) -> Tarefa:
    db.add(tarefa)
    db.commit()
    db.refresh(tarefa)
    return tarefa


@router.get("", response_model=list[TarefaResposta])
def listar(db: Session = Depends(get_db), usuario: Usuario = Depends(usuario_atual)):
    consulta = select(Tarefa).where(Tarefa.usuario_id == usuario.id)
    return db.scalars(consulta.order_by(Tarefa.data_prevista, Tarefa.id)).all()


@router.post("", response_model=TarefaResposta, status_code=201)
def criar(dados: TarefaNova, db: Session = Depends(get_db), usuario: Usuario = Depends(usuario_atual)):
    return _salvar(db, Tarefa(usuario_id=usuario.id, **dados.model_dump()))


@router.patch("/{tarefa_id}", response_model=TarefaResposta)
def editar(tarefa_id: int, dados: TarefaEdicao, db: Session = Depends(get_db), usuario: Usuario = Depends(usuario_atual)):
    tarefa = _buscar(db, usuario, tarefa_id)
    for campo, valor in dados.model_dump(exclude_unset=True).items():
        setattr(tarefa, campo, valor)
    return _salvar(db, tarefa)


@router.post("/{tarefa_id}/iniciar", response_model=TarefaResposta)
def iniciar(tarefa_id: int, db: Session = Depends(get_db), usuario: Usuario = Depends(usuario_atual)):
    tarefa = _buscar(db, usuario, tarefa_id)
    tarefa.status = "em_andamento"
    return _salvar(db, tarefa)


@router.post("/{tarefa_id}/concluir", response_model=TarefaResposta)
def concluir(tarefa_id: int, db: Session = Depends(get_db), usuario: Usuario = Depends(usuario_atual)):
    tarefa = _buscar(db, usuario, tarefa_id)
    tarefa.status = "concluida"
    return _salvar(db, tarefa)


@router.delete("/{tarefa_id}", status_code=204)
def excluir(tarefa_id: int, db: Session = Depends(get_db), usuario: Usuario = Depends(usuario_atual)):
    db.delete(_buscar(db, usuario, tarefa_id))
    db.commit()
    return Response(status_code=204)
