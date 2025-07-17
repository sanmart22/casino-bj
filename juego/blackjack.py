# Importación de librerías para impresión en consola y manejo de paneles
from rich.console import Console
from rich.panel import Panel
from utils.mazo import crear_mazo, mostrar_mano
from .historial import guardar_partida
from usuarios.gestion_usuarios import cargar_balances, guardar_balances

# Función para calcular el valor de una mano de blackjack
# Uso de diccionarios para asignar valores a las cartas
# Uso de listas para representar la mano (lista de tuplas)
def calcular_valor_mano(mano):
    valores = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
        "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11
    }
    # Suma de valores usando comprensión de listas
    suma = sum(valores[c[1]] for c in mano)
    ases = sum(1 for c in mano if c[1] == "A")
    # Ajuste por ases (si la suma supera 21)
    while suma > 21 and ases > 0:
        suma -= 10
        ases -= 1
    return suma

# Función para repartir las manos iniciales
# Uso de listas y slicing para simular el reparto de cartas
def repartir_manos(mazo):
    return ([mazo.pop(), mazo.pop()], [mazo.pop(), mazo.pop()])

# Función para resumir los datos de una partida
# Uso de diccionarios y tuplas para estructurar la información
def resumen_partida(jugador, dealer, resultado):
    return {
        "jugador": tuple(jugador),
        "dealer": tuple(dealer),
        "resultado": resultado,
        "puntaje_jugador": calcular_valor_mano(jugador),
        "puntaje_dealer": calcular_valor_mano(dealer)
    }

# Función principal del juego de blackjack
# Uso de listas para representar las manos, diccionarios para balances, manejo de excepciones, cadenas, input/output, slicing, etc.
def jugar_blackjack(usuario):
    console = Console()
    balances = cargar_balances()  # Diccionario clave-valor (usuario: fichas)
    saldo = balances.get(usuario, 0)
    if saldo <= 0:
        console.print(Panel("No tienes fichas suficientes para jugar. Recarga fichas desde el menú.", style="bold red"))
        return
    while True:
        try:
            apuesta = int(input(f"¿Cuántas fichas quieres apostar? (Saldo: {saldo}): "))
            if apuesta <= 0:
                console.print("La apuesta debe ser mayor a 0.")
            elif apuesta > saldo:
                console.print("No tienes suficientes fichas para esa apuesta.")
            else:
                break
        except ValueError:
            # Manejo de excepciones para entradas no numéricas
            console.print("Ingresa un número válido.")
    saldo -= apuesta
    balances[usuario] = saldo
    guardar_balances(balances)

    console.print(Panel(f"Comienza la partida de Blackjack {usuario}", style="bold cyan"))
    mazo = crear_mazo()  # Lista de tuplas (matriz de cartas)
    jugador_mano, dealer_mano = repartir_manos(mazo)

    console.print(f"Tu mano: {mostrar_mano(jugador_mano)}")
    console.print(f"Mano del dealer: {mostrar_mano(dealer_mano, ocultar_primera=True)}")

    while calcular_valor_mano(jugador_mano) < 21:
        accion = input("Pedir (p) o Plantarse (pl)? ").lower()
        if accion == 'p':
            jugador_mano.append(mazo.pop())
            console.print(f"Tu mano ahora: {mostrar_mano(jugador_mano)} (Valor: {calcular_valor_mano(jugador_mano)})")
            if calcular_valor_mano(jugador_mano) > 21:
                console.print(Panel("Te pasaste, Dealer gana", style="bold red"))
                datos = resumen_partida(jugador_mano, dealer_mano, "Perdiste")
                guardar_partida(usuario, datos["resultado"], datos["puntaje_jugador"], datos["puntaje_dealer"])
                console.print(f"Saldo actual: {saldo}")
                return
        elif accion == 'pl':
            break

    console.print(f"\nMano del dealer: {mostrar_mano(dealer_mano)} (Valor: {calcular_valor_mano(dealer_mano)})")
    while calcular_valor_mano(dealer_mano) < 17:
        dealer_mano.append(mazo.pop())
        console.print(f"Mano del dealer ahora: {mostrar_mano(dealer_mano)} (Valor: {calcular_valor_mano(dealer_mano)})")
        if calcular_valor_mano(dealer_mano) > 21:
            console.print(Panel("El dealer se pasó, ganaste", style="bold green"))
            datos = resumen_partida(jugador_mano, dealer_mano, "Gano")
            saldo += apuesta * 2
            balances[usuario] = saldo
            guardar_balances(balances)
            guardar_partida(usuario, datos["resultado"], datos["puntaje_jugador"], datos["puntaje_dealer"])
            console.print(f"Saldo actual: {saldo}")
            return

    jugador_valor = calcular_valor_mano(jugador_mano)
    dealer_valor = calcular_valor_mano(dealer_mano)

    if jugador_valor > dealer_valor:
        console.print(Panel("Ganaste", style="bold green"))
        resultado = "Gano"
        saldo += apuesta * 2
    elif dealer_valor > jugador_valor:
        console.print(Panel("Gana Dealer", style="bold red"))
        resultado = "Perdio"
        # saldo ya descontado
    else:
        console.print(Panel("Empate", style="bold yellow"))
        resultado = "Empate"
        saldo += apuesta
    balances[usuario] = saldo
    guardar_balances(balances)
    datos = resumen_partida(jugador_mano, dealer_mano, resultado)
    guardar_partida(usuario, datos["resultado"], datos["puntaje_jugador"], datos["puntaje_dealer"])
    console.print(f"Saldo actual: {saldo}")

# Notas generales:
# - Las listas permiten representar manos de cartas y mazos (listas de tuplas).
# - Los diccionarios permiten estructurar información de partidas y balances.
# - El manejo de excepciones previene errores por entradas inválidas.
# - Las cadenas de caracteres se usan para interacción y formateo de mensajes.
# - El acceso a archivos permite persistir datos de partidas y balances.
# - El uso de slicing y comprensión de listas es común en la manipulación de colecciones.
# - Las funciones facilitan la organización y reutilización del código.