from cryptography.fernet import Fernet

import os

CLAVE_PATH = "clave.key"

def guardar_clave(path=CLAVE_PATH):
    clave = Fernet.generate_key()
    with open(path, "wb") as f:
        f.write(clave)

def cargar_clave(path=CLAVE_PATH):
    if not os.path.exists(path):
        guardar_clave(path)
    with open(path, "rb") as f:
        return f.read()

clave = cargar_clave()
fernet = Fernet(clave)      

def cifrar_contraseña(password: str) -> bytes:
    """
    Cifra la contraseña usando Fernet y devuelve la versión cifrada en bytes.
    """
    return fernet.encrypt(password.encode())

def descifrar_contraseña(password_cifrada: bytes) -> str:
    """
    Descifra la contraseña y la devuelve como string plano.
    """
    return fernet.decrypt(password_cifrada).decode()