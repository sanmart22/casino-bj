from rich.console import Console
from rich.panel import Panel
import json
import os

class UsuarioExistenteError(Exception):
    pass
class UsuarioNoEncontradoError(Exception):
    pass
class ContrasenaIncorrectaError(Exception):
    pass
usuarios = {}

USUARIOS_JSON = os.path.join(os.path.dirname(__file__), 'usuarios.json')

# Funciones para manejar el balance de fichas en JSON
def cargar_balances():
    if not os.path.exists(USUARIOS_JSON):
        return {}
    with open(USUARIOS_JSON, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def guardar_balances(balances):
    with open(USUARIOS_JSON, 'w', encoding='utf-8') as f:
        json.dump(balances, f, indent=4)

def registrar_usuario():
    console = Console()
    try:
        nombre = input("Ingrese nombre de usuario: ").strip()
        if nombre.lower() in (n.lower() for n in usuarios):
            raise UsuarioExistenteError(f"El usuario '{nombre}' ya existe")
        
        contrasena = input("Ingrese contraseña: ").strip()
        usuarios[nombre] = contrasena
        # Balance inicial de 100 fichas
        balances = cargar_balances()
        balances[nombre] = 100
        guardar_balances(balances)
        console.print(Panel(f"Usuario '{nombre.upper()}' registrado con éxito con 100 fichas", style="bold green"))

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