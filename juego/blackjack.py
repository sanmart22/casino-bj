
from utils.mazo import crear_mazo, mostrar_mano
from .historial import guardar_partida

def calcular_valor_mano(mano):
    valores = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
        "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11
    }
    suma = sum(valores[c[1]] for c in mano)
    ases = sum(1 for c in mano if c[1] == "A")
    while suma > 21 and ases > 0:
        suma -= 10
        ases -= 1
    return suma

def repartir_manos(mazo):
    return ([mazo.pop(), mazo.pop()], [mazo.pop(), mazo.pop()])

def resumen_partida(jugador, dealer, resultado):
    return {
        "jugador": tuple(jugador),
        "dealer": tuple(dealer),
        "resultado": resultado,
        "puntaje_jugador": calcular_valor_mano(jugador),
        "puntaje_dealer": calcular_valor_mano(dealer)
    }

def jugar_blackjack(usuario):
    print(f"\nComienza la partida de Blackjack {usuario}")
    mazo = crear_mazo()
    jugador_mano, dealer_mano = repartir_manos(mazo)

    print(f"Tu mano: {mostrar_mano(jugador_mano)}")
    print(f"Mano del dealer: {mostrar_mano(dealer_mano, ocultar_primera=True)}")

    while calcular_valor_mano(jugador_mano) < 21:
        accion = input("Pedir (p) o Plantarse (pl)? ").lower()
        if accion == 'p':
            jugador_mano.append(mazo.pop())
            print(f"Tu mano ahora: {mostrar_mano(jugador_mano)} (Valor: {calcular_valor_mano(jugador_mano)})")
            if calcular_valor_mano(jugador_mano) > 21:
                print("Te pasaste, Dealer gana")
                datos = resumen_partida(jugador_mano, dealer_mano, "Perdiste")
                guardar_partida(usuario, datos["resultado"], datos["puntaje_jugador"], datos["puntaje_dealer"])
                return
        elif accion == 'pl':
            break

    print(f"\nMano del dealer: {mostrar_mano(dealer_mano)} (Valor: {calcular_valor_mano(dealer_mano)})")
    while calcular_valor_mano(dealer_mano) < 17:
        dealer_mano.append(mazo.pop())
        print(f"Mano del dealer ahora: {mostrar_mano(dealer_mano)} (Valor: {calcular_valor_mano(dealer_mano)})")
        if calcular_valor_mano(dealer_mano) > 21:
            print("El dealer se paso, ganaste")
            datos = resumen_partida(jugador_mano, dealer_mano, "Gano")
            guardar_partida(usuario, datos["resultado"], datos["puntaje_jugador"], datos["puntaje_dealer"])
            return

    jugador_valor = calcular_valor_mano(jugador_mano)
    dealer_valor = calcular_valor_mano(dealer_mano)

    if jugador_valor > dealer_valor:
        print("Ganaste")
        resultado = "Gano"
    elif dealer_valor > jugador_valor:
        print("Gana Dealer")
        resultado = "Perdio"
    else:
        print("Empate")
        resultado = "Empate"

    datos = resumen_partida(jugador_mano, dealer_mano, resultado)
    guardar_partida(usuario, datos["resultado"], datos["puntaje_jugador"], datos["puntaje_dealer"])