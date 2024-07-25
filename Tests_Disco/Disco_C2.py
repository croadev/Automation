import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Services.FuncionesManager import FuncionesModular
import time


def main():
    disco_modular = FuncionesModular(
        "https://www.disco.com.ar")
    try:
        print('Cliente recurrente, Retiro en Tienda, Food')
        disco_modular.reporteInicial()
        sucursal = disco_modular.sucursal(
            prov="CABA", seller="Disco Alto Palermo", direccion_email="carlos.roa@cencosud.com.ar")
        disco_modular.cerrarModal()
        disco_modular.buscarArticulo("Whisky")
        time.sleep(5)
        disco_modular.addToCart()
        time.sleep(5)
        disco_modular.goCart()
        disco_modular.irACheckout()
        disco_modular.criterio("Criterio Disco")
        time.sleep(2)
        disco_modular.envioRecurrenteTienda()
        disco_modular.reporteFinal()

    except Exception as e:
        print(e)
        print('Ocurrio un error')
    finally:
        disco_modular.quit()


if __name__ == '__main__':
    main()
