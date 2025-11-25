import re
import pprint
from conexion import get_collection

def insertar_usuario(nombre, edad, ciudad):
    coleccion = get_collection()
    usuario = {"nombre": nombre, "edad": edad, "ciudad": ciudad}
    resultado = coleccion.insert_one(usuario)
    return resultado.inserted_id

def insertar_varios_usuarios(usuarios):
    coleccion = get_collection()
    resultado = coleccion.insert_many(usuarios)
    return resultado.inserted_ids

def mostrar_todos():
    coleccion = get_collection()
    print("\n--- TODOS LOS USUARIOS ---")
    for doc in coleccion.find():
        pprint.pprint(doc)

def filtrar_por_edad(edad_minima):
    coleccion = get_collection()
    print(f"\n--- USUARIOS MAYORES DE {edad_minima} ---")
    for doc in coleccion.find({"edad": {"$gt": edad_minima}}):
        pprint.pprint(doc)

def modificar_edad_usuario(nombre, nueva_edad):
    coleccion = get_collection()
    resultado = coleccion.update_one(
        {"nombre": re.compile(f"^{re.escape(nombre)}$", re.IGNORECASE)},
        {"$set": {"edad": nueva_edad}}
    )
    return resultado.modified_count

def modificar_nombre_usuario(nombre, nuevo_nombre):
    coleccion = get_collection()
    resultado = coleccion.update_one(
        {"nombre": re.compile(f"^{re.escape(nombre)}$", re.IGNORECASE)},
        {"$set": {"nombre": nuevo_nombre}}
    )
    return resultado.modified_count

def modificar_ciudad_usuario(nombre, nueva_ciudad):
    coleccion = get_collection()
    resultado = coleccion.update_one(
        {"nombre": re.compile(f"^{re.escape(nombre)}$", re.IGNORECASE)},
        {"$set": {"ciudad": nueva_ciudad}}
    )
    return resultado.modified_count

def eliminar_usuario(nombre):
    coleccion = get_collection()
    resultado = coleccion.delete_one(
        {"nombre": re.compile(f"^{re.escape(nombre)}$", re.IGNORECASE)}
    )
    return resultado.deleted_count


def buscar_usuario(nombre):
    coleccion = get_collection()
    return coleccion.find_one(
        {"nombre": re.compile(f"^{re.escape(nombre)}$", re.IGNORECASE)}
    )
