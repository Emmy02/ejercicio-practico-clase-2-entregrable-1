# task_manager.py
import requests
from datetime import datetime, timedelta
from app.requests.author_request import AuthorRequest
from app.requests.task_request import TaskRequest
from utils import assert_ok

class TaskManager:
    """
    Encapsula la lógica de negocio por encima de las llamadas HTTP.
    Decide cuándo crear, completar, o limpiar tareas según reglas de negocio.
    """

    def __init__(self):
        self._author_client = AuthorRequest()
        self._task_client   = TaskRequest()

    def registrar_autor(self, nombre: str, correo: str) -> dict:
        """Crea un autor y devuelve sus datos. Lanza error si falla."""
        res = self._author_client.create_author(nombre, correo)
        assert_ok(res, 201)
        return res.json()

    def eliminar_autor(self, author_id: int):
        """Elimina un autor y verifica que ya no existe."""
        res = self._author_client.delete_author(author_id)
        assert res.status_code == 204
        verify = self._author_client.get_author_by_id(author_id)
        assert verify.status_code == 404

    def crear_tarea(self, titulo: str, author_id: int, contenido: str = None, deadline: str = None) -> dict:
        """Crea una tarea y verifica que se creó correctamente."""
        res = self._task_client.create_task(titulo, author_id, contenido, deadline)
        assert_ok(res, 201)
        return res.json()

    def crear_tarea_expirada(self, titulo: str, author_id: int, contenido: str = None) -> dict:
        """Crea una tarea con deadline de ayer — útil para probar expiración."""
        ayer = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%S")
        return self.crear_tarea(titulo, author_id, contenido, deadline=ayer)

    def crear_tarea_futura(self, titulo: str, author_id: int, contenido: str = None, dias: int = 7) -> dict:
        """Crea una tarea con deadline en el futuro."""
        futuro = (datetime.now() + timedelta(days=dias)).strftime("%Y-%m-%dT%H:%M:%S")
        return self.crear_tarea(titulo, author_id, contenido, deadline=futuro)

    def completar_tarea(self, task_id: int) -> dict:
        """Marca una tarea como completada y verifica el resultado."""
        res = self._task_client.complete_task(task_id)
        assert_ok(res)
        assert res.json()["completada"] is True
        return res.json()

    def eliminar_tarea(self, task_id: int):
        """Elimina una tarea y verifica que ya no existe."""
        res = self._task_client.delete_task(task_id)
        assert res.status_code == 204
        verify = self._task_client.get_task_by_id(task_id)
        assert verify.status_code == 404

    def obtener_tareas_expiradas(self) -> list:
        """Devuelve la lista de tareas expiradas."""
        res = self._task_client.get_expired_tasks()
        assert_ok(res)
        return res.json()

    def verificar_total_tareas(self, esperado: int):
        """Verifica que el total de tareas en el sistema sea el esperado."""
        res = self._task_client.get_all_tasks()
        assert_ok(res)
        assert len(res.json()) == esperado, (
            f"Expected {esperado} tasks, got {len(res.json())}"
        )

    def verificar_total_autores(self, esperado: int):
        """Verifica que el total de autores en el sistema sea el esperado."""
        res = self._author_client.get_all_authors()
        assert_ok(res)
        assert len(res.json()) == esperado, (
            f"Expected {esperado} authors, got {len(res.json())}"
        )