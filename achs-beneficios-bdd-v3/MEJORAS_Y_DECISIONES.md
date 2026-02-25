# Mejoras y Decisiones Técnicas – Versión BDD v3

## Alineación ISTQB
- Particiones de equivalencia
- Análisis de valores límite (14.99, 15, 17.5, 39.99, 40, 69.99, 70)
- Tabla de decisión completa (10 tramos)
- Pruebas negativas (grado < 0, grado > 100, SBM <= 0)
- Combinación con gran invalidez

## Arquitectura
Separación de responsabilidades:
- api_client → consumo HTTP
- expected_engine → motor independiente de verdad
- validator → validación estructural
- features → BDD legible por negocio

## Precisión Financiera
Uso de Decimal + ROUND_HALF_EVEN para evitar IEEE 754.

## Expansión Futura
- CI/CD
- Property-based testing
- Performance testing
- Versionado de contratos