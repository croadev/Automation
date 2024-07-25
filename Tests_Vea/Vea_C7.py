import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Services.FuncionesManager import FuncionesModular
import time


def main():
    Vea_modular = FuncionesModular(
        "https://www.vea.com.ar")
    try:
        print('Cliente Nuevo, Retiro en Tienda, Food')
        Vea_modular.reporteInicial()
        Vea_modular.sucursalClienteNuevo(
            prov="CABA", seller="Vea CABA Araoz 265", direccion_email="pruebaautomatizada@prueba.com")
        Vea_modular.cerrarModal()
        Vea_modular.buscarArticulo("Whisky")
        time.sleep(5)
        Vea_modular.addToCart()
        time.sleep(5)
        Vea_modular.goCart()
        Vea_modular.irACheckout()
        Vea_modular.criterio("Criterio Vea")
        Vea_modular.identificacion(
            "Prueba", "Disco", "12/10/95", "11", "56789912", "33333334")
        Vea_modular.genero(True)
        Vea_modular.aceptar_terminosycondiciones()
        Vea_modular.goto_deliver()
        Vea_modular.envioClienteNuevo_Direccion("Av Lope de Vega 345", "Araoz 265 CABA")
        Vea_modular.reporteFinal()

    except Exception as e:
        print(e)
        print('Ocurrio un error')
    finally:
        Vea_modular.quit()


if __name__ == '__main__':
    main()