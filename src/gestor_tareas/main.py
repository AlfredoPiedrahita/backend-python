"""Primera entrega: crear y listar tareas
Escribe una aplicación de consola en Python que permita:
1. Mostrar un menú con estas opciones:
   - Agregar tarea
   - Listar tareas
   - Salir
2. Pedir una opción al usuario.
3. Si elige Agregar tarea, pedir un título y una descripción.
4. Si el título está vacío o contiene solo espacios, mostrar un mensaje de error y no agregar la tarea.
5. Si los datos son válidos, guardar la tarea en una lista mientras el programa esté abierto.
6. Si elige Listar tareas, mostrar todas las tareas agregadas con su número, título, descripción y estado. Las nuevas tareas empiezan como pendientes.
7. Si todavía no hay tareas, mostrar un mensaje que lo indique.
8. Si elige Salir, terminar el programa.
9. Si escribe una opción que no existe, mostrar un mensaje y volver al menú.
Por ahora, no agregues completar o eliminar tareas, archivos, clases, decoradores, async ni pruebas con pytest. Los iremos incorporando después, cuando esta versión esté clara.
Cómo organizar el código
Guarda la aplicación en un archivo llamado main.py dentro de src/gestor_tareas/. Usa funciones separadas para mostrar el menú, agregar una tarea, listar tareas y ejecutar el programa. El programa debe poder iniciarse desde main.py.
Tu trabajo con Git
1. Desde la carpeta del proyecto, crea una rama llamada feature/add-and-list-tasks.
2. Escribe el código y ejecútalo para comprobar los casos de la lista.
3. Revisa los cambios con git status y git diff.
4. Crea un commit descriptivo.
5. Cuando estés listo, comparte aquí el contenido de main.py y te ayudo a revisarlo antes de subirlo a GitHub y abrir el Pull Request."""




def mostrar_menu():
    # Punto 1: mostrar el menú
    print("\n=== GESTOR DE TAREAS ===")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Salir")

def agregar_tarea(tareas):
    # Punto 3: pedir título y descripción
    titulo = input("Título: ")
    descripcion = input("Descripción: ")

    # Punto 4: validar que el título no esté vacío ni solo espacios
    if titulo.strip() == "":
        print("Error: el título no puede estar vacío.")
        return

    # Punto 5: guardar la tarea en la lista (estado inicial: pendiente)
    tarea = {
        "titulo": titulo.strip(),
        "descripcion": descripcion.strip(),
        "estado": "Pendiente",
    }
    tareas.append(tarea)
    print("Tarea agregada correctamente.")


def listar_tareas(tareas):
    # Punto 7: mensaje si no hay tareas
    if not tareas:
        print("No hay tareas registradas todavía.")
        return

    # Punto 6: mostrar número, título, descripción y estado
    print("\n--- LISTA DE TAREAS ---")
    for numero, tarea in enumerate(tareas, start=1):
        print(f"{numero}. {tarea['titulo']}")
        print(f"   Descripción: {tarea['descripcion']}")
        print(f"   Estado: {tarea['estado']}")


def main():
    tareas = []  # Punto 5: la lista vive mientras el programa esté abierto

    while True:
        mostrar_menu()
        # Punto 2: pedir una opción
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            listar_tareas(tareas)
        elif opcion == "3":
            # Punto 8: salir
            print("¡Hasta luego!")
            break
        else:
            # Punto 9: opción inválida, vuelve al menú
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()

