dispositivos = {}

automatizaciones = {}

TIPOS_VALIDOS = ("AIRE_ACONDICIONADO", "VENTILADOR",
                 "ENCENDIBLES")
MODOS_AC = ("VENTILADOR", "FRIO", "CALOR", "HUMEDAD")


def automatizar_dispositivo():
    tipo = int(input(
        "¿Que tipo de dispositivo es?: "
        "1) Aire acondicionado. "
        "2) Ventilador (Pie, Techo). "
        "3) Encendible (Luces, Computadores personales, cafeteras): "))
    if 0 < tipo <= 3:
        if tipo == 1:
            automatizar_aire_acondicionado()
        if tipo == 2:
            automatizar_ventilador()
        if tipo == 3:
            automatizar_encendido_apagado()
    else:
        print("Opcion invalida")


def automatizar_encendido_apagado():
    arranque = ""
    apagado = ""
    texto_estado = "ENCENDIDO"

    if check_dispositivos_por_tipo("ENCENDIBLES"):
        mostrar_dispositivos_por_tipo("ENCENDIBLES")
    else:
        print("No existen dispositivos del tipo.")
        return False

    identificador = int(input("Indique que dispositivo quiere automatizar: "))

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

    automatizaciones[identificador] = {
        "Horario de inicio de la rutina": inicio,
        "Estado del dispositivo": texto_estado,
        "Horario arranque de dispositivo": arranque,
        "Horario apagado de dispositivo": apagado,
        "Nivel de intensidad": nivel_input,
        "Modo fiesta": modo_fiesta,
        "Modo nocturno": modo_nocturno
    }

    return True


def automatizar_aire_acondicionado():
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
    identificador = int(input("Indique que dispositivo quiere automatizar: "))

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

    automatizaciones[identificador] = {
        "Horario de inicio de la rutina": inicio,
        "Estado del dispositivo": texto_estado,
        "Horario arranque de dispositivo": arranque,
        "Horario apagado de dispositivo": apagado,
        "Velocidad ventilador": velocidad,
        "Modo": modo,
        "Temperatura": temperatura
    }

    return True


def automatizar_ventilador():
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
    identificador = int(input("Indique que dispositivo quiere automatizar: "))

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

    automatizaciones[identificador] = {
        "Horario de inicio de la rutina": inicio,
        "Estado del dispositivo": texto_estado,
        "Horario arranque de dispositivo": arranque,
        "Horario apagado de dispositivo": apagado,
        "Velocidad ventilador": velocidad,
        "Giro": giro
    }

    return True


def agregar_dispositivo():
    nombre = input("Indique el nombre del dispositivo: ")
    tipo = int(input(
        "¿Que tipo de dispositivo es?: "
        "1) Aire acondicionado. "
        "2) Ventilador (Pie, Techo). "
        "3) Encendible (Luces, Computadores personales, cafeteras): "))
    tipo_dispositivo = ""
    if 0 < tipo <= 3:
        if tipo == 1:
            tipo_dispositivo = "AIRE_ACONDICIONADO"
        if tipo == 2:
            tipo_dispositivo = "VENTILADOR"
        if tipo == 3:
            tipo_dispositivo = "ENCENDIBLES"
    else:
        print("Opcion invalida")
    if check_dispositivo_existe_por_nombre(str.upper(nombre)) or len(nombre) < 1:
        print("El dispositivo ya existe o el valor ingresado como nombre es invalido")
        return False
    else:
        dispositivo = {
            "Nombre": str.upper(nombre),
            "Estado": "Encendido",
            "Tipo": tipo_dispositivo
        }
        dispositivos[len(dispositivos) + 1] = dispositivo
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
    nombre = input("Indique el nombre del dispositivo: ")
    encontrado = False
    for id_disp, disp in dispositivos.items():
        if disp['Nombre'] == str.upper(nombre):
            print(f"Identificador del dispositivo: {id_disp}. "
                  f"Nombre:{disp['Nombre']}. "
                  f"Estado:{disp['Estado']}. "
                  f"Tipo:{disp['Tipo']}.")
            encontrado = True
            break
    if not encontrado:
        print("No se encontro el dispositivo")


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
    if len(automatizaciones) == 0:
        print("No hay automatizaciones")
    for key, values in automatizaciones.items():
        print(f"Automatizacion del dispositivo:{key}.")
        for automatizacion, atributo in values.items():
            print(f"{automatizacion}:{atributo}")


def eliminar_automatizacion():
    mostrar_dispositivos()
    identificador = int(input("Ingrese el Identificador del dispositivo cuya rutina desea eliminar: "))
    if not identificador > len(dispositivos) or identificador <= 0:
        if identificador in automatizaciones:
            automatizaciones.pop(identificador)
            print("Rutina eliminada.")
        else:
            print("No existe rutina para el dispositivo")
    else:
        print("Valor invalido.")


if __name__ == "__main__":
    print("La aplicacion debe ejecutarse desde el modulo main.")
