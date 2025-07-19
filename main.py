# Importación de funciones de otros módulos del proyecto
# Permite la reutilización de código y la organización en archivos separados
from usuarios.gestion_usuarios import registrar_usuario, iniciar_sesion, cargar_balances, guardar_balances
from juego.blackjack import jugar_blackjack
from juego.historial import ver_historial
from rich.console import Console
from rich.panel import Panel

# Función para mostrar el menú principal
# Uso de cadenas de caracteres para formatear la interfaz
# Uso de triple comillas para cadenas multilínea
# Uso de la librería rich para mejorar la visualización en consola
def mostrar_menu():
    console = Console()
    menu = """
[bold cyan]Casino BJ[/bold cyan]
[bold yellow]1.[/bold yellow] Registrarse
[bold yellow]2.[/bold yellow] Iniciar Sesión
[bold yellow]3.[/bold yellow] Jugar Blackjack
[bold yellow]4.[/bold yellow] Ver Historial
[bold yellow]5.[/bold yellow] Recargar Fichas
[bold yellow]6.[/bold yellow] Salir
"""
    console.print(Panel(menu, title="[bold green]Menú Principal[/bold green]", expand=False))

# Función principal del programa
# Uso de bucle while para mantener el menú activo hasta que el usuario decida salir
# Manejo de excepciones implícito en las funciones importadas
# Uso de diccionarios para almacenar balances de fichas
# Uso de cadenas para la interacción con el usuario
def main():
    console = Console()
    usuario_actual = None  # Variable para almacenar el usuario logueado (puede ser None o una cadena)
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        console.print(Panel(f"Has seleccionado la opción: {opcion}", style="bold blue"))

        if opcion == '1':
            registrar_usuario()  # Registro de usuario (ver manejo de diccionarios y archivos en gestion_usuarios.py)
        elif opcion == '2':
            usuario_actual = iniciar_sesion()  # Inicio de sesión (manejo de excepciones y diccionarios)
        elif opcion == '3':
            if usuario_actual:
                jugar_blackjack(usuario_actual)  # Juego principal (ver manejo de listas, diccionarios y archivos en blackjack.py)
            else:
                console.print("[bold red]Tenes que iniciar sesión para jugar[/bold red]")
        elif opcion == '4':
            if usuario_actual:
                ver_historial(usuario_actual)  # Visualización del historial (ver manejo de listas, diccionarios y archivos en historial.py)
            else:
                console.print("[bold red]Tenes que iniciar sesión para ver el historial[/bold red]")
        elif opcion == '5':
            if usuario_actual:
                balances = cargar_balances()  # Carga de diccionario desde archivo JSON
                saldo = balances.get(usuario_actual, 0)
                try:
                    monto = int(input(f"¿Cuántas fichas quieres recargar? (Saldo actual: {saldo}): "))
                    if monto > 0:
                        saldo += monto
                        balances[usuario_actual] = saldo
                        guardar_balances(balances)  # Guardado de diccionario en archivo JSON
                        console.print(Panel(f"Recargaste {monto} fichas. Nuevo saldo: {saldo}", style="bold green"))
                    else:
                        console.print("[bold red]El monto debe ser mayor a 0[/bold red]")
                except ValueError:
                    # Manejo de excepciones: ValueError si el input no es un número
                    console.print("[bold red]Ingresa un número válido[/bold red]")
            else:
                console.print("[bold red]Tenes que iniciar sesión para recargar fichas[/bold red]")
        elif opcion == '6':
            console.print(Panel("Gracias por visitarnos", style="bold green"))
            break
        else:
            console.print("[bold red]Opción inválida[/bold red]")

# Punto de entrada del programa
# Uso de la variable especial __name__ para permitir la ejecución directa o importación como módulo
if __name__ == "__main__":
    main()

# Notas:
# - El uso de diccionarios permite almacenar balances de fichas por usuario (clave: nombre, valor: fichas).
# - El manejo de excepciones previene errores por entradas inválidas.
# - Las cadenas de caracteres se usan para la interacción y formateo de mensajes.
# - El acceso a archivos JSON permite persistir datos entre ejecuciones.
# - La modularización facilita la organización y reutilización del código.
