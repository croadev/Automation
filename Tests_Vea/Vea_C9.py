import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Services.FuncionesManager import FuncionesModular
import time

def main():
    vea_modular = FuncionesModular(
        "https://www.vea.com.ar"
    )
    try:
        print('Cliente recurrente, Direccion Fuera de Cobertura')
        vea_modular.reporteInicial()
        vea_modular.ModalFueraDeCobertura("carlos.roa@cencosud.com.ar", "San Martin 500 - Santa Rosa La Pampa")
        vea_modular.cerrarModal()
        time.sleep(2)
        vea_modular.buscarArticulo("Heladeras")
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