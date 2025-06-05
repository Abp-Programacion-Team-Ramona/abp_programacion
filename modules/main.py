from gestor_dispositivos import agregar_dispositivo, mostrar_dispositivos, buscar_dispositivo_por_nombre, \
    automatizar_dispositivo, eliminar_automatizacion, eliminar_dispositivo, mostrar_automatizaciones


def menu_usuario_estandar():
    print("Opciones:\n"
          "1: Ver informacion de usuario\n"
          "2: Mostrar dispositivos\n"
          "3: Buscar dispositivo por nombre\n"
          "4: Automatizar dispositivo\n"
          "5: Desactivar automatizacion\n"
          "7: Salir")


aplicacion_ejecutando = True

while aplicacion_ejecutando:

    print("\n")
    menu_usuario_estandar()
    print("\n")

    opcion = input("Elija una opcion:")

    if opcion.isdigit():
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
            case 8:
                print("Cerrando aplicacion.")
                aplicacion_ejecutando = False
            case _:
                print("Opcion invalida.")
    else:
        print("Solo se admiten valores numericos")
