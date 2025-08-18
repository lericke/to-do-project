from fastapi import APIRouter
from models.user_models import Task
from services.user_service import TaskEngine

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.post("/tarefa/cria_tarefa/{titulo}")
def criar_tarefa(titulo:str, data: Task):
    return  TaskEngine.create_task(titulo)

@router.get("/tarefa/get_task_by_id")
def get_task_id():
    pass

@router.get("/tarefa/lista_tarefas_do_dia")
def lista_tarefas_do_dia():
    pass

@router.get("/tarefa/lista_todas_tarefas")
def lista_todas_tarefas():
    pass

@router.put("/tarefa/atualiza_tarefa")
def atualiza_tarefa():
    pass

@router.delete("/tarefa/deleta_tarefa")
def deleta_tarefa():
    pass