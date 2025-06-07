usuarios_db = {}


def login():
    print("Iniciando sesion...\n")
    nombre = input("Usuario: ")
    password = input("Contraseña: ")

    usuario = usuarios_db.get(nombre)

    if usuario and usuario["contraseña"] == password:
        print(f"Exito. Bienvenido, {nombre}.")
        return True
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
            usuarios_db[nombre] = {
                "contraseña": password,
                "Rol": "ADMIN",
                "Correo": correo
            }
            print("Administrador registrado con éxito.")
            return
        elif check.upper() == "X":
            print("Reintentando registrar administrador...\n")
        else:
            print("Opción inválida. Solo se aceptan los valores (X) e (Y)\n")


def mostrar_usuarios():
    for key, value in usuarios_db.items():
        print(f"Usuario:{key}")
        for clave, valor in value.items():
            print(f" {clave}:{valor}")
        print()


def recuperar_usuario():
    mostrar_usuarios()
    nombre = input("Indique el nombre del usuario que desea modificar: ").strip()
    if nombre in usuarios_db:
        return nombre
    else:
        print("No se encontró el usuario.")
        return None


def eliminar_usuarios():
    print("Advertencia: esta es una accion destructiva irreversible.")
    nombre = recuperar_usuario()
    usuarios_db.pop(nombre)
    print("Usuario eliminado.")


def otorgar_privilegios():
    print("Advertencia: se están modificando permisos de administrador.")
    nombre = recuperar_usuario()
    if nombre:
        if usuarios_db[nombre]["Rol"] == "USUARIO":
            usuarios_db[nombre]["Rol"] = "ADMIN_TEMP"
            print(f"Rol de {nombre} actualizado a ADMIN_TEMP.")
        else:
            print("El usuario ya es administrador")


def quitar_privilegios():
    print("Advertencia: se están quitando permisos de administrador.")
    nombre = recuperar_usuario()
    if nombre:
        if usuarios_db[nombre]["Rol"] == "ADMIN_TEMP":
            usuarios_db[nombre]["Rol"] = "USUARIO"
            print(f"Rol de {nombre} cambiado a USUARIO.")
        else:
            print(f"El usuario {nombre} no tiene rol ADMIN_TEMP.")