from modules.cifrador import cifrar_contraseña, descifrar_contraseña

usuarios_db = {}

def login(nombre):
    print("Iniciando sesión...\n")
    password = input("Contraseña: ")
    usuario = usuarios_db.get(nombre)
    if usuario and descifrar_contraseña(usuario["contraseña"]) == password:
        print(f"Éxito. Bienvenido, {nombre}.")
        rol = recuperar_rol_usuario(nombre)
        return rol
    else:
        print("Usuario o contraseña incorrectos.\n")
        return False

def recuperar_rol_usuario(nombre):
    usuario = usuarios_db.get(nombre)
    if usuario:
        return usuario.get("rol")
    return None

def simular_usuario():
    usuarios_db["admin"] = {
        "contraseña": cifrar_contraseña("admin"),
        "rol": "ADMIN",
        "correo": "admin"
    }

def admin_check():
    return len(usuarios_db) > 0

def registrar_usuario_standar():
    print("Registro de usuario nuevo.")

    while True:
        nombre = input("Ingrese un nombre de usuario: ").strip()

        if nombre in usuarios_db:
            print("El nombre de usuario ya existe. Elija otro.\n")
            continue

        correo = input("Ingrese un correo electrónico: ").strip()

        correo_duplicado = any(
            usuario.get("correo", "").lower() == correo.lower()
            for usuario in usuarios_db.values()
        )

        if correo_duplicado:
            print("Ya hay un usuario registrado con ese correo.\n")
            continue

        password = input("Ingrese la contraseña: ")

        print(f"\nLos datos serán:\n"
              f"Usuario: {nombre}\n"
              f"Contraseña: {password}\n"
              f"Correo: {correo}\n")

        check = input("Confirme por favor: Si (Y) / No (X): ").strip().upper()

        if check == "Y":
            usuarios_db[nombre] = {
                "contraseña": cifrar_contraseña(password),
                "rol": "USUARIO",
                "correo": correo
            }
            print("Usuario registrado con éxito.\n")
            return nombre
        elif check == "X":
            print("Reintentando registrar usuario...\n")
        else:
            print("Opción inválida. Solo se aceptan los valores (X) e (Y)\n")

def registrar_administrador():
    print(
        "No se han detectado usuarios previos. Se registrarán sus siguientes datos como administrador de la aplicación.\n"
        "Si usted está viendo este mensaje por segunda vez, por favor comuníquese con el área de soporte."
    )

    while True:
        nombre = input("Ingrese el nombre de usuario para la cuenta de administrador: ")
        password = input("Ingrese la contraseña para la cuenta de administrador: ")
        correo = input("Ingrese un correo electrónico: ")

        print(f"Los datos serán:\n"
              f"Usuario: {nombre}\n"
              f"Contraseña: {password}\n"
              f"Correo: {correo}")

        check = input("Confirme por favor: Si (Y) / No (X): ")

        if check.upper() == "Y":
            usuarios_db[nombre] = {
                "contraseña": cifrar_contraseña(password),
                "rol": "ADMIN",
                "correo": correo
            }
            print("Administrador registrado con éxito.\n")
            return
        elif check.upper() == "X":
            print("Reintentando registrar administrador...\n")
        else:
            print("Opción inválida. Solo se aceptan los valores (X) e (Y)\n")

def mostrar_info_usuario(nombre_usuario):
    usuario = usuarios_db.get(nombre_usuario)
    if usuario:
        print(f"Nombre: {nombre_usuario}")
        print(f"Contraseña: {usuario['contraseña']}")
        print(f"Rol: {usuario['rol']}")
        print(f"Correo: {usuario['correo']}")
    else:
        print("Usuario no encontrado.")

def mostrar_usuarios():
    hay_usuarios = False
    for nombre, usuario in usuarios_db.items():
        if usuario.get("rol", "").upper() != "ADMIN":
            hay_usuarios = True
            print(f"Usuario: {nombre}")
            for clave, valor in usuario.items():
                print(f"  {clave}: {valor}")
            print()

    if not hay_usuarios:
        print("No se detectaron usuarios (más allá del administrador).")

def recuperar_usuario():
    mostrar_usuarios()
    nombre = input("Indique el nombre del usuario que desea modificar: ").strip()
    if nombre in usuarios_db:
        return nombre
    else:
        print("No se encontró el usuario.")
        return None

def eliminar_usuarios():
    print("Advertencia: esta es una acción destructiva irreversible.")
    nombre = recuperar_usuario()
    if nombre:
        usuarios_db.pop(nombre)
        print("Usuario eliminado.")

def otorgar_privilegios():
    print("Advertencia: se están modificando permisos de administrador.")
    nombre = recuperar_usuario()
    if nombre:
        if usuarios_db[nombre].get("rol") == "USUARIO":
            usuarios_db[nombre]["rol"] = "ADMIN_TEMP"
            print(f"Rol de {nombre} actualizado a ADMIN_TEMP.")
        else:
            print("El usuario ya es administrador o tiene otro rol.")

def quitar_privilegios():
    print("Advertencia: se están quitando permisos de administrador.")
    nombre = recuperar_usuario()
    if nombre:
        if usuarios_db[nombre].get("rol") == "ADMIN_TEMP":
            usuarios_db[nombre]["rol"] = "USUARIO"
            print(f"Rol de {nombre} cambiado a USUARIO.")
        else:
            print(f"El usuario {nombre} no tiene rol ADMIN_TEMP.")
