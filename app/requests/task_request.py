import requests
from utils import print_response
BASE_URL = "http://localhost:8000"


class TaskRequest:
    def __init__(self):
        self.base_url = BASE_URL

    def create_task(self, titulo: str, author_id: int, contenido: str = None, deadline: str = None) -> requests.Response:
        res = requests.post(f"{self.base_url}/tasks/", json={
            "titulo": titulo,
            "author_id": author_id,
            "contenido": contenido,
            "deadline": deadline
        })
        print_response(f"Create task: {titulo}", res)
        return res

    def get_all_tasks(self) -> requests.Response:
        res = requests.get(f"{self.base_url}/tasks/")
        print_response("Get all tasks", res)
        if res.ok:
            for task in res.json():
                status = "✅" if task["completada"] else "⏳"
                print(f"  {status} id: {task['id']} | {task['titulo']} | author: {task['author']['nombre']}")
        return res

    def get_task_by_id(self, task_id: int) -> requests.Response:
        res = requests.get(f"{self.base_url}/tasks/{task_id}")
        print_response(f"Get task id: {task_id}", res)
        return res

    def delete_task(self, task_id: int) -> requests.Response:
        res = requests.delete(f"{self.base_url}/tasks/{task_id}")
        print_response(f"Delete task id: {task_id}", res)
        return res

    def complete_task(self, task_id: int) -> requests.Response:
        res = requests.put(f"{self.base_url}/tasks/{task_id}/completar")
        print_response(f"Complete task id: {task_id}", res)
        return res

    def get_expired_tasks(self) -> requests.Response:
        res = requests.get(f"{self.base_url}/tasks/caducadas")
        return res