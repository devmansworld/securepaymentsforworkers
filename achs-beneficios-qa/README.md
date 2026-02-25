# ACHS – Evaluación QA Automation

## Contexto

Este repositorio contiene el diseño de pruebas y automatización
para el endpoint:

POST /api/v1/beneficios/calcular

La API fue entregada con posibles defectos intencionales.

Objetivos:

- Validar reglas de negocio según especificación del PO
- Detectar errores en límites
- Validar precisión financiera
- Validar manejo de errores
- Verificar consistencia del contrato JSON

## Stack Tecnológico

- Python 3.11+
- pytest
- requests
- decimal.Decimal
- flake8
- mypy

## Ejecución

pip install -r requirements.txt
pytest

## Análisis Estático

flake8 .
mypy .