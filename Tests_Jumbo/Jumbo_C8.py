import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Services.FuncionesManager import FuncionesModular
import time


def main():
    Jumbo_modular = FuncionesModular(
        "https://www.jumbo.com.ar")
    try:
        print('Cliente Nuevo, Retiro en Tienda, Electro')
        Jumbo_modular.reporteInicial()
        Jumbo_modular.sucursalClienteNuevo(
            prov="Buenos Aires", seller="Jumbo Martinez", direccion_email="pruebaautomatizada@prueba.com")
        try:
            Jumbo_modular.cerrarModal()
        except:
            time.sleep(3)
        Jumbo_modular.buscarArticulo("Heladeras")
        time.sleep(5)
        Jumbo_modular.addToCart()
        time.sleep(5)
        Jumbo_modular.goCart()
        Jumbo_modular.irACheckout()
        try:
            Jumbo_modular.cerrarModal()
        except:
            time.sleep(2)
        Jumbo_modular.criterio("Criterio Jumbo")
        Jumbo_modular.identificacion(
            "Prueba", "Disco", "12/10/95", "11", "56789912", "33333334")
        Jumbo_modular.genero(True)
        Jumbo_modular.aceptar_terminosycondiciones()
        #Jumbo_modular.cerrar_politicas()
        Jumbo_modular.goto_deliver()
        Jumbo_modular.envioClienteNuevo_DireccionElectro("Av Lope de Vega 345")
        Jumbo_modular.reporteFinal()

    except Exception as e:
        print(e)
        print('Ocurrio un error')
    finally:
        Jumbo_modular.quit()


if __name__ == '__main__':
    main()
