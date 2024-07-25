import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Services.FuncionesManager import FuncionesModular
import time

def main():
    vea_modular = FuncionesModular(
        "https://www.vea.com.ar")
    try:
        print('Cliente Nuevo, Envío a Domicilio, Food')
        vea_modular.reporteInicial()
        vea_modular.direccionNuevaDV1(mail="pruebaautomatizada@prueba.com", direccion="Av Lope de Vega 345")
        vea_modular.nextdir()
        vea_modular.direcconNuevaDV2()
        vea_modular.cerrarModal()
        vea_modular.buscarArticulo("Whisky")
        time.sleep(5)
        vea_modular.addToCart()
        time.sleep(5)
        vea_modular.goCart()
        vea_modular.irACheckout()
        vea_modular.criterio("Criterio Vea")
        vea_modular.identificacion(
            "Pruebaa", "Discooo", "12/10/95", "11", "56789912", "33333334")
        vea_modular.genero(True)
        vea_modular.aceptar_terminosycondiciones()
        #vea_modular.cerrar_politicas()
        vea_modular.goto_deliver()
        vea_modular.envioClienteNuevo()
        vea_modular.reporteFinal()


    except Exception as e:
        print(e)
        print('Ocurrio un error')
    finally:
        vea_modular.quit()


if __name__ == '__main__':
    main()
