import hashlib
import re

message = ""


def encriptar_password(password):
    # Convertir la contraseña a bytes
    password_bytes = password.encode('utf-8')

    # Generar el hash SHA-256 de la contraseña
    hash_object = hashlib.sha256()
    hash_object.update(password_bytes)
    hash_password = hash_object.hexdigest()

    return hash_password


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


def validate_form(data: dict):
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if not all(key in data for key in ["fullname", "phone", "email", "password", "confirm"]):
        message = "Todos los campos son requeridos"
        return False, message

    if not re.match(email_regex, data["email"]):
        message = "Email inválido"
        return False, message

    if data["password"] != data["confirm"]:
        message = "Las contraseñas no coinciden"
        return False, message

    return True, None


def validate_login_form(data: dict):
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not all(key in data for key in ["email", "password"]):
        message = "Todos los campos son requeridos"
        return False, message

    if not re.match(email_regex, data["email"]):
        message = "Email inválido"
        return False, message

    return True, None
