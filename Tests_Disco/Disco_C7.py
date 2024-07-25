import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Services.FuncionesManager import FuncionesModular
import time


def main():
    Disco_modular = FuncionesModular(
        "https://www.disco.com.ar")
    try:
        print('Cliente Nuevo, Retiro en Tienda, Food')
        Disco_modular.reporteInicial()
        Disco_modular.sucursalClienteNuevo(
            prov="CABA", seller="Disco Alto Palermo", direccion_email="pruebaautomatizada@prueba.com")
        Disco_modular.cerrarModal()
        Disco_modular.buscarArticulo("Whisky")
        time.sleep(5)
        Disco_modular.addToCart()
        time.sleep(5)
        Disco_modular.goCart()
        Disco_modular.irACheckout()
        Disco_modular.criterio("Criterio Disco")
        Disco_modular.identificacion(
            "Prueba", "Disco", "12/10/95", "11", "56789912", "33333334")
        Disco_modular.genero(True)
        Disco_modular.aceptar_terminosycondiciones()
        Disco_modular.cerrar_politicas()
        Disco_modular.goto_deliver()
        Disco_modular.envioClienteNuevo_Direccion("Av Lope de Vega 345", "Disco CABA Alto Palermo Bulnes 2117")
        Disco_modular.reporteFinal()

    except Exception as e:
        print(e)
        print('Ocurrio un error')
    finally:
        Disco_modular.quit()


if __name__ == '__main__':
    main()
