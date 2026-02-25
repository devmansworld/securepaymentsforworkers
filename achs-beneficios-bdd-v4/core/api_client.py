from typing import Dict, Any
import requests
import os

BASE_URL = os.getenv("BASE_URL", "http://localhost:3000")

class BeneficiosAPI:

    def calcular(self, payload: Dict[str, Any]) -> requests.Response:
        return requests.post(
            f"{BASE_URL}/api/v1/beneficios/calcular",
            json=payload,
            timeout=5
        )