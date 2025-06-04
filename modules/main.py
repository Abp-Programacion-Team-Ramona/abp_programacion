from gestor_dispositivos import agregar_dispositivo, mostrar_dispositivos, buscar_dispositivo_por_nombre, \
    automatizar_dispositivo, eliminar_automatizacion, eliminar_dispositivo,mostrar_automatizaciones


def menu():
    print("Menu:")
    print("1:Registrar dispositivo:")
    print("2:Mostrar dispositivos:")
    print("3:Buscar dispositivo:")
    print("4:Automatizar dispositivo:")
    print("5:Eliminar automatizacion")
    print("6:Desconectar dispositivo:")
    print("7:Mostrar Automatizacion:")
    print("8:Salir:")


aplicacion_ejecutando = True

while aplicacion_ejecutando:

    print()
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
