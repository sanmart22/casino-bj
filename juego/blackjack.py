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

def jugar_blackjack(usuario):
    print(f"\nComienza la partida de Blackjack {usuario}")
    mazo = crear_mazo()
    jugador_mano = [mazo.pop(), mazo.pop()]
    dealer_mano = [mazo.pop(), mazo.pop()]

    print(f"Tu mano: {mostrar_mano(jugador_mano)}")
    print(f"Mano del dealer: {mostrar_mano(dealer_mano, ocultar_primera=True)}")

    while calcular_valor_mano(jugador_mano) < 21:
        accion = input("Pedir (p) o Plantarse (pl)? ").lower()
        if accion == 'p':
            jugador_mano.append(mazo.pop())
            print(f"Tu mano ahora: {mostrar_mano(jugador_mano)} (Valor: {calcular_valor_mano(jugador_mano)})")
            if calcular_valor_mano(jugador_mano) > 21:
                print("Te pasaste, Dealer gana")
                guardar_partida(usuario, "Perdiste", calcular_valor_mano(jugador_mano), calcular_valor_mano(dealer_mano))
                return
        elif accion == 'pl':
            break

    print(f"\nMano del dealer: {mostrar_mano(dealer_mano)} (Valor: {calcular_valor_mano(dealer_mano)})")
    while calcular_valor_mano(dealer_mano) < 17:
        dealer_mano.append(mazo.pop())
        print(f"Mano del dealer ahora: {mostrar_mano(dealer_mano)} (Valor: {calcular_valor_mano(dealer_mano)})")
        if calcular_valor_mano(dealer_mano) > 21:
            print("El dealer se paso, ganaste")
            guardar_partida(usuario, "Gano", calcular_valor_mano(jugador_mano), calcular_valor_mano(dealer_mano))
            return

    jugador_valor = calcular_valor_mano(jugador_mano)
    dealer_valor = calcular_valor_mano(dealer_mano)
    if jugador_valor > dealer_valor:
        print("Ganaste")
        guardar_partida(usuario, "Gano", jugador_valor, dealer_valor)
    elif dealer_valor > jugador_valor:
        print("Gana Dealer")
        guardar_partida(usuario, "Perdio", jugador_valor, dealer_valor)
    else:
        print("Empate")
        guardar_partida(usuario, "Empate", jugador_valor, dealer_valor)
