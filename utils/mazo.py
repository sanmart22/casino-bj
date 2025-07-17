# Importación de la librería random para mezclar el mazo
import random

# Función para crear un mazo de cartas
# Uso de listas, tuplas y comprensión de listas
# El mazo es una lista de tuplas (palo, valor), similar a una matriz de 2 columnas
def crear_mazo(recursivo=False):
    palos = ["Corazones", "Diamantes", "Tréboles", "Picas"]  # Lista de cadenas
    rangos = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]  # Lista de cadenas
    mazo = [(p, r) for p in palos for r in rangos]  # Lista de tuplas (producto cartesiano)
    if recursivo:
        barajar_mazo_recursivo(mazo)
    else:
        random.shuffle(mazo)  # Mezcla aleatoria del mazo (modifica la lista in-place)
    return mazo

# Función recursiva para barajar el mazo
# Implementa el algoritmo de Fisher-Yates de forma recursiva
def barajar_mazo_recursivo(mazo, n=None):
    if n is None:
        n = len(mazo)
    if n <= 1:
        return
    i = random.randint(0, n-1)
    mazo[i], mazo[n-1] = mazo[n-1], mazo[i]
    barajar_mazo_recursivo(mazo, n-1)

# Función para mostrar la mano de un jugador
# Uso de listas, cadenas, tuplas, enumeración y slicing
def mostrar_mano(mano, ocultar_primera=False):
    cartas = []  # Lista para almacenar las representaciones de las cartas
    for i, carta in enumerate(mano):  # Recorrido por índice y valor
        if ocultar_primera and i == 0:
            cartas.append("Carta oculta")  # Uso de cadenas
        else:
            cartas.append(f"{carta[1]} de {carta[0]}")  # Formateo de cadenas y acceso a tuplas
    return ", ".join(cartas)  # Concatenación de cadenas

# Notas generales:
# - Las listas y tuplas permiten representar colecciones de datos estructurados.
# - El uso de comprensión de listas facilita la creación de estructuras complejas.
# - El acceso por índice y slicing es común en la manipulación de listas.
# - Las cadenas de caracteres se usan para mostrar información de manera legible.
# - La recursividad puede ser usada para algoritmos como el barajado de Fisher-Yates.
