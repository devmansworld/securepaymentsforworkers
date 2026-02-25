from typing import Any, Dict
import requests

BASE_URL = "http://localhost:3000"

def calcular_beneficio(payload: Dict[str, Any]) -> requests.Response:
    """Envía request POST al endpoint."""
    return requests.post(f"{BASE_URL}/api/v1/beneficios/calcular", json=payload, timeout=5)