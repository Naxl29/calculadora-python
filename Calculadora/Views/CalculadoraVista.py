from colorama import Fore, Style

class VistaCalculadora:
    @staticmethod
    def menu():
        print(Fore.CYAN + "=== CALCULADORA ===")
        print("1. Realizar operación")
        print("2. Ver historial")
        print("3. Salir")

    @staticmethod
    def datos():
        n1 = int(input("Ingrese el primer número: "))
        signo = input("¿Qué desea realizar? (x, /, +, -): ")
        n2 = int(input("Ingrese el segundo número: "))
        return n1, signo, n2

    def historial(self, operaciones):
        if operaciones:
            print(Fore.CYAN + "=== Historial ===" + Style.RESET_ALL)
            for operacion in operaciones:
                print(f"{operacion[0]}")
        else:
            print(Fore.RED + "No hay operaciones registradas." + Style.RESET_ALL)

