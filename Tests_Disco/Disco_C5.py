import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Services.FuncionesManager import FuncionesModular
import time

def main():
    disco_modular = FuncionesModular(
        "https://www.disco.com.ar")
    try:
        print('Cliente Nuevo, Envío a Domicilio, Food')
        disco_modular.reporteInicial()
        disco_modular.direccionNuevaDV1(mail="pruebaautomatizada@prueba.com", direccion="Av Lope de Vega 345")
        disco_modular.nextdir()
        disco_modular.direcconNuevaDV2()
        disco_modular.cerrarModal()
        disco_modular.buscarArticulo("Whisky")
        time.sleep(5)
        disco_modular.addToCart()
        time.sleep(5)
        disco_modular.goCart()
        disco_modular.irACheckout()
        disco_modular.criterio("Criterio Disco")
        disco_modular.identificacion(
            "Prueba", "Disco", "12/10/95", "11", "56789912", "33333334")
        disco_modular.genero(True)
        disco_modular.aceptar_terminosycondiciones()
        disco_modular.cerrar_politicas()
        disco_modular.goto_deliver()
        disco_modular.envioClienteNuevo()
        disco_modular.reporteFinal()


    except Exception as e:
        print(e)
        print('Ocurrio un error')
    finally:
        disco_modular.quit()


if __name__ == '__main__':
    main()
