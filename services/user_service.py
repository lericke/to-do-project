from datetime import datetime
from db.database import load_data, save_data

class TaskEngine:

    def create_task(name: str):
        data = load_data()
        new_id = max([u["id"] for u in data], default=0) + 1
        task_date = datetime
        new_task = {"id": new_id, "task_name": name, "date": task_date}
        data.append(new_task)
        save_data(data)
        return new_task 