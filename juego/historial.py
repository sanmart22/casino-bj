historial_partidas = []

def guardar_partida(usuario, resultado, jugador_valor, dealer_valor):
    historial_partidas.append([usuario, resultado, jugador_valor, dealer_valor])

def ver_historial(usuario):
    print("\n--- Historial de Partidas ---")
    partidas_usuario = list(filter(lambda p: p[0] == usuario, historial_partidas))
    for p in partidas_usuario[-5:]:
        print(f"Resultado: {p[1]} | Puntaje: {p[2]} - Dealer: {p[3]}")
