from gestor_dispositivos import (agregar_dispositivo, mostrar_dispositivos, buscar_dispositivo_por_nombre, \
    automatizar_dispositivo, eliminar_automatizacion, eliminar_dispositivo, mostrar_automatizaciones)

from gestor_usuarios import (login, registrar_administrador, registrar_usuario_standar,mostrar_info_usuario, usuarios_db)

def menu_principal():
    while True:
        print("--- Menú Principal ---\n")
        print("Opciones:\n" 
              "1: Iniciar sesión\n"
              "2: Registrar usuario\n"
              "3: Salir\n")
        opciones = input("Elija una opción: ")

        if opciones.isdigit():
            opciones = int(opciones)

            match opciones:
                case 1:
                    usuario = login()
                    if usuario:
                        rol = usuarios_db[usuario]["rol"]
                        if rol == "ADMIN":
                           # menu_administrador(usuario)
                            print("Implementando")
                        else:
                            menu_usuario_estandar(usuario)
                case 2:
                    registrar_usuario_standar()
                case 3:
                    print("Saliendo...")
                    break
                case _:
                    print("Opción inválida")
        else:
            print("Solo se admiten números.")



def menu_usuario_estandar(usuario):

    aplicacion_ejecutando = True

    while aplicacion_ejecutando:

        print("--- Menú de Usuario ---")
        print("Opciones:\n"
          "1: Ver informacion de usuario\n"
          "2: Mostrar dispositivos\n"
          "3: Buscar dispositivo por nombre\n"
          "4: Automatizar dispositivo\n"
          "5: Modificar automatizacion"
          "6: Eliminar automatizacion\n"
          "7: Salir\n")

        opcion = input("Elija una opcion:")

        if opcion.isdigit():
            opcion = int(opcion)
            match opcion:
                case 1:
                    mostrar_info_usuario(usuario)
                case 2:
                    mostrar_dispositivos()
                case 3:
                    buscar_dispositivo_por_nombre()
                case 4:
                    automatizar_dispositivo()
                case 5:
                    #modificar_automatizacion()
                    print("implementar")
                case 6:
                    eliminar_automatizacion()
                case 7:
                    print("Cerrando aplicacion.")
                    aplicacion_ejecutando = False
                case _:
                    print("Opcion invalida.")
        else:
            print("Solo se admiten valores numericos")



print("\n")
menu_principal()
print("\n")
