import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Services.FuncionesManager import FuncionesModular
import time

def main():
    disco_modular = FuncionesModular(
        "https://www.disco.com.ar"
    )
    try:
        print('Cliente recurrente, Direccion Fuera de Cobertura')
        disco_modular.reporteInicial()
        disco_modular.ModalFueraDeCobertura("carlos.roa@cencosud.com.ar", "San Martin 500 - Santa Rosa La Pampa")
        disco_modular.cerrarModal()
        time.sleep(2)
        disco_modular.buscarArticulo("Heladeras")
        time.sleep(5)
        disco_modular.addToCart()
        time.sleep(5)
        disco_modular.goCart()
        disco_modular.irACheckout()
        disco_modular.criterio("Criterio Disco")
        disco_modular.envioRecurrenteDomicilio()
        disco_modular.reporteFinal()

    except Exception as e:
        print(e)
        print('Ocurrio un error')
    finally:
        disco_modular.quit()

if __name__ == '__main__':
    main()