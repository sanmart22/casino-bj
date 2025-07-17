# Importación de librerías para impresión en consola y manejo de paneles
from rich.console import Console
from rich.panel import Panel
import json
import os

# Definición de excepciones personalizadas
# Permite un manejo más claro y específico de errores en el flujo del programa
class UsuarioExistenteError(Exception):
    pass
class UsuarioNoEncontradoError(Exception):
    pass
class ContrasenaIncorrectaError(Exception):
    pass

# Diccionario global para almacenar usuarios en memoria (clave: nombre, valor: contraseña)
# Los diccionarios permiten acceso eficiente a los datos por clave
usuarios = {}

# Ruta al archivo JSON donde se almacenan los balances de fichas
USUARIOS_JSON = os.path.join(os.path.dirname(__file__), 'usuarios.json')

# Funciones para manejar el balance de fichas en JSON
# Uso de archivos: open, read, write, manejo de excepciones y serialización JSON
# El balance es un diccionario (clave: usuario, valor: fichas)
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

# Función para registrar un usuario
# Uso de cadenas para entrada y validación, manejo de excepciones personalizadas
# Actualiza el diccionario de usuarios y el archivo JSON de balances
def registrar_usuario():
    console = Console()
    try:
        nombre = input("Ingrese nombre de usuario: ").strip()
        # Comparación de cadenas y uso de generadores para verificar existencia
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
        # Manejo de excepciones personalizadas
        console.print(Panel(f"Error: {e}", style="bold red"))

# Función para iniciar sesión
# Uso de cadenas, diccionarios y manejo de excepciones personalizadas
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

# Notas generales:
# - Los diccionarios permiten almacenar y acceder a datos de manera eficiente por clave.
# - El manejo de excepciones personalizadas mejora la claridad y robustez del código.
# - El acceso a archivos JSON permite persistir información estructurada entre ejecuciones.
# - Las cadenas de caracteres se manipulan para validar y mostrar información al usuario.
# - El uso de funciones facilita la reutilización y organización del código.