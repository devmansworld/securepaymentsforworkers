from utils.api_client import calcular_beneficio

def test_grado_negativo():
    r=calcular_beneficio({"sbm":1500000,"gradoIncapacidad":-1})
    assert r.status_code==400

def test_sbm_negativo():
    r=calcular_beneficio({"sbm":-100,"gradoIncapacidad":50})
    assert r.status_code==400