dispositivos = {}

automatizaciones = {}

TIPOS_VALIDOS = ("AIRE_ACONDICIONADO", "VENTILADOR",
                 "ENCENDIBLES")
MODOS_AC = ("VENTILADOR", "FRIO", "CALOR", "HUMEDAD")


def automatizar_dispositivo():
    tipo_input = input(
        "¿Qué tipo de dispositivo es?\n"
        "1) Aire acondicionado\n"
        "2) Ventilador (Pie, Techo)\n"
        "3) Encendible (Luces, Computadoras, Cafeteras)\n"
        "Seleccione una opción: "
    )

    nombre_rutina = input("Indique el identificador de la rutina:")

    if tipo_input.isdigit():
        tipo = int(tipo_input)
        match tipo:
            case 1:
                automatizar_aire_acondicionado(nombre_rutina)
            case 2:
                automatizar_ventilador(nombre_rutina)
            case 3:
                automatizar_encendido_apagado(nombre_rutina)
            case _:
                print("Opción invalida.")
    else:
        print("Solo se aceptan valores numericos.")


def automatizar_encendido_apagado(nombre_rutina):
    arranque = ""
    apagado = ""
    texto_estado = "ENCENDIDO"

    if check_dispositivos_por_tipo("ENCENDIBLES"):
        mostrar_dispositivos_por_tipo("ENCENDIBLES")
    else:
        print("No existen dispositivos del tipo.")
        return False

    nombre_dispositivo = buscar_dispositivo_por_identificador()

    print("Indique un horario de inicio de la rutina:")
    inicio = input()
    print("Indique el estado deseado del dispositivo ( ENCENDIDO (Y) / APAGADO (X) ):")
    estado = input()
    while str.upper(estado) not in ("X", "Y"):
        print("Indique el estado deseado del dispositivo ( ENCENDIDO (Y) / APAGADO (X) ):")
        estado = input()

    if str.upper(estado) == "X":
        texto_estado = "APAGADO"
        print(
            "Si desea agregar un horario de encendido indiquelo a continuacion. De lo contrario deje vacio el espacio.")
        arranque = input()
    else:
        print(
            "Si desea agregar un horario de apagado indiquelo a continuacion. De lo contrario deje vacio el espacio.")
        apagado = input()

    nivel_input = input(
        "Si el dispositivo tiene multiples niveles de intensidad indiquelo a continuacion, de lo contrario deje el espacio vacio: ")

    if len(nivel_input) <= 0:
        nivel_input = 1

    modo_fiesta_input = input(
        "Si el dispositivo tiene modo fiesta y desea activarlo al iniciar la rutina indiquelo: ( ENCENDIDO (Y) / APAGADO (X) ) ")
    modo_fiesta = str.upper(modo_fiesta_input) == "Y"

    modo_nocturno_input = input(
        "Si el dispositivo tiene modo nocturno y desea activarlo al iniciar la rutina indiquelo: ( ENCENDIDO (Y) / APAGADO (X) ) ")
    modo_nocturno = str.upper(modo_nocturno_input) == "Y"

    automatizaciones[nombre_rutina] = {
        "Dispositivo": nombre_dispositivo,
        "Horario de inicio de la rutina": inicio,
        "Estado del dispositivo": texto_estado,
        "Horario arranque de dispositivo": arranque,
        "Horario apagado de dispositivo": apagado,
        "Nivel de intensidad": nivel_input,
        "Modo fiesta": modo_fiesta,
        "Modo nocturno": modo_nocturno
    }

    return True


def automatizar_aire_acondicionado(nombre_rutina):
    arranque = ""
    apagado = ""
    velocidad = 0
    temperatura = 0
    modo = ""
    texto_estado = "ENCENDIDO"
    if check_dispositivos_por_tipo("AIRE_ACONDICIONADO"):
        mostrar_dispositivos_por_tipo("AIRE_ACONDICIONADO")
    else:
        print("No existen dispositivos del tipo.")
        return False

    nombre_dispositivo = buscar_dispositivo_por_identificador()

    print("Indique un horario de inicio de la rutina:")
    inicio = input()
    print("Indique el estado deseado del dispositivo ( ENCENDIDO (Y) / APAGADO (X) ):")
    estado = input()
    while str.upper(estado) not in ("X", "Y"):
        print("Indique el estado deseado del dispositivo ( ENCENDIDO (Y) / APAGADO (X) ):")
        estado = input()

    if str.upper(estado) == "X":
        texto_estado = "APAGADO"
        print(
            "Si desea agregar un horario de encendido indiquelo a continuacion. De lo contrario deje vacio el espacio.")
        arranque = input()
    else:
        print("Indique la velocidad del dispositivo con un valor entre 1 y 3 inclusive:")
        velocidad = int(input())
        if 0 < velocidad > 4:
            while 0 < velocidad > 4:
                print("Opcion invalida.")
                print("Indique la velocidad del dispositivo con un valor entre 1 y 3 inclusive:")
                velocidad = int(input())
        print(
            "Si desea agregar un horario de apagado indiquelo a continuacion. De lo contrario deje vacio el espacio.")
        apagado = input()
        print("Ingrese el modo de aire acondicionado: ( (1) VENTILADOR,(2) FRIO, (3) CALOR, (4) HUMEDAD ) ")
        modo_input = int(input())
        if modo_input < 0 or modo_input > 4:
            while modo_input < 0 or modo_input > 4:
                print("Opcion invalida")
                print("Ingrese el modo de aire acondicionado: ((1) VENTILADOR,(2) FRIO, (3) CALOR, (4) HUMEDAD ) ")
        if modo_input == 1:
            modo = "VENTILADOR"
        elif modo_input == 2:
            modo = "FRIO"
        elif modo_input == 3:
            modo = "CALOR"
        elif modo_input == 4:
            modo = "HUMEDAD"
        print("Ingrese una temperatura entre 15-38 (Celcius): ")
        temperatura = int(input())
        if temperatura < 15 or temperatura > 38:
            while temperatura < 15 or temperatura > 38:
                print("Opcion invalida")
                print("Ingrese una temperatura entre 15-38 (Celcius): ")
                temperatura = int(input())

    automatizaciones[nombre_rutina] = {
        "Dispositivo": nombre_dispositivo,
        "Horario de inicio de la rutina": inicio,
        "Estado del dispositivo": texto_estado,
        "Horario arranque de dispositivo": arranque,
        "Horario apagado de dispositivo": apagado,
        "Velocidad ventilador": velocidad,
        "Modo": modo,
        "Temperatura": temperatura
    }

    return True


def automatizar_ventilador(nombre_rutina):
    arranque = ""
    apagado = ""
    velocidad = 0
    giro = False
    texto_estado = "ENCENDIDO"
    if check_dispositivos_por_tipo("VENTILADOR"):
        mostrar_dispositivos_por_tipo("VENTILADOR")
    else:
        print("No existen dispositivos del tipo.")
        return False

    nombre_dispositivo = buscar_dispositivo_por_identificador()

    print("Indique un horario de inicio de la rutina:")
    inicio = input()

    print("Indique el estado deseado del dispositivo ( ENCENDIDO (Y) / APAGADO (X) ):")

    estado = input()

    while str.upper(estado) not in ("X", "Y"):
        print("Indique el estado deseado del dispositivo ( ENCENDIDO (Y) / APAGADO (X) ):")

        estado = input()

    if str.upper(estado) == "X":
        texto_estado = "APAGADO"
        print(
            "Si desea agregar un horario de encendido indiquelo a continuacion. De lo contrario deje vacio el espacio.")
        arranque = input()
    else:
        giro_input = input("Indique si desea habilitar el giro en el ventilador: ( SI (Y) / NO (X) )")
        giro = str.upper(giro_input) == "Y"
        print("Indique la velocidad del dispositivo con un valor entre 1 y 3 inclusive:")
        velocidad = int(input())
        if velocidad < 0 or velocidad > 4:
            while velocidad < 0 or velocidad > 4:
                print("Opcion invalida.")
                print("Indique la velocidad del dispositivo con un valor entre 1 y 3 inclusive:")
                velocidad = int(input())
        print(
            "Si desea agregar un horario de apagado indiquelo a continuacion. De lo contrario deje vacio el espacio.")
        apagado = input()

    automatizaciones[nombre_rutina] = {
        "Dispositivo": nombre_dispositivo,
        "Horario de inicio de la rutina": inicio,
        "Estado del dispositivo": texto_estado,
        "Horario arranque de dispositivo": arranque,
        "Horario apagado de dispositivo": apagado,
        "Velocidad ventilador": velocidad,
        "Giro": giro
    }

    return True


def agregar_dispositivo():
    while True:
        opcion = input(
            "¿Que tipo de dispositivo es?: "
            "1) Aire acondicionado. "
            "2) Ventilador (Pie, Techo). "
            "3) Encendible (Luces, Computadores personales, cafeteras): ")
        if opcion.isdigit():
            tipo = int(opcion)
            if 0 < tipo <= 3:
                match tipo:
                    case 1:
                        tipo_dispositivo = "AIRE_ACONDICIONADO"
                        break
                    case 2:
                        tipo_dispositivo = "VENTILADOR"
                        break
                    case 3:
                        tipo_dispositivo = "ENCENDIBLES"
                        break
            else:
                print("Opcion invalida")

    while True:
        nombre = input("Indique el nombre del dispositivo: ")
        if check_dispositivo_existe_por_nombre(str.upper(nombre)) or len(nombre) < 1:
            print("El dispositivo ya existe o el valor ingresado como nombre es invalido. Intente nuevamente")
        else:
            dispositivo = {
                "Nombre": str.upper(nombre),
                "Estado": "Encendido",
                "Tipo": tipo_dispositivo
            }
            dispositivos[len(dispositivos) + 1] = dispositivo
            break
    print(f"El dispositivo {nombre} fue registrado correctamente.")


def check_dispositivo_existe_por_nombre(nombre):
    for disp in dispositivos.values():
        for valor in disp.values():
            if str.upper(nombre) == valor:
                return True


def mostrar_dispositivos():
    if len(dispositivos) == 0:
        print("No hay dispositivos")
    for id_disp, disp in dispositivos.items():
        print(f"Identificador del dispositivo: {id_disp}.")
        for clave, valor in disp.items():
            print(f"  {clave}: {valor}")
        print()


def buscar_dispositivo_por_nombre():
    nombre = input("Indique el nombre del dispositivo: ").strip().upper()

    for id_disp, disp in dispositivos.items():
        if disp['Nombre'] == nombre:
            print(f"Identificador del dispositivo: {id_disp}. "
                  f"Nombre:{disp['Nombre']}. "
                  f"Estado:{disp['Estado']}. "
                  f"Tipo:{disp['Tipo']}.")
            return
    print("No se encontro el dispositivo.")


def buscar_dispositivo_por_identificador():
    numero = int(input("Indique el numero de identificacion de dispositivo que quiere automatizar: "))

    dispositivo = dispositivos.get(numero)

    if dispositivo:
        nombre_dispositivo = dispositivo["Nombre"]
        print(f"Dispositivo seleccionado: {nombre_dispositivo}")
        return nombre_dispositivo
    else:
        print("No existe un dispositivo con ese número.")
        return False


def mostrar_dispositivos_por_tipo(tipo):
    for id_disp, disp in dispositivos.items():
        if disp['Tipo'] == str.upper(tipo):
            print(f"Identificador del dispositivo: {id_disp}. Nombre:{disp['Nombre']}.")


def check_dispositivos_por_tipo(tipo):
    for id_disp, disp in dispositivos.items():
        if disp['Tipo'] == str.upper(tipo):
            return True
    return False


def eliminar_dispositivo():
    mostrar_dispositivos()
    identificador = int(input("Ingrese el Identificador del dispositivo: "))
    if not identificador > len(dispositivos) or identificador <= 0:
        dispositivo = dispositivos.pop(identificador)
        print(f"El dispositivo '{dispositivo['Nombre']}' y su rutina fueron eliminados correctamente.")
        automatizaciones.pop(identificador)
    else:
        print("Valor invalido.")


def mostrar_automatizaciones():
    if not automatizaciones:
        print("No hay automatizaciones creadas.")
        return

    for nombre_rutina, datos in automatizaciones.items():
        print(f"Nombre de la rutina: {nombre_rutina}")
        for clave, valor in datos.items():
            print(f"  {clave}: {valor}")


def eliminar_automatizacion():
    mostrar_automatizaciones()
    nombre = input("Indique el nombre de la automatizacion que desea eliminar")
    if nombre in automatizaciones:
        automatizaciones.pop(nombre)
        print(f"Automatización '{nombre}' eliminada.")
    else:
        print(f"No se encontro una automatización con el nombre '{nombre}'.")


if __name__ == "__main__":
    print("La aplicacion debe ejecutarse desde el modulo main.")
