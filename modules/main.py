import gestor_dispositivos
import gestor_usuarios
import gestor_vivienda


def menu_general(rol):
    print("\n===== MENÚ DEL SISTEMA =====")
    print("1: Agregar dispositivo")
    print("2: Mostrar dispositivos")
    print("3: Buscar dispositivo por nombre")
    print("4: Automatizar dispositivo")
    print("5: Desactivar automatización")
    print("6: Eliminar dispositivo")
    print("7: Mostrar automatizaciones")
    print("8: Mostrar información de usuario")

    if rol == "ADMIN" or rol == "ADMIN_TEMP":
        print("9: Mostrar todos los usuarios")
        print("10: Eliminar usuario")
        print("11: Otorgar privilegios")
        print("12: Quitar privilegios")
        print("13: Registrar vivienda")
        print("14: Mostrar información de vivienda")
        print("15: Eliminar vivienda")
        print("16: Mostrar dispositivos de la vivienda")

    print("0: Cerrar sesión")


def iniciar_aplicacion(rol, nombre):
    while True:
        menu_general(rol)
        opcion = input("Seleccione una opción: ").strip()

        if not opcion.isdigit():
            print("Ingrese un número válido.")
            continue

        opcion = int(opcion)

        match opcion:
            case 1:
                gestor_dispositivos.agregar_dispositivo()
            case 2:
                gestor_dispositivos.mostrar_dispositivos()
            case 3:
                gestor_dispositivos.buscar_dispositivo_por_nombre()
            case 4:
                gestor_dispositivos.automatizar_dispositivo()
            case 5:
                gestor_dispositivos.eliminar_automatizacion()
            case 6:
                if rol == "ADMIN" or "ADMIN_TEMP":
                    gestor_dispositivos.eliminar_dispositivo()
                else:
                    print("Acceso denegado: solo administradores pueden eliminar dispositivos.")
            case 7:
                gestor_dispositivos.mostrar_automatizaciones()
            case 8:
                gestor_usuarios.mostrar_info_usuario(nombre)
            case 9 if rol == "ADMIN" or "ADMIN_TEMP":
                gestor_usuarios.mostrar_usuarios()
            case 10 if rol == "ADMIN" or "ADMIN_TEMP":
                gestor_usuarios.eliminar_usuarios()
            case 11 if rol == "ADMIN" or "ADMIN_TEMP":
                gestor_usuarios.otorgar_privilegios()
            case 12 if rol == "ADMIN" or "ADMIN_TEMP":
                gestor_usuarios.quitar_privilegios()
            case 13 if rol == "ADMIN" or "ADMIN_TEMP":
                gestor_vivienda.registrar_vivienda()
            case 14 if rol == "ADMIN" or "ADMIN_TEMP":
                gestor_vivienda.mostrar_vivienda()
            case 15 if rol == "ADMIN" or "ADMIN_TEMP":
                gestor_vivienda.eliminar_vivienda()
            case 16 if rol == "ADMIN" or "ADMIN_TEMP":
                gestor_vivienda.mostrar_dispositivo_vivienda()
            case 0:
                print(f"Cerrando sesión de {nombre}.")
                break
            case _:
                print("Opción inválida.")


if __name__ == "__main__":
    while True:
        if not gestor_usuarios.admin_check():
            # gestor_usuarios.simular_usuario()
            gestor_usuarios.registrar_administrador()

        print("\n===== BIENVENIDO =====")
        print("1: Registrar usuario")
        print("2: Acceder")
        print("0: Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            gestor_usuarios.registrar_usuario_standar()
        elif opcion == "2":
            nombre = input("Usuario: ").strip()
            rol = gestor_usuarios.login(nombre)
            if rol:
                iniciar_aplicacion(rol, nombre)
            else:
                print("Datos inválidos.")
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
