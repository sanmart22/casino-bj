# Importación de módulos para pruebas unitarias y manipulación de rutas
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from usuarios.gestion_usuarios import registrar_usuario, iniciar_sesion, usuarios

# Clase de pruebas unitarias para la gestión de usuarios
# Uso de la librería unittest y funciones assert
class TestGestionUsuarios(unittest.TestCase):
    def setUp(self):
        usuarios.clear()  # Limpia el diccionario de usuarios antes de cada prueba

    def test_registrar_usuario(self):
        # Prueba de registro de usuario (modifica el diccionario usuarios)
        registrar_usuario()
        self.assertIn('test_user', usuarios)  # Verifica que el usuario fue agregado

    def test_iniciar_sesion(self):
        # Prueba de inicio de sesión (verifica acceso a diccionario y manejo de cadenas)
        usuarios['test_user'] = 'test_pass'
        self.assertEqual(iniciar_sesion(), 'test_user')

# Punto de entrada para ejecutar las pruebas unitarias
if __name__ == '__main__':
    unittest.main() 

# Notas generales:
# - Las pruebas unitarias permiten verificar el correcto funcionamiento de funciones y módulos.
# - El uso de assert ayuda a detectar errores de manera temprana.
# - Los diccionarios se usan para almacenar usuarios y contraseñas.
# - El manejo de cadenas es fundamental para la validación de usuarios.
# - La modularización y las pruebas facilitan el mantenimiento y la calidad del código. 