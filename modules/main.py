from gestor_dispositivos import agregar_dispositivo, mostrar_dispositivos, buscar_dispositivo_por_nombre, \
    automatizar_dispositivo, eliminar_automatizacion, eliminar_dispositivo, mostrar_automatizaciones




def menu_general(rol):
    opciones = (
        "\n===== MENÚ DEL SISTEMA =====\n"
        "1: Agregar dispositivo\n"
        "2: Mostrar dispositivos\n"
        "3: Buscar dispositivo por nombre\n"
        "4: Automatizar dispositivo\n"
        "5: Desactivar automatización\n"
        "6: Modificar automatización\n"
        "7: Eliminar dispositivo\n"
        "8: Mostrar automatizaciones\n"
    )
    if rol == "admin":
        opciones += (
            "9: Mostrar usuarios\n"
            "10: Eliminar usuario\n"
            "11: Otorgar privilegios\n"
            "12: Quitar privilegios\n"
            "13: Salir\n"
        )
    else:
        opciones += "9: Salir\n"

    print(opciones)

def ejecutar_menu_general(rol):
    while True:
        menu_general(rol)
        opcion = input("Seleccione una opción: ").strip()

        if not opcion.isdigit():
            print("Ingrese un número válido.")
            continue

        opcion = int(opcion)

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
                modificar_automatizacion()
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

print("Bienvenido al sistema de gestión de dispositivos.")
usuario_logueado = login()

if usuario_logueado:
    ejecutar_menu_general(usuario_logueado["rol"])
else:
    print("No se pudo iniciar sesión.")