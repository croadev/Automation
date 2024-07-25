import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Services.FuncionesManager import FuncionesModular
import time


def main():
    jumbo_modular = FuncionesModular(
        "https://www.jumbo.com.ar")
    try:
        print('Cliente recurrente, Retiro en Tienda, Electro')
        jumbo_modular.reporteInicial()
        sucursal = jumbo_modular.sucursal(
            prov="Buenos Aires", seller="Jumbo Martinez", direccion_email="carlos.roa@cencosud.com.ar")
        #jumbo_modular.cerrarModal()
        jumbo_modular.buscarArticulo("Heladeras")
        time.sleep(5)
        jumbo_modular.addToCart()
        time.sleep(5)
        jumbo_modular.goCart()
        jumbo_modular.irACheckout()
        jumbo_modular.criterio("Criterio Jumbo")
        jumbo_modular.envioRecurrenteTiendaElectro()
        jumbo_modular.reporteFinal()

    except Exception as e:
        print(e)
        print('Ocurrio un error')
    finally:
        jumbo_modular.quit()


if __name__ == '__main__':
    main()