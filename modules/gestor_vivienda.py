from gestor_dispositivos import mostrar_dispositivos

vivienda = {}

def registrar_vivienda():
    while True:
        opcion = input(
            "¿Que tipo de vivienda es?: "
            "1) Casa. "
            "2) Departamento. "
            "3) Trabajo. ")
        if opcion.isdigit():
            tipo = int(opcion)
            if 0 < tipo <= 3:
                match tipo:
                    case 1:
                        tipo_vivienda = "CASA"
                        break
                    case 2:
                        tipo_vivienda = "DEPARTAMENTO"
                        break
                    case 3:
                        tipo_vivienda = "TRABAJO"
                        break
            else:
                print("Opcion invalida")
        else:
            print("Ingrese un numero valido")
    while True:
        nombre = input("Indique el nombre de la vivienda: ")
        if check_vivienda_existe_por_nombre(str.upper(nombre)) or len(nombre) < 1:
            print("La vivienda ya existe o el valor ingresado como nombre es invalido. Intente nuevamente")
        else:
            vivienda_data = {
                "Nombre": str.upper(nombre),
                "Tipo": tipo_vivienda
            }
            vivienda[len(vivienda) + 1] = vivienda_data
            break
    print(f"La vivienda {nombre} fue registrada correctamente.")


def check_vivienda_existe_por_nombre(nombre):
    for disp in vivienda.values():
        if disp["Nombre"] == str.upper(nombre):
            return True
    return False


def mostrar_vivienda():
    if len(vivienda) == 0:
        print("No hay vivienda registradas")
        return
    for id_disp, disp in vivienda.items():
        print(f"Identificador de la vivienda: {id_disp}.")
        for clave, valor in disp.items():
            print(f"  {clave}: {valor}")
        print()


def eliminar_vivienda():
    if len(vivienda) == 0:
        print("No hay viviendas registradas")
        return
    mostrar_vivienda()
    while True:
        identificador_input = input("Ingrese el Identificador de vivienda: ")
        if identificador_input.isdigit():
            identificador = int(identificador_input)
            if identificador in vivienda:
                vivienda_eliminada = vivienda.pop(identificador)
                print(f"La vivienda '{vivienda_eliminada['Nombre']}' fue eliminada correctamente.")
                break
            else:
                print("Identificador invalido. Intente nuevamente.")
        else:
            print("Ingrese un numero valido.")


def mostrar_dispositivo_vivienda():
    if len(vivienda) == 0:
        print("No hay viviendas registradas")
        return
    print("Viviendas disponibles:")
    mostrar_vivienda()
    while True:
        identificador_input = input("Ingrese el Identificador de la vivienda para ver sus dispositivos: ")
        if identificador_input.isdigit():
            identificador = int(identificador_input)
            if identificador in vivienda:
                vivienda_seleccionada = vivienda[identificador]
                print(f"\n Dispositivos de {vivienda_seleccionada['Nombre']} ")
                mostrar_dispositivos()
                break
            else:
                print("Identificador de vivienda inválido. Intente nuevamente.")
        else:
            print("Ingrese un número válido.")