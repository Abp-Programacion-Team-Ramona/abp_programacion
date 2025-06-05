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
