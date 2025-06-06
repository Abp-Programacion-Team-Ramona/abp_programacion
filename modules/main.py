from gestor_dispositivos import agregar_dispositivo, mostrar_dispositivos, buscar_dispositivo_por_nombre, \
    automatizar_dispositivo, eliminar_automatizacion, eliminar_dispositivo, mostrar_automatizaciones

from gestor_usuarios import mostrar_usuarios, eliminar_usuarios, otorgar_privilegios, quitar_privilegios

def menu_admin():
    print("Opciones Administrador:\n"
          "1: Mostrar todos los dispositivos\n"
          "2: Mostrar automatizaciones\n"
          "3: Eliminar dispositivo\n"
          "4: Mostrar usuarios\n"
          "5: Eliminar usuario\n"
          "6: Otorgar privilegios\n"
          "7: Quitar privilegios\n"
          "8: Salir")

def ejecutar_menu_admin():
    while True:
        print("\n")
        menu_admin()
        print("\n")
        opcion = input("Elija una opción (admin): ")

        if opcion.isdigit():
            opcion = int(opcion)
            match opcion:
                case 1:
                    mostrar_dispositivos()
                case 2:
                    mostrar_automatizaciones()
                case 3:
                    eliminar_dispositivo()
                case 4:
                    mostrar_usuarios()
                case 5:
                    eliminar_usuarios()
                case 6:
                    otorgar_privilegios()
                case 7:
                    quitar_privilegios()
                case 8:
                    print("Cerrando sesión de administrador.")
                    break
                case _:
                    print("Opción inválida.")
        else:
            print("Solo se admiten valores numéricos.")
            