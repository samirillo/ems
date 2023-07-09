import hashlib
import re

message=""
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


def validate_form(name, phone, email, password, confirm_password):
    global message
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not name or not phone or not email or not password or not confirm_password:
        message = "todos los campos son requeridos"
        return False
    # Validación de formato de correo electrónico

    elif not re.match(email_regex, email):
        message="email invalido"
        return False
    elif password != confirm_password:
        message="las contraseñas no coinciden"
        return False

    else:

        return True


def validar_email(email):
    # Expresión regular para verificar el formato del correo electrónico
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    # Validar el correo electrónico utilizando la expresión regular
    if re.match(patron, email):
        return True
    else:
        return False


def compare_textfields(password, confirm_password):
    if password == confirm_password:
        return True
