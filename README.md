# Ejercicio Práctico Clase 2 - Entregrable 1

## Descripción

Este proyecto es una API RESTful desarrollada con FastAPI que permite gestionar autores y tareas pendientes (todos). La API implementa operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para ambos modelos, con relaciones definidas entre ellos.

## Estructura del Proyecto

```
app/
├── main.py             # Punto de entrada de la aplicación
├── database.py         # Configuración de la base de datos y modelos
├── models/             # Modelos de la base de datos
│   ├── author.py
│   └── task.py
├── schemas/            # Esquemas de Pydantic para validación y serialización
│   ├── author.py
│   └── task.py
└── routers/            # Controladores de las rutas
    ├── authors.py
    └── tasks.py
```

## Requisitos Previos

- Python 3.8+
- pip (gestor de paquetes de Python)

## Instalación

1. **Clonar el repositorio** (o descargar el código fuente)

2. **Crear un entorno virtual** (recomendado):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución

Para iniciar el servidor en modo desarrollo con recarga automática:

```bash
uvicorn app.main:app --reload
```

El servidor estará disponible en `http://localhost:8000`.

## Endpoints Disponibles

### Autores

- `POST /authors/`: Crear un nuevo autor
- `GET /authors/`: Obtener todos los autores
- `GET /authors/{author_id}/`: Obtener un autor por ID
- `PUT /authors/{author_id}/`: Actualizar un autor
- `DELETE /authors/{author_id}/`: Eliminar un autor

### Tareas (Tasks)

- `POST /tasks/`: Crear una nueva tarea
- `GET /tasks/`: Obtener todas las tareas
- `GET /tasks/{task_id}/`: Obtener una tarea por ID
- `PUT /tasks/{task_id}/`: Actualizar una tarea
- `DELETE /tasks/{task_id}/`: Eliminar una tarea

## Documentación de la API

La documentación interactiva (Swagger UI) está disponible en:

- **Swagger UI**: `http://localhost:8000/docs`

## Tests

Para ejecutar los tests automáticos:

### Primero hay que borrar la base de datos

```bash
rm app/task.db
```

### Luego ejecutar los tests

```bash
python tests/test_requests.py
```

## Tecnologías Utilizadas

- **FastAPI**: Framework web para construir APIs con Python
- **SQLAlchemy**: ORM para la interacción con la base de datos
- **Alembic**: Herramienta de migración de bases de datos
- **Pydantic**: Validación de datos y esquemas
- **SQLite**: Base de datos relacional (por defecto)
- **Uvicorn**: Servidor ASGI