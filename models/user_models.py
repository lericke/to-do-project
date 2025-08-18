from pydantic import BaseModel
from datetime import datetime

class Task(BaseModel):
    task_id: int
    task_name: str
