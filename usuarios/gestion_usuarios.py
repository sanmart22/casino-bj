usuarios = {}

def registrar_usuario():
    nombre = input("Ingrese un nombre de usuario: ").strip()
    if nombre.lower() in (n.lower() for n in usuarios):
        print("Este nombre de usuario ya existe.")
        return
    contrasena = input("Ingrese una contraseña: ").strip()
    usuarios[nombre] = contrasena
    print(f"Usuario '{nombre.upper()}' registrado con éxito.")

def iniciar_sesion():
    nombre = input("Ingrese su nombre de usuario: ").strip()
    if nombre not in usuarios:
        print("Usuario no encontrado.")
        return None
    contrasena = input("Ingrese su contraseña: ").strip()
    if usuarios[nombre] == contrasena:
        print(f"Bienvenido, {nombre.capitalize()}!")
        return nombre
    else:
        print("Contraseña incorrecta.")
        return None
    