from pydantic import BaseModel
from datetime import datetime

class Task(BaseModel):
    task_id: str
    task_name: str
