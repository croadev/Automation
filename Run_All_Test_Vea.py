import pytest
from Tests_Vea import Vea_C1, Vea_C2, Vea_C3, Vea_C4, Vea_C5, Vea_C6, Vea_C7, Vea_C8, Vea_C9


@pytest.mark.VC1
def test_cliente_recurrente_envio_a_domicilio_food_vea():
    print("Ejecutando Vea_C1")
    Vea_C1.main()


@pytest.mark.VC2
def test_cliente_recurrente_retiro_en_tienda_food_vea():
    print("Ejecutando Vea_C2")
    Vea_C2.main()


@pytest.mark.VC3
def test_cliente_recurrente_envio_a_domicilio_electro_vea():
    print("Ejecutando Vea_C3")
    Vea_C3.main()


@pytest.mark.VC4
def test_cliente_recurrente_retiro_en_tienda_electro_vea():
    print("Ejecutando Vea_C4")
    Vea_C4.main()


@pytest.mark.VC5
def test_cliente_nuevo_Envio_a_domicilio_food__vea():
    print("Ejecutando Vea_C5")
    Vea_C5.main()


@pytest.mark.VC6
def test_cliente_nuevo_envio_a_domicilio_electro_vea():
    print("Ejecutando Vea_C6")
    Vea_C6.main()


@pytest.mark.VC7
def test_cliente_nuevo_retiro_en_tienda_food_vea():
    print("Ejecutando Vea_C7")
    Vea_C7.main()


@pytest.mark.VC8
def test_cliente_nuevo_retiro_en_tienda_electro_vea():
    print("Ejecutando Vea_C8")
    Vea_C8.main()


@pytest.mark.VC9
def test_cliente_recurrente_dirección_fuera_de_cobertura_vea():
    print("Ejecutando Vea_C9")
    Vea_C9.main()
