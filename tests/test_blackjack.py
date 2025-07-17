# Importación de módulos para pruebas unitarias y manipulación de rutas
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from juego.blackjack import calcular_valor_mano, repartir_manos

# Clase de pruebas unitarias para el módulo de blackjack
# Uso de la librería unittest y funciones assert
class TestBlackjack(unittest.TestCase):
    def test_calcular_valor_mano(self):
        # Prueba de suma de valores en una mano (lista de tuplas)
        mano = [('Corazones', 'A'), ('Diamantes', 'K')]
        self.assertEqual(calcular_valor_mano(mano), 21)  # Uso de assert para verificar el resultado

    def test_repartir_manos(self):
        # Prueba de reparto de cartas usando listas y slicing
        mazo = [('Corazones', 'A'), ('Diamantes', 'K'), ('Tréboles', 'Q'), ('Picas', 'J')]
        jugador_mano, dealer_mano = repartir_manos(mazo)
        self.assertEqual(len(jugador_mano), 2)
        self.assertEqual(len(dealer_mano), 2)

# Punto de entrada para ejecutar las pruebas unitarias
if __name__ == '__main__':
    unittest.main() 

# Notas generales:
# - Las pruebas unitarias permiten verificar el correcto funcionamiento de funciones y módulos.
# - El uso de assert ayuda a detectar errores de manera temprana.
# - Las listas y tuplas se usan para representar manos y mazos de cartas.
# - La modularización y las pruebas facilitan el mantenimiento y la calidad del código. 