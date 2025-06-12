from rich.console import Console
from rich.panel import Panel

class UsuarioExistenteError(Exception):
    pass
class UsuarioNoEncontradoError(Exception):
    pass
class ContrasenaIncorrectaError(Exception):
    pass
usuarios = {}

def registrar_usuario():
    console = Console()
    try:
        nombre = input("Ingrese nombre de usuario: ").strip()
        if nombre.lower() in (n.lower() for n in usuarios):
            raise UsuarioExistenteError(f"El usuario '{nombre}' ya existe")
        
        contrasena = input("Ingrese contraseña: ").strip()
        usuarios[nombre] = contrasena
        console.print(Panel(f"Usuario '{nombre.upper()}' registrado con éxito", style="bold green"))

    except UsuarioExistenteError as e:
        console.print(Panel(f"Error: {e}", style="bold red"))

def iniciar_sesion():
    console = Console()
    try:
        nombre = input("Ingrese nombre de usuario: ").strip()
        if nombre not in usuarios:
            raise UsuarioNoEncontradoError(f"El usuario '{nombre}' no existe")
        
        contrasena = input("Ingrese contraseña: ").strip()
        if usuarios[nombre] != contrasena:
            raise ContrasenaIncorrectaError("Contraseña incorrecta")
        else:
            console.print(Panel(f"Bienvenido, {nombre.upper()}!", style="bold green"))
        return nombre
    except UsuarioNoEncontradoError as e:
        console.print(Panel(f"Error: {e}", style="bold red"))
    except ContrasenaIncorrectaError as e:
        console.print(Panel(f"Error: {e}", style="bold red"))