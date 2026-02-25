from typing import Any, Dict
import requests

BASE_URL: str = "http://localhost:3000"

def calcular_beneficio(payload: Dict[str, Any]) -> requests.Response:
    '''
    Envía la solicitud POST al endpoint de cálculo.
    '''
    url = f"{BASE_URL}/api/v1/beneficios/calcular"
    response = requests.post(url, json=payload, timeout=5)
    return response