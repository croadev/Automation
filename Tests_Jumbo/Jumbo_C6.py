import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Services.FuncionesManager import FuncionesModular
import time

def main():
    jumbo_modular = FuncionesModular(
        "https://www.jumbo.com.ar")
    try:
        print('Cliente Nuevo, Envío a Domicilio, Electro')
        jumbo_modular.reporteInicial()
        jumbo_modular.direccionNueva(mail="pruebaautomatizada@prueba.com", direccion="Av Lope de Vega 345")
        jumbo_modular.cerrarModal()
        jumbo_modular.buscarArticulo("heladeras")
        time.sleep(5)
        jumbo_modular.addToCart()
        time.sleep(5)
        jumbo_modular.goCart()
        jumbo_modular.irACheckout()
        jumbo_modular.criterio("Criterio Jumbo")
        jumbo_modular.identificacion(
            "Pruebaa", "Discooo", "12/10/95", "11", "56789912", "33333334")
        jumbo_modular.genero(True)
        jumbo_modular.aceptar_terminosycondiciones()
        #jumbo_modular.cerrar_politicas()
        jumbo_modular.goto_deliver()
        jumbo_modular.envioRecurrenteTiendaElectro()
        jumbo_modular.reporteFinal()

    except Exception as e:
        print(e)
        print('Ocurrio un error')
    finally:
        jumbo_modular.quit()


if __name__ == '__main__':
    main()