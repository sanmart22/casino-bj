class UsuarioExistenteError(Exception):
    pass
class UsuarioNoEncontradoError(Exception):
    pass
class ContrasenaIncorrectaError(Exception):
    pass
usuarios = {}

def registrar_usuario():
    try:
        nombre = input("Ingrese nombre de usuario: ").strip()
        if nombre.lower() in (n.lower() for n in usuarios):
            raise UsuarioExistenteError(f"El usuario '{nombre}' ya existe")
        
        contrasena = input("Ingrese contraseña: ").strip()
        usuarios[nombre] = contrasena
        print(f"Usuario '{nombre.upper()}' registrado con exito")

    except UsuarioExistenteError as e:
        print(f"Error: {e}")

def iniciar_sesion():
    try:
        nombre = input("Ingrese nombre de usuario: ").strip()
        if nombre not in usuarios:
            raise UsuarioNoEncontradoError(f"El usuario '{nombre}' no existe")
        
        contrasena = input("Ingrese contraseña: ").strip()
        if usuarios[nombre] != contrasena:
            raise ContrasenaIncorrectaError("Contraseña incorrecta")
        else:
            print(f"Bienvenido, {nombre.upper()}!")
        return nombre
    except UsuarioNoEncontradoError as e:
        print(f"Error: {e}")
    except ContrasenaIncorrectaError as e:
        print(f"Error: {e}")