# ==============================
# SISTEMA DE BIBLIOTECA
# ==============================

# Lista donde se guardan los libros
biblioteca = []


# --------------------------------
# Registrar libro
# --------------------------------
def registrar_libro():

    titulo = input("Ingrese el título del libro: ")

    # Validar títulos duplicados
    for libro in biblioteca:
        if libro["titulo"].lower() == titulo.lower():
            print("Ese libro ya está registrado.")
            return
        
    autor = input("Ingrese el autor: ")

    año = input("Ingrese el año de publicación: ")

    while not año.isdigit():
        año = input("Ingrese un año válido: ")

    # Crear diccionario del libro
    libro = {
        "titulo": titulo,
        "autor": autor,
        "año": año
    }

    # Agregar libro a la lista
    biblioteca.append(libro)

    print("Libro registrado correctamente.")


# --------------------------------
# Mostrar libros
# --------------------------------
def mostrar_libros():

    if len(biblioteca) == 0:
        print("No hay libros registrados.")
        return

    print("\n===== LISTA DE LIBROS =====")

    for i, libro in enumerate(biblioteca, start=1):
        print(f"\nLibro #{i}")
        print(f"Título: {libro['titulo']}")
        print(f"Autor: {libro['autor']}")
        print(f"Año: {libro['año']}")

    print(f"\nTotal de libros: {len(biblioteca)}")


# --------------------------------
#  Buscar libro
# --------------------------------
def buscar_libro():

    titulo_buscar = input("Ingrese el título a buscar: ")

    encontrado = False

    for libro in biblioteca:

        if libro["titulo"].lower() == titulo_buscar.lower():

            print("\nLibro encontrado:")
            print(f"Título: {libro['titulo']}")
            print(f"Autor: {libro['autor']}")
            print(f"Año: {libro['año']}")

            encontrado = True
            break

    if not encontrado:
        print("Libro no encontrado.")

def buscar_por_autor():

    autor_buscar = input("Ingrese el autor a buscar: ")

    encontrado = False

    for libro in biblioteca:

        if autor_buscar.lower() in libro["autor"].lower():

            print("\nLibro encontrado:")
            print(f"Título: {libro['titulo']}")
            print(f"Autor: {libro['autor']}")
            print(f"Año: {libro['año']}")

            encontrado = True

    if not encontrado:
        print("No se encontraron libros de ese autor.")       


# --------------------------------
# Eliminar libro
# --------------------------------
def eliminar_libro():

    titulo_eliminar = input("Ingrese el título del libro a eliminar: ")

    for libro in biblioteca:

        if libro["titulo"].lower() == titulo_eliminar.lower():

            biblioteca.remove(libro)

            print("Libro eliminado correctamente.")
            return

    print("No se encontró el libro.")


# --------------------------------
# Mostrar libro más antiguo
# --------------------------------
def libro_mas_antiguo():

    if len(biblioteca) == 0:
        print("No hay libros registrados.")
        return

    # Buscar el libro con menor año
    antiguo = min(biblioteca, key=lambda x: int(x["año"]))

    print("\n===== LIBRO MÁS ANTIGUO =====")
    print(f"Título: {antiguo['titulo']}")
    print(f"Autor: {antiguo['autor']}")
    print(f"Año: {antiguo['año']}")
# --------------------------------
# ACTUALIZAR INFO_LIBRO
# --------------------------------
def actualizar_libro():
    titulo_buscar= input("Ingrese el titulo del libro a actualizar: ")
    for libro in biblioteca:
        if libro["titulo"].lower() == titulo_buscar.lower():
            print("\nLibro encontrado.")
            print("Ingrese los nuevos datos.")

            nuevo_titulo = input("Nuevo título: ")
            nuevo_autor = input("Nuevo autor: ")
            nuevo_año = input("Nuevo año: ")

    while not nuevo_año.isdigit():
            nuevo_año = input("Ingrese un año válido: ")

            # Actualizar datos
            libro["titulo"] = nuevo_titulo
            libro["autor"] = nuevo_autor
            libro["año"] = nuevo_año

            print("Libro actualizado correctamente.")
            return

    print("Libro no encontrado.")

# --------------------------------
# Contar libros registrados
# --------------------------------
def contar_libros():

    print(f"\nTotal de libros registrados: {len(biblioteca)}")

# --------------------------------
# MENU PRINCIPAL
# --------------------------------
while True:

    print("\n===== BIBLIOTECA =====")
    print("1. Registrar libro")
    print("2. Mostrar libros")
    print("3. Buscar libro")
    print("4. Buscar libros por autor")
    print("5. Eliminar libro")
    print("6. Actualizar informacion del libro")
    print("7. Mostrar libro más antiguo")
    print("8. Contar libros registrados")
    print("9. Salir")

    opcion = input("Seleccione una opción: ")

    # Validar opción
    if opcion == "1":
        registrar_libro()

    elif opcion == "2":
        mostrar_libros()

    elif opcion == "3":
        buscar_libro()

    elif opcion == "4":
        buscar_por_autor()

    elif opcion == "5":
        eliminar_libro()

    elif opcion == "6":
        actualizar_libro()

    elif opcion == "7":
        libro_mas_antiguo()

    elif opcion == "8":
        contar_libros()

    elif opcion == "9":
        print("Saliendo del programa...")
        break

    else:
         print("Opción inválida.")