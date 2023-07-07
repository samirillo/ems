import hashlib
import re

def encriptar_password(password):
    # Convertir la contraseña a bytes
    password_bytes = password.encode('utf-8')

    # Generar el hash SHA-256 de la contraseña
    hash_object = hashlib.sha256()
    hash_object.update(password_bytes)
    hash_password = hash_object.hexdigest()

    return hash_password





import hashlib

def verificar_password(password, hash_password):
    # Convertir la contraseña a bytes
    password_bytes = password.encode('utf-8')

    # Generar el hash SHA-256 de la contraseña ingresada
    hash_object = hashlib.sha256()
    hash_object.update(password_bytes)
    hash_input = hash_object.hexdigest()

    # Comparar el hash ingresado con el hash almacenado
    if hash_input == hash_password:
        return True
    else:
        return False


def validar_email(email):
    # Expresión regular para verificar el formato del correo electrónico
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    # Validar el correo electrónico utilizando la expresión regular
    if re.match(patron, email):
        return True
    else:
        return False
