import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Services.FuncionesManager import FuncionesModular
import time

def main():
    vea_modular = FuncionesModular(
        "https://www.vea.com.ar")
    try:
        print('Cliente recurrente, Envio a domicilio, Food')
        vea_modular.reporteInicial()
        vea_modular.direccion1(mail="carlos.roa@cencosud.com.ar")
        vea_modular.cerrarModal()
        vea_modular.buscarArticulo("Whisky")
        time.sleep(5)
        vea_modular.addToCart()
        time.sleep(5)
        vea_modular.goCart()
        vea_modular.irACheckout()
        vea_modular.criterio("Criterio Vea")
        vea_modular.envioRecurrenteDomicilio()
        vea_modular.reporteFinal()

    except Exception as e:
        print(e)
        print('Ocurrio un error')
    finally:
        vea_modular.quit()


if __name__ == '__main__':
    main()
