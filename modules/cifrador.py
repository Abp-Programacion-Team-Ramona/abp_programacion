def cifrar_contraseña(password, desplazamiento=3):
    return ''.join(chr((ord(c) + desplazamiento) % 256) for c in password)


def descifrar_contraseña(password_cifrada, desplazamiento=3):
    return ''.join(chr((ord(c) - desplazamiento) % 256) for c in password_cifrada)
