from gestor_dispositivos import agregar_dispositivo, mostrar_dispositivos, buscar_dispositivo_por_nombre, \
    automatizar_dispositivo, eliminar_automatizacion, eliminar_dispositivo,mostrar_automatizaciones


def menu():
    print("Menu:\n"
          "1: Registrar dispositivo\n"
          "2: Mostrar dispositivos\n"
          "3: Buscar dispositivo\n"
          "4: Automatizar dispositivo\n"
          "5: Eliminar automatizacion\n"
          "6: Desconectar dispositivo\n"
          "7: Mostrar Automatizacion\n"
          "8: Salir")


aplicacion_ejecutando = True

while aplicacion_ejecutando:

    print("\n")
    menu()
    print()

    try:
        opcion = int(input("Elija una opcion:"))

        if opcion < 1 or opcion > 8:
            print("Opcion invalida.")
        else:
            if opcion == 1:
                agregar_dispositivo()
            if opcion == 2:
                mostrar_dispositivos()
            if opcion == 3:
                buscar_dispositivo_por_nombre()
            if opcion == 4:
                automatizar_dispositivo()
            if opcion == 5:
                eliminar_automatizacion()
            if opcion == 6:
                eliminar_dispositivo()
            if opcion == 7:
                mostrar_automatizaciones()
            if opcion == 8:
                print("Cerrando aplicacion.")
                aplicacion_ejecutando = False

    except ValueError:
        print("El valor debe ser numerico")
