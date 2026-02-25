from utils.api_client import calcular_beneficio

def test_boundary_14_99():
    r=calcular_beneficio({"sbm":1500000,"gradoIncapacidad":14.99,"opciones":{}})
    assert r.json()["tipoBeneficio"]=="NINGUNO"

def test_boundary_40():
    r=calcular_beneficio({"sbm":1500000,"gradoIncapacidad":40,"opciones":{}})
    assert r.json()["tipoBeneficio"]=="PENSION_PARCIAL"

def test_boundary_70():
    r=calcular_beneficio({"sbm":1500000,"gradoIncapacidad":70,"opciones":{}})
    assert r.json()["tipoBeneficio"]=="PENSION_TOTAL"