import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Services.FuncionesManager import FuncionesModular
import time

def main():
    jumbo_modular = FuncionesModular(
        "https://www.jumbo.com.ar"
    )
    try:
        print('Cliente Nuevo, Direccion Fuera de Cobertura')
        jumbo_modular.reporteInicial()
        jumbo_modular.ModalFueraDeCobertura("pruebaAutomatizada@gmail.com", "San Martin 500 - Santa Rosa La Pampa")
        jumbo_modular.cerrarModal()
        time.sleep(2)
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