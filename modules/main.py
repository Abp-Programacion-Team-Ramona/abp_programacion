from gestor_usuarios import registrar_administrador, guardar_usuarios, cargar_usuarios, usuarios_db
from gestor_dispositivos import agregar_dispositivo, mostrar_dispositivos, buscar_dispositivo_por_nombre, \
    automatizar_dispositivo, eliminar_automatizacion, eliminar_dispositivo, mostrar_automatizaciones

from gestor_usuarios import mostrar_usuarios, eliminar_usuarios, otorgar_privilegios, quitar_privilegios


def menu_general(rol):
    opciones = (
        "\n===== MENÚ DEL SISTEMA =====\n"
        "1: Agregar dispositivo\n"
        "2: Mostrar dispositivos\n"
        "3: Buscar dispositivo por nombre\n"
        "4: Automatizar dispositivo\n"
        "5: Desactivar automatización\n"
        "6: Eliminar dispositivo\n"
        "7: Mostrar automatizaciones\n"
    )
    if rol == "admin":
        opciones += (
            "8: Mostrar usuarios\n"
            "9: Eliminar usuario\n"
            "10: Otorgar privilegios\n"
            "11: Quitar privilegios\n"
            "12: Salir\n"
        )
    else:
        opciones += "8: Salir\n"

    print(opciones)


def iniciar_aplicacion(rol):
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
                eliminar_dispositivo()
            case 7:
                mostrar_automatizaciones()
            case 8 if rol == "admin":
                mostrar_usuarios()
            case 9 if rol == "admin":
                eliminar_usuarios()
            case 10 if rol == "admin":
                otorgar_privilegios()
            case 11 if rol == "admin":
                quitar_privilegios()
            case 12 if rol == "admin":
                print("Cerrando sesión de administrador.")
                break
            case 8 if rol == "usuario":
                print("Cerrando sesión de usuario estándar.")
                break
            case _:
                print("Opción inválida.")
