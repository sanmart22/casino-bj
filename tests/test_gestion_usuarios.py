import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from usuarios.gestion_usuarios import registrar_usuario, iniciar_sesion, usuarios

class TestGestionUsuarios(unittest.TestCase):
    def setUp(self):
        usuarios.clear()

    def test_registrar_usuario(self):
        registrar_usuario()
        self.assertIn('test_user', usuarios)

    def test_iniciar_sesion(self):
        usuarios['test_user'] = 'test_pass'
        self.assertEqual(iniciar_sesion(), 'test_user')

if __name__ == '__main__':
    unittest.main() 