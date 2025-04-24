from usuarios.gestion_usuarios import registrar_usuario, iniciar_sesion
from juego.blackjack import jugar_blackjack
from juego.historial import ver_historial

def mostrar_menu():
    print("\nCasino BC")
    print("1. Registrarse")
    print("2. Iniciar Sesión")
    print("3. Jugar Blackjack")
    print("4. Ver Historial")
    print("5. Salir")

def main():
    usuario_actual = None
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            usuario_actual = iniciar_sesion()
        elif opcion == '3':
            if usuario_actual:
                jugar_blackjack(usuario_actual)
            else:
                print("Tenes que iniciar sesión para jugar")
        elif opcion == '4':
            if usuario_actual:
                ver_historial(usuario_actual)
            else:
                print("Tenes que iniciar sesión para ver el historial")
        elif opcion == '5':
            print("Gracias por visitarnos")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
