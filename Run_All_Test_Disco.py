import pytest
from Tests_Disco import Disco_C1, Disco_C4, Disco_C3, Disco_C2, Disco_C5, Disco_C6, Disco_C7, Disco_C8, Disco_C9


@pytest.mark.DC1
def test_cliente_recurrente_envio_a_domicilio_food_disco():
    print("Ejecutando Disco_C1")
    Disco_C1.main()


@pytest.mark.DC2
def test_cliente_recurrente_retiro_en_tienda_food_disco():
    print("Ejecutando Disco_C1")
    Disco_C2.main()


@pytest.mark.DC3
def test_cliente_recurrente_envío_a_domicilio_electro_disco():
    print("Ejecutando Disco_C2")
    Disco_C3.main()


@pytest.mark.DC4
def test_cliente_recurrente_retiro_en_tienda_electro_disco():
    print("Ejecutando Disco_C3")
    Disco_C4.main()


@pytest.mark.DC5
def test_cliente_nuevo_envio_a_domicilio_food_disco():
    print("Ejecutando Disco_C5")
    Disco_C5.main()


@pytest.mark.DC6
def test_cliente_nuevo_Envio_a_domicilio_electro_disco():
    print("Ejecutando Disco_C6")
    Disco_C6.main()


@pytest.mark.DC7
def test__cliente_nuevo_retiro_en_tienda_food_disco():
    print("Ejecutando Disco_C7")
    Disco_C7.main()


@pytest.mark.DC8
def test_cliente_nuevo_retiro_en_tienda_electro_disco():
    print("Ejecutando Disco_C8")
    Disco_C8.main()


@pytest.mark.DC9
def test_cliente_recurrente_dirección_fuera_de_cobertura_diso():
    print("Ejecutando Disco_C9")
    Disco_C9.main()

