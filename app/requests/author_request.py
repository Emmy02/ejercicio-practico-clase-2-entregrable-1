import requests
from utils import print_response
BASE_URL = "http://localhost:8000"

class AuthorRequest:
    def __init__(self):
        self.base_url = BASE_URL

    def create_author(self, nombre: str, correo: str) -> requests.Response:
        res = requests.post(f"{self.base_url}/authors/", json={"nombre": nombre, "correo": correo})
        print_response(f"Create author: {nombre}", res)
        return res

    def get_all_authors(self) -> requests.Response:
        res = requests.get(f"{self.base_url}/authors/")
        print_response("Get all authors", res)
        if res.ok:
            for author in res.json():
                print(f"  → id: {author['id']} | {author['nombre']} | {author['correo']} | tasks: {len(author['tasks'])}")
        return res

    def get_author_by_id(self, author_id: int) -> requests.Response:
        res = requests.get(f"{self.base_url}/authors/{author_id}")
        print_response(f"Get author id: {author_id}", res)
        return res

    def delete_author(self, author_id: int) -> requests.Response:
        res = requests.delete(f"{self.base_url}/authors/{author_id}")
        print_response(f"Delete author id: {author_id}", res)
        return res
