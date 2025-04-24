import random

def crear_mazo():
    palos = ["Corazones", "Diamantes", "Tréboles", "Picas"]
    rangos = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    mazo = [(p, r) for p in palos for r in rangos]
    random.shuffle(mazo)
    return mazo

def mostrar_mano(mano, ocultar_primera=False):
    cartas = []
    for i, carta in enumerate(mano):
        if ocultar_primera and i == 0:
            cartas.append("Carta oculta")
        else:
            cartas.append(f"{carta[1]} de {carta[0]}")
    return ", ".join(cartas)
