from funciones import *



while True:
    print("\n" + "=" * 40)
    print("""    MENÚ GESTIÓN DE USUARIOS
    [1] Mostrar todos los usuarios
    [2] Insertar usuario
    [3] Insertar múltiples usuarios
    [4] Filtrar usuarios por edad
    [5] Modificar nombre de usuario
    [6] Modificar edad de usuario
    [7] Modificar ciudad de usuario
    [8] Eliminar usuario
    [9] Buscar usuario
    [0] Salir""")
    print("=" * 40 + "\n")
    opcion = input("Seleccione acción a realizar: ")

    match opcion:
        case "1":
            mostrar_todos()
        case "2":
            while True:
                nombre = input("Nombre: ").strip()
                if not nombre:
                    print("El nombre no puede estar vacío.")
                    continue

                ciudad = input("Ciudad: ").strip()

                while True:
                    try:
                        edad = int(input("Edad: "))
                        if edad <= 0:
                            print("La edad no puede ser negativa ni cero.")
                        else:
                            break
                    except ValueError:
                        print("Debes ingresar un número válido para la edad.")

                id_insertado = insertar_usuario(nombre, edad, ciudad)
                print(f"Usuario insertado con ID: {id_insertado}")
                break

        case "3":
            lista_usuarios = []

            while True:
                nombre = input("Nombre: ").strip()
                if not nombre:
                    print("El nombre no puede estar vacío.")
                    continue

                while True:
                    try:
                        edad = int(input("Edad: "))
                        if edad <= 0:
                            print("La edad no puede ser negativa ni cero.")
                        else:
                            break  # edad válida
                    except ValueError:
                        print("Debes ingresar un número válido para la edad.")

                ciudad = input("Ciudad: ")

                usuario = {
                    "nombre": nombre,
                    "edad": edad,
                    "ciudad": ciudad
                }
                lista_usuarios.append(usuario)
                print(f"Usuario '{nombre}' agregado a la lista.")

                while True:
                    respuesta = input("¿Deseas ingresar otro usuario? [s|n]?: ").lower()
                    if respuesta not in ("s", "n"):
                        print("Respuesta incorrecta. Debes ingresar Sí [s] o No [n].")
                    else:
                        break

                if respuesta == "n":
                    break

            print("Lista de usuarios ingresados:")
            for u in lista_usuarios:
                print(u)

        case "4":
            while True:
                try:
                    edad_minima = int(input("Ingrese edad mínima para el filtro: "))
                    if edad_minima <= 0:
                        print("La edad no puede ser negativa ni cero.")
                    else:
                        break
                except ValueError:
                    print("Debes ingresar un número válido para la edad.")

            filtrar_por_edad(edad_minima)
        case "5":
            while True:
                nombre = input("Ingrese el nombre del usuario a modificar: ").strip()
                if nombre:
                    break
                print("El nombre no puede estar vacío.")

            while True:
                nuevo_nombre = input(f"Ingrese el nuevo nombre para '{nombre}': ").strip()
                if nuevo_nombre:
                    break
                print("El nuevo nombre no puede estar vacío.")

            resultado = modificar_nombre_usuario(nombre, nuevo_nombre)
            if resultado > 0:
                print(f"Nombre de '{nombre}' modificado a '{nuevo_nombre}'.")
            else:
                print(f"No se encontró un usuario con el nombre '{nombre}'.")
        case "6":
            while True:
                nombre = input("Ingrese el nombre del usuario a modificar: ").strip()
                if nombre:
                    break
                print("El nombre no puede estar vacío. Inténtelo nuevamente.")

            while True:
                try:
                    nueva_edad = int(input(f"Ingrese nueva edad para el usuario '{nombre}': "))
                    if nueva_edad <= 0:
                        print("La edad no puede ser negativa ni cero.")
                    else:
                        break
                except ValueError:
                    print("Debes ingresar un número válido para la edad.")

            resultado = modificar_edad_usuario(nombre, nueva_edad)
            if resultado > 0:
                print(f"Edad de '{nombre}' modificada a {nueva_edad}.")
            else:
                print(f"No se encontró un usuario con el nombre '{nombre}'.")
        case "7":
            while True:
                nombre = input("Ingrese el nombre del usuario a modificar: ").strip()
                if nombre:
                    break
                print("El nombre no puede estar vacío.")

            while True:
                nueva_ciudad = input(f"Ingrese nueva ciudad para '{nombre}': ").strip()
                if nueva_ciudad:
                    break
                print("La ciudad no puede estar vacía.")

            resultado = modificar_ciudad_usuario(nombre, nueva_ciudad)
            if resultado > 0:
                print(f"Ciudad de '{nombre}' modificada a '{nueva_ciudad}'.")
            else:
                print(f"No se encontró un usuario con el nombre '{nombre}'.")
        case "8":
            while True:
                nombre = input("Ingrese el nombre del usuario a eliminar: ").strip()
                if nombre:
                    break
                print("El nombre no puede estar vacío. Inténtelo nuevamente.")

            resultado = eliminar_usuario(nombre)
            if resultado > 0:
                print(f"Usuario '{nombre}' eliminado correctamente.")
            else:
                print(f"No se encontró un usuario con el nombre '{nombre}'.")

        case "9":
            while True:
                nombre = input("Ingrese el nombre del usuario a buscar: ").strip()
                if nombre:
                    break
                print("El nombre no puede estar vacío. Inténtelo nuevamente.")

            usuario = buscar_usuario(nombre)
            if usuario:
                print("Usuario encontrado:")
                pprint.pprint(usuario)
            else:
                print(f"No se encontró un usuario con el nombre '{nombre}'.")

        case "0":
            print("Salir")
            break
        case _:
            print("Opción no válida. Intente nuevamente.")