from usuarios.gestion_usuarios import registrar_usuario, iniciar_sesion, cargar_balances, guardar_balances
from juego.blackjack import jugar_blackjack
from juego.historial import ver_historial
from rich.console import Console
from rich.panel import Panel

def mostrar_menu():
    console = Console()
    menu = """
[bold cyan]Casino BC[/bold cyan]
[bold yellow]1.[/bold yellow] Registrarse
[bold yellow]2.[/bold yellow] Iniciar Sesión
[bold yellow]3.[/bold yellow] Jugar Blackjack
[bold yellow]4.[/bold yellow] Ver Historial
[bold yellow]5.[/bold yellow] Recargar Fichas
[bold yellow]6.[/bold yellow] Salir
"""
    console.print(Panel(menu, title="[bold green]Menú Principal[/bold green]", expand=False))

def main():
    console = Console()
    usuario_actual = None
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        console.print(Panel(f"Has seleccionado la opción: {opcion}", style="bold blue"))

        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            usuario_actual = iniciar_sesion()
        elif opcion == '3':
            if usuario_actual:
                jugar_blackjack(usuario_actual)
            else:
                console.print("[bold red]Tenes que iniciar sesión para jugar[/bold red]")
        elif opcion == '4':
            if usuario_actual:
                ver_historial(usuario_actual)
            else:
                console.print("[bold red]Tenes que iniciar sesión para ver el historial[/bold red]")
        elif opcion == '5':
            if usuario_actual:
                balances = cargar_balances()
                saldo = balances.get(usuario_actual, 0)
                try:
                    monto = int(input(f"¿Cuántas fichas quieres recargar? (Saldo actual: {saldo}): "))
                    if monto > 0:
                        saldo += monto
                        balances[usuario_actual] = saldo
                        guardar_balances(balances)
                        console.print(Panel(f"Recargaste {monto} fichas. Nuevo saldo: {saldo}", style="bold green"))
                    else:
                        console.print("[bold red]El monto debe ser mayor a 0[/bold red]")
                except ValueError:
                    console.print("[bold red]Ingresa un número válido[/bold red]")
            else:
                console.print("[bold red]Tenes que iniciar sesión para recargar fichas[/bold red]")
        elif opcion == '6':
            console.print(Panel("Gracias por visitarnos", style="bold green"))
            break
        else:
            console.print("[bold red]Opción inválida[/bold red]")

if __name__ == "__main__":
    main()
