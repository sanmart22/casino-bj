import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from juego.blackjack import calcular_valor_mano, repartir_manos

class TestBlackjack(unittest.TestCase):
    def test_calcular_valor_mano(self):
        mano = [('Corazones', 'A'), ('Diamantes', 'K')]
        self.assertEqual(calcular_valor_mano(mano), 21)

    def test_repartir_manos(self):
        mazo = [('Corazones', 'A'), ('Diamantes', 'K'), ('Tréboles', 'Q'), ('Picas', 'J')]
        jugador_mano, dealer_mano = repartir_manos(mazo)
        self.assertEqual(len(jugador_mano), 2)
        self.assertEqual(len(dealer_mano), 2)

if __name__ == '__main__':
    unittest.main() 