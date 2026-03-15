import requests

BASE_URL = "http://localhost:8000"


def print_response(label: str, response: requests.Response):
    print(f"\n[{response.status_code}] {label}")
    if response.status_code == 204:
        print("  ✅ Deleted successfully")
    elif response.ok:
        print(f"  ✅ {response.json()}")
    else:
        print(f"  ❌ Error: {response.json().get('detail', response.text)}")


class AuthorRequest:
    def __init__(self):
        self.base_url = BASE_URL

    def create_author(self, name: str, email: str) -> requests.Response:
        res = requests.post(f"{self.base_url}/authors/", json={"name": name, "email": email})
        print_response(f"Create author: {name}", res)
        return res

    def get_all_authors(self) -> requests.Response:
        res = requests.get(f"{self.base_url}/authors/")
        print_response("Get all authors", res)
        if res.ok:
            for author in res.json():
                print(f"  → id: {author['id']} | {author['name']} | {author['email']} | todos: {len(author['todos'])}")
        return res

    def get_author_by_id(self, author_id: int) -> requests.Response:
        res = requests.get(f"{self.base_url}/authors/{author_id}")
        print_response(f"Get author id: {author_id}", res)
        return res

    def delete_author(self, author_id: int) -> requests.Response:
        res = requests.delete(f"{self.base_url}/authors/{author_id}")
        print_response(f"Delete author id: {author_id}", res)
        return res


class TodoRequest:
    def __init__(self):
        self.base_url = BASE_URL

    def create_todo(self, title: str, author_id: int, description: str = None) -> requests.Response:
        res = requests.post(f"{self.base_url}/todos/", json={
            "title": title,
            "author_id": author_id,
            "description": description
        })
        print_response(f"Create todo: {title}", res)
        return res

    def get_all_todos(self) -> requests.Response:
        res = requests.get(f"{self.base_url}/todos/")
        print_response("Get all todos", res)
        if res.ok:
            for todo in res.json():
                status = "✅" if todo["completed"] else "⏳"
                print(f"  {status} id: {todo['id']} | {todo['title']} | author: {todo['author']['name']}")
        return res

    def get_todo_by_id(self, todo_id: int) -> requests.Response:
        res = requests.get(f"{self.base_url}/todos/{todo_id}")
        print_response(f"Get todo id: {todo_id}", res)
        return res

    def delete_todo(self, todo_id: int) -> requests.Response:
        res = requests.delete(f"{self.base_url}/todos/{todo_id}")
        print_response(f"Delete todo id: {todo_id}", res)
        return res

    def update_todo(self, todo_id: int, **fields) -> requests.Response:
        res = requests.patch(f"{self.base_url}/todos/{todo_id}", json=fields)
        print_response(f"Update todo id: {todo_id} → {fields}", res)
        return res


if __name__ == "__main__":

    # NOTA: PARA PODER EJECUTAR ESTE TEST DE MANERA CORRECTA, ES NECESARIO LIMPIAR LA BASE DE DATOS ANTES DE EJECUTAR EL TEST.

    author_client = AuthorRequest()
    todo_client   = TodoRequest()

    # Creamos los dos autores
    enmanuel_response = author_client.create_author("Enmanuel Alejandro De Oleo", "guest@pontia.com")
    john_response     = author_client.create_author("Juan Ortiz", "guest22@pontia.com")

    # Salimos si alguno de los autores no se creó correctamente
    if not enmanuel_response.ok or not john_response.ok:
        print("\n❌ No se pudieron crear los autores, abortando... Hay que eliminar los regitros de la base de datos antes de poder ejecutar este script.")
        exit(1)

    enmanuel = enmanuel_response.json()
    john     = john_response.json()

    print("\n--- Autores ---")
    author_client.get_all_authors()

    # Creamos los tres todos
    todo1 = todo_client.create_todo("Ir al gym",            enmanuel["id"], "Trabajar extremidades bajas").json()
    todo2 = todo_client.create_todo("Escribir tests",       enmanuel["id"], "Escribir test para la tarea de pontia").json()
    todo3 = todo_client.create_todo("Revisar pull request", john["id"],     "Revisar el pull request de la rama").json()

    print("\n--- Todos ---")
    todo_client.get_all_todos()

    # Actualizamos un todo
    todo_client.update_todo(todo1["id"], completed=True)

    # Renombramos un todo
    todo_client.update_todo(todo2["id"], title="Write integration tests")

    # Borramos un todo
    todo_client.delete_todo(todo3["id"])

    print("\n--- Todos despues de borrar un todo ---")
    todo_client.get_all_todos()

    # Borramos a Juan
    author_client.delete_author(john["id"])

    print("\n--- Autores despues de borrar a Juan ---")
    author_client.get_all_authors()