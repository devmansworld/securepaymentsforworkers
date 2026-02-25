# Decisiones Técnicas

## Observaciones sobre la API

Se detectan los siguientes riesgos:

- Uso de floating point en JavaScript (riesgo financiero)
- Falta de validación de valores negativos
- Ambigüedad en límites (17.5%, 40%, 70%)
- Aplicación parcial del suplemento granInvalidez
- No definición de redondeo

## Estrategia

Se utiliza Python + Decimal para validar cálculos esperados
con precisión financiera.

Técnicas aplicadas:

- Partición de equivalencia
- Análisis de valores límite
- Pruebas negativas
- Tabla de decisión