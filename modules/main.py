from gestor_dispositivos import agregar_dispositivo, mostrar_dispositivos, buscar_dispositivo_por_nombre, \
    automatizar_dispositivo, eliminar_automatizacion, modificar_automatizacion, eliminar_dispositivo, mostrar_automatizaciones

from gestor_usuarios import mostrar_usuarios, eliminar_usuarios, otorgar_privilegios, quitar_privilegios

def login():
    print(" Inicio de sesión")
    usuario = input("Usuario: ").strip()
    contraseña = input("Contraseña: ").strip()

    if usuario == "admin" and contraseña == "admin123":
        return {"nombre": "admin", "rol": "admin"}
    elif usuario == "usuario" and contraseña == "user123":
        return {"nombre": "usuario", "rol": "usuario"}
    else:
        print("Credenciales incorrectas.")
        return None

def menu_general(rol):
    print("\n===== MENÚ DEL SISTEMA =====")
    print("1: Agregar dispositivo")
    print("2: Mostrar dispositivos")
    print("3: Buscar dispositivo por nombre")
    print("4: Automatizar dispositivo")
    print("5: Desactivar automatización")
    print("6: Modificar automatización")   # NUEVO
    print("7: Eliminar dispositivo")
    print("8: Mostrar automatizaciones")
    if rol == "admin":
        print("9: Mostrar usuarios")
        print("10: Eliminar usuario")
        print("11: Otorgar privilegios")
        print("12: Quitar privilegios")
        print("13: Salir")
    else:
        print("9: Salir")

def ejecutar_menu_general(rol):
    while True:
        menu_general(rol)
        opcion = input("Seleccione una opción: ").strip()

        if opcion.isdigit():
            opcion = int(opcion)

            try:
                match opcion:
                    case 1:
                        agregar_dispositivo()
                    case 2:
                        mostrar_dispositivos()
                    case 3:
                        buscar_dispositivo_por_nombre()
                    case 4:
                        automatizar_dispositivo()
                    case 5:
                        eliminar_automatizacion()
                    case 6:
                        modificar_automatizacion()  # NUEVO
                    case 7:
                        eliminar_dispositivo()
                    case 8:
                        mostrar_automatizaciones()
                    case 9 if rol == "admin":
                        mostrar_usuarios()
                    case 10 if rol == "admin":
                        eliminar_usuarios()
                    case 11 if rol == "admin":
                        otorgar_privilegios()
                    case 12 if rol == "admin":
                        quitar_privilegios()
                    case 13 if rol == "admin":
                        print("Cerrando sesión de administrador.")
                        break
                    case 9 if rol == "usuario":
                        print("Cerrando sesión de usuario estándar.")
                        break
                    case _:
                        print("Opción inválida.")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Ingrese un número válido.")

print("Bienvenido al sistema de gestión de dispositivos.")
usuario_logueado = login()

if usuario_logueado:
    ejecutar_menu_general(usuario_logueado["rol"])
else:
    print("No se pudo iniciar sesión.")
