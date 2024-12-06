from colorama import Fore, Style
import sys

class ControladorCalculadora:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar(self):
        while True:
            self.vista.menu()
            opcion = input(Fore.YELLOW + "Seleccione una opción: " + Style.RESET_ALL)
            match opcion:
                case '1':
                    while True:
                        try:
                            n1, signo, n2 = self.vista.datos()
                            
                            while signo not in ["/", "x", "+", "-"]:
                                print(Fore.RED + "Opción incorrecta. Por favor, ingrese una operación válida: /, x, +, -." + Style.RESET_ALL)
                                n1, signo, n2 = self.vista.datos()

                            self.modelo.agregar_operacion(n1, signo, n2)

                            id_operacion = self.modelo.ultimo_id()
                        
                            if signo == "/":
                                resultado = n1 / n2
                                print(Fore.GREEN + f"El resultado es: {resultado}")
                                self.modelo.agregar_resultado(resultado)

                                id_resultado = self.modelo.ultimo_id()
                                self.modelo.op_re(id_operacion, id_resultado)
                                break
                            elif signo == "x":
                                resultado = n1 * n2
                                print(Fore.GREEN + f"El resultado es: {resultado}")
                                self.modelo.agregar_resultado(resultado)

                                id_resultado = self.modelo.ultimo_id()
                                self.modelo.op_re(id_operacion, id_resultado)
                                break
                            elif signo == "+":
                                resultado = n1 + n2
                                print(Fore.GREEN + f"El resultado es: {resultado}")
                                self.modelo.agregar_resultado(resultado)
                                
                                id_resultado = self.modelo.ultimo_id()
                                self.modelo.op_re(id_operacion, id_resultado)
                                break
                            elif signo == "-":
                                resultado = n1 - n2
                                print(Fore.GREEN + f"El resultado es: {resultado}")
                                self.modelo.agregar_resultado(resultado)

                                id_resultado = self.modelo.ultimo_id()
                                self.modelo.op_re(id_operacion, id_resultado)
                                break
                        except ValueError:
                            print(Fore.RED + "Opción incorrecta" + Style.RESET_ALL)
                case '2':
                    operaciones = self.modelo.ver_historial()
                    self.vista.historial(operaciones) 

                case '3':
                    print(Fore.CYAN + "Saliendo de la calculadora")
                    sys.exit(0)
                case _:
                    print(Fore.RED + "Opción incorrecta")

