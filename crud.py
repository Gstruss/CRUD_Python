# Lista de ejemplo que simula una base de datos
db = []

# Crear
def crear(id, nombre, edad):
    persona = {
        'id': id,
        'nombre': nombre,
        'edad': edad
    }
    db.append(persona)
    print(f"Persona {nombre} agregada correctamente.")

# Leer
def leer():
    if not db:
        print("No hay registros.")
    else:
        print("Registros en la base de datos:")
        for persona in db:
            print(persona)

# Actualizar
def actualizar(id, nuevo_nombre, nueva_edad):
    for persona in db:
        if persona['id'] == id:
            persona['nombre'] = nuevo_nombre
            persona['edad'] = nueva_edad
            print(f"Persona con id {id} actualizada correctamente.")
            return
    print(f"No se encontró una persona con el id {id}.")

# Eliminar
def eliminar(id):
    global db
    db = [persona for persona in db if persona['id'] != id]
    print(f"Persona con id {id} eliminada correctamente.")

# Menú para interactuar con el CRUD
def menu():
    while True:
        print("\n--- CRUD en Python ---")
        print("1. Crear")
        print("2. Leer")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            id = int(input("Ingresa el ID: "))
            nombre = input("Ingresa el nombre: ")
            edad = int(input("Ingresa la edad: "))
            crear(id, nombre, edad)
        elif opcion == "2":
            leer()
        elif opcion == "3":
            id = int(input("Ingresa el ID de la persona a actualizar: "))
            nuevo_nombre = input("Ingresa el nuevo nombre: ")
            nueva_edad = int(input("Ingresa la nueva edad: "))
            actualizar(id, nuevo_nombre, nueva_edad)
        elif opcion == "4":
            id = int(input("Ingresa el ID de la persona a eliminar: "))
            eliminar(id)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

# Ejecutar el menú
menu()
