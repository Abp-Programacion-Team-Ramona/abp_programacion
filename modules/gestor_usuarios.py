usuarios_db = {}


def registrar_administrador():
    print(
        "No se han detectado usuarios previos. Se registraran sus siguientes datos como administrador de la aplicacion.\n"
        "Si usted esta viendo este mensaje por segunda vez porfavor comuniquese con el area de soporte. ")

    nombre = input("Ingrese el nombre de usuario para la cuenta de administrador. ")
    password = input("Ingrese la contraseña la cuenta de administrador. ")

    confirmacion = False

    while not confirmacion:
        print(f"Los datos seran:\n"
              f"Usuario: {nombre} \n"
              f"Contraseña: {password}")
    check = input("Si (Y) / No (X) ")
    if check.upper() == "Y":
        print("Administrador registrado con exito.")
        confirmacion = True
    elif check.upper() == "X":
        nombre = input("Ingrese el nombre de usuario para la cuenta de administrador. ")
        password = input("Ingrese la contraseña la cuenta de administrador. ")
    else:
        print("Solo se aceptan los valores (X) e (Y) ")

    usuarios = {
        "nombre_usuario": nombre,
        "contraseña": password,
        "Rol": "ADMIN"
    }
