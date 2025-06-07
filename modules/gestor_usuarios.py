from modules.cifrador import cifrar_contraseña, descifrar_contraseña
import json

import os

usuarios_db = {}
def login():
    print("Iniciando sesion...\n")
    nombre = input("Usuario: ")
    password = input("Contraseña: ")

    usuario = usuarios_db.get(nombre)

    if usuario:
        password_guardada_cifrada = usuario["contraseña"]
        password_descifrada = descifrar_contraseña(password_guardada_cifrada)

        if password == password_descifrada:
            print(f"Éxito. Bienvenido, {nombre}.")
            return True
        else:
            print("Usuario o contraseña incorrectos.")
            return False
    else:
        print("Usuario o contraseña incorrectos.")
        return False

def registrar_administrador():
    print(
        "No se han detectado usuarios previos. Se registrarán sus siguientes datos como administrador de la aplicación.\n"
        "Si usted está viendo este mensaje por segunda vez, por favor comuníquese con el área de soporte. "
    )

    nombre = input("Ingrese el nombre de usuario para la cuenta de administrador: ")
    password = input("Ingrese la contraseña para la cuenta de administrador: ")
    correo = input("Ingrese un correo electronico: ")

    while True:
        print(f"Los datos serán:\n"
              f"Usuario: {nombre}\n"
              f"Contraseña: {password}\n"
              f"Correo: {correo}")
        check = input("Confirme por favor: Si (Y) / No (X): ")
        if check.upper() == "Y":
            password_cifrada = cifrar_contraseña(password)

            usuarios_db[nombre] = {
                "contraseña": password_cifrada,
                "Rol": "ADMIN",
                "Correo": correo
            }
            print("Administrador registrado con éxito.\n")
            return
        elif check.upper() == "X":
            print("Reintentando registrar administrador...\n")
        else:
            print("Opción inválida. Solo se aceptan los valores (X) e (Y)\n")

def guardar_usuarios():
    with open("usuarios.json", "w") as f:
        datos_serializables = {}
        for usuario, info in usuarios_db.items():
            datos_serializables[usuario] = {
                "contraseña": info["contraseña"].decode(),  # bytes a texto
                "Rol": info["Rol"],
                "Correo": info["Correo"]
            }
        json.dump(datos_serializables, f)

def cargar_usuarios():
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r") as f:
            datos = json.load(f)
            for usuario, info in datos.items():
                usuarios_db[usuario] = {
                    "contraseña": info["contraseña"].encode(),  # texto a bytes
                    "Rol": info["Rol"],
                    "Correo": info["Correo"]
                }