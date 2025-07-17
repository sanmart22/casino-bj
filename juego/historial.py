# Importación de librerías para impresión en consola con formato
from rich.console import Console
from rich.panel import Panel
# Importación de librerías para manejo de archivos y JSON
import json
import os

# HISTORIAL_JSON es la ruta al archivo donde se almacena el historial de partidas en formato JSON
HISTORIAL_JSON = os.path.join(os.path.dirname(__file__), 'historial.json')

# Función para cargar el historial desde el archivo JSON
# Uso de archivos: open, read, manejo de excepciones y serialización JSON
# El historial es una lista de diccionarios (cada diccionario representa una partida)
def cargar_historial():
    if not os.path.exists(HISTORIAL_JSON):
        return []  # Retorna una lista vacía si el archivo no existe
    with open(HISTORIAL_JSON, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)  # Carga y retorna la lista de partidas
        except json.JSONDecodeError:
            return []  # Si el archivo está vacío o corrupto, retorna lista vacía

# Función para guardar el historial en el archivo JSON
# Uso de archivos: open, write, serialización con json.dump
def guardar_historial(historial):
    with open(HISTORIAL_JSON, 'w', encoding='utf-8') as f:
        json.dump(historial, f, indent=4)  # Guarda la lista de partidas en formato JSON

# Función para agregar una partida al historial
# El historial es una lista (estructura similar a una matriz de una sola dimensión de objetos)
# Cada partida es un diccionario (clave-valor) con los datos relevantes
# Diccionarios permiten acceso eficiente por clave y son útiles para estructurar datos complejos
# Manejo de excepciones implícito al cargar y guardar archivos
# Ejemplo de uso de listas, diccionarios y archivos en conjunto
def guardar_partida(usuario, resultado, jugador_valor, dealer_valor):
    historial = cargar_historial()  # Lista de partidas
    historial.append({
        'usuario': usuario,
        'resultado': resultado,
        'jugador_valor': jugador_valor,
        'dealer_valor': dealer_valor
    })
    guardar_historial(historial)

# Función para mostrar el historial de partidas de un usuario
# Uso de slicing para mostrar solo las últimas 5 partidas
# Uso de listas, diccionarios y acceso por clave
# Uso de cadenas de caracteres para formatear la salida
def ver_historial(usuario):
    console = Console()
    console.print(Panel("--- Historial de Partidas ---", style="bold cyan"))
    historial = cargar_historial()  # Lista de diccionarios
    # Usando filter y lambda para filtrar partidas del usuario
    partidas_usuario = list(filter(lambda p: p['usuario'] == usuario, historial))
    for p in partidas_usuario[-5:]:
        console.print(f"Resultado: {p['resultado']} | Puntaje: {p['jugador_valor']} - Dealer: {p['dealer_valor']}")

# Notas generales:
# - Las listas en Python permiten almacenar secuencias de elementos y pueden ser usadas como matrices (listas de listas).
# - Los diccionarios permiten almacenar pares clave-valor y son útiles para representar objetos o registros.
# - El manejo de archivos con 'with' asegura el cierre adecuado del archivo.
# - El módulo json permite serializar y deserializar datos estructurados.
# - El manejo de excepciones es fundamental para evitar errores en tiempo de ejecución y mejorar la robustez del código.
# - Las cadenas de caracteres pueden manipularse con métodos como format, lower, upper, strip, etc.
# - Las pruebas unitarias pueden implementarse para verificar el correcto funcionamiento de estas funciones.
