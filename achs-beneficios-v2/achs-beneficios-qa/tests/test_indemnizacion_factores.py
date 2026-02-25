import pytest
from decimal import Decimal
from utils.api_client import calcular_beneficio

@pytest.mark.parametrize("grado,factor",[
    (15.0,1.5),(16.0,1.5),
    (17.5,3.0),(18.0,3.0),
    (20.0,4.5),(21.0,4.5),
    (22.5,6.5),(23.0,6.5),
    (25.0,7.5),(26.0,7.5),
    (27.5,9.0),(28.0,9.0),
    (30.0,10.5),(31.0,10.5),
    (32.5,12.0),(33.0,12.0),
    (35.0,13.5),(36.0,13.5),
    (37.5,15.0),(38.0,15.0),
])
def test_tabla_factores(grado,factor):
    sbm=1500000
    payload={"sbm":sbm,"gradoIncapacidad":grado,"opciones":{"granInvalidez":False}}
    r=calcular_beneficio(payload)
    assert r.status_code==200
    assert Decimal(str(r.json()["monto"]))==Decimal(str(sbm))*Decimal(str(factor))