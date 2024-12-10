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
                            n1 = self.vista.n1()
                            signo = self.vista.signo()
                            while True:
                                if signo in ["/", "*", "+", "-"]:
                                    n2 = self.vista.n2()
                                    self.modelo.agregar_operacion(n1, signo, n2)
                                    break
                                else:
                                    print(Fore.RED + "Opción incorrecta. Por favor, ingrese una operación válida: /, *, +, -." + Style.RESET_ALL)
                                    signo = self.vista.signo()

                            id_operacion = self.modelo.ultimo_id()
                        
                            if signo == "/":
                                while True:
                                    try:
                                        resultado = n1 / n2
                                        print(Fore.GREEN + f"El resultado es: {resultado}")
                                        self.modelo.agregar_resultado(resultado)
                                        
                                        id_resultado = self.modelo.ultimo_id()
                                        self.modelo.op_re(id_operacion, id_resultado)
                                        break
                                    except ZeroDivisionError:
                                        print(Fore.RED + "Error: No se puede dividir por 0" + Style.RESET_ALL)
                                break
                            elif signo == "*":
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
                    while True:
                        op = self.vista.preguntar_historial()
                        if op == "si":
                            operaciones = self.modelo.ver_historial()
                            self.vista.historial_t(operaciones)
                            break
                        elif op == "no":
                            operaciones = self.modelo.ver_h()
                            self.vista.historial(operaciones)
                            break
                        else:
                            print(Fore.RED + "Opción incorrecta" + Style.RESET_ALL) 

                case '3':
                    while True:
                        eli = self.vista.borrar_h()
                        if eli == "si":
                            self.modelo.borrar_historial()
                            print(Fore.GREEN + "Historial eliminado" + Style.RESET_ALL)
                            break
                        elif eli == "no":
                            break
                        else:
                            print(Fore.RED + "Opción incorrecta" + Style.RESET_ALL) 
                case '4':
                    print(Fore.CYAN + "Saliendo de la calculadora")
                    sys.exit(0)
                case _:
                    print(Fore.RED + "Opción incorrecta")

