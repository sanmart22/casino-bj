from rich.console import Console
from rich.panel import Panel
import json
import os

HISTORIAL_JSON = os.path.join(os.path.dirname(__file__), 'historial.json')

def cargar_historial():
    if not os.path.exists(HISTORIAL_JSON):
        return []
    with open(HISTORIAL_JSON, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def guardar_historial(historial):
    with open(HISTORIAL_JSON, 'w', encoding='utf-8') as f:
        json.dump(historial, f, indent=4)

def guardar_partida(usuario, resultado, jugador_valor, dealer_valor):
    historial = cargar_historial()
    historial.append({
        'usuario': usuario,
        'resultado': resultado,
        'jugador_valor': jugador_valor,
        'dealer_valor': dealer_valor
    })
    guardar_historial(historial)

def ver_historial(usuario):
    console = Console()
    console.print(Panel("--- Historial de Partidas ---", style="bold cyan"))
    historial = cargar_historial()
    partidas_usuario = [p for p in historial if p['usuario'] == usuario]
    for p in partidas_usuario[-5:]:
        console.print(f"Resultado: {p['resultado']} | Puntaje: {p['jugador_valor']} - Dealer: {p['dealer_valor']}")
