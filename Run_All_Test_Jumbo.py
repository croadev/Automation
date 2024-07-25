import pytest
from Tests_Jumbo import Jumbo_C1, Jumbo_C2, Jumbo_C3, Jumbo_C4, Jumbo_C5, Jumbo_C6, Jumbo_C7, Jumbo_C8, Jumbo_C9


@pytest.mark.JC1
def test_cliente_recurrente_envio_a_domicilio_food_jumbo():
    print("Ejecutando Jumbo_C1")
    Jumbo_C1.main()


@pytest.mark.JC2
def test_cliente_recurrente_retiro_en_tienda_food_jumbo():
    print("Ejecutando Jumbo_C2")
    Jumbo_C2.main()


@pytest.mark.JC3
def test_cliente_recurrente_envio_a_domicilio_electro_jumbo():
    print("Ejecutando Jumbo_C3")
    Jumbo_C3.main()


@pytest.mark.JC4
def test_cliente_recurrente_retiro_en_tienda_electro_jumbo():
    print("Ejecutando Jumbo_C4")
    Jumbo_C4.main()


@pytest.mark.JC5
def test_cliente_nuevo_Envio_a_domicilio_food_jumbo():
    print("Ejecutando Jumbo_C5")
    Jumbo_C5.main()


@pytest.mark.JC6
def test_cliente_nuevo_envio_a_domicilio_electro_jumbo():
    print("Ejecutando Jumbo_C6")
    Jumbo_C6.main()


@pytest.mark.JC7
def test_cliente_nuevo_retiro_en_tienda_food_jumbo():
    print("Ejecutando Jumbo_C7")
    Jumbo_C7.main()


@pytest.mark.JC8
def test_cliente_nuevo_retiro_en_tienda_electro_jumbo():
    print("Ejecutando Jumbo_C8")
    Jumbo_C8.main()


@pytest.mark.JC9
def test_cliente_recurrente_dirección_fuera_de_cobertura_jumbo():
    print("Ejecutando Jumbo_C9")
    Jumbo_C9.main()
