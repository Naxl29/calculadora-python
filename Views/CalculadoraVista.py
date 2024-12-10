from colorama import Fore, Style
from tabulate import tabulate
class VistaCalculadora:
    @staticmethod
    def menu():
        print(Fore.CYAN + "=== CALCULADORA ===")
        print("1. Realizar operación")
        print("2. Ver historial")
        print("3. Eliminar historial")
        print("4. Salir")

    @staticmethod
    def n1():
        n1 = int(input("Ingrese el primer número: "))
        return n1

    @staticmethod
    def signo():
        signo = input("¿Qué desea realizar? (*, /, +, -): ")
        return signo

    @staticmethod
    def n2():
        n2 = int(input("Ingrese el segundo número: "))
        return n2
        
    @staticmethod
    def historial_t(operaciones):
        if operaciones:
            print(Fore.CYAN + "=== Historial ===" + Style.RESET_ALL)
            
            columnas = ["ID", "Número 1", "Signo", "Número 2", "Resultado"]
            
            print(tabulate(operaciones, headers=columnas, tablefmt="fancy_grid"))
        else:
            print(Fore.RED + "No hay operaciones registradas." + Style.RESET_ALL)

    @staticmethod
    def preguntar_historial():
        return input(Fore.GREEN + "¿Desea ver el historial en forma de tabla? (si/no): " + Style.RESET_ALL)
    
    @staticmethod
    def historial(operaciones):
        if operaciones:
            print(Fore.CYAN + "=== Historial ===" + Style.RESET_ALL)
            for operacion in operaciones:
                print(f"{operacion[0]}")
        else:
            print(Fore.RED + "No hay operaciones registradas." + Style.RESET_ALL)


    @staticmethod
    def borrar_h():
        return input(Fore.GREEN + "¿Está seguro de eliminar todo el historial? (si/no): " + Style.RESET_ALL)