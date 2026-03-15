from task_manager import TaskManager

if __name__ == "__main__":

    manager = TaskManager()

    enmanuel = manager.registrar_autor("Enmanuel Alejandro De Oleo", "guest@pontia.com")
    john     = manager.registrar_autor("Juan Ortiz", "guest22@pontia.com")
    manager.verificar_total_autores(2)

    task1 = manager.crear_tarea_expirada("Ir al gym",          enmanuel["id"], "Trabajar extremidades bajas")
    task2 = manager.crear_tarea_futura("Escribir tests",       enmanuel["id"], "Escribir test para la tarea de pontia")
    task3 = manager.crear_tarea_futura("Revisar pull request", john["id"],     "Revisar el pull request de la rama")
    
    manager.verificar_total_tareas(3)

    short_task_res = manager.crear_tarea("", john["id"], "", "")
    assert short_task_res.status_code == 422

    manager.completar_tarea(task1["id"])
    manager.eliminar_tarea(task3["id"])
    manager.verificar_total_tareas(2)

    expiradas = manager.obtener_tareas_expiradas()
    assert len(expiradas) == 1
    assert expiradas[0]["titulo"] == "Ir al gym"

    manager.eliminar_autor(john["id"])
    manager.verificar_total_autores(1)

    print("\n✅ Todas las verificaciones pasaron correctamente!")