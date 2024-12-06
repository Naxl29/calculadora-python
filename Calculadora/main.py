from Models.Calculadora import ModeloCalculadora
from Views.CalculadoraVista import VistaCalculadora
from Controllers.CalculadoraControlador import ControladorCalculadora

if __name__ == "__main__":
    modelo = ModeloCalculadora()
    vista = VistaCalculadora()
    controlador = ControladorCalculadora(modelo, vista)
    controlador.ejecutar()