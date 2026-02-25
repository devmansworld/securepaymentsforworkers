from decimal import Decimal
from utils.api_client import calcular_beneficio
from utils.expected_calculator import calcular_esperado

def test_pension_parcial_equivalencia():
    payload = {
        "sbm": 1500000,
        "gradoIncapacidad": 45.5,
        "opciones": {"granInvalidez": False}
    }

    response = calcular_beneficio(payload)
    data = response.json()

    esperado = calcular_esperado(
        Decimal("1500000"),
        Decimal("45.5"),
        False
    )

    assert response.status_code == 200
    assert data["tipoBeneficio"] == esperado["tipoBeneficio"]