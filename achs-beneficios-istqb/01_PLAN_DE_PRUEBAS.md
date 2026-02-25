# Plan de Pruebas – Motor de Cálculo Prestaciones ACHS

## 1. Objetivo

Validar funcionalmente el endpoint:
POST /api/v1/beneficios/calcular

Asegurar cumplimiento de reglas de negocio,
precisión monetaria y manejo adecuado de errores.

---

## 2. Alcance

Incluye:
- Validación de reglas de negocio
- Análisis de valores límite
- Validación de estructura JSON
- Pruebas negativas
- Validación de suplemento granInvalidez

Excluye:
- Seguridad
- Performance
- Infraestructura

---

## 3. Enfoque ISTQB

Técnicas aplicadas:
- Partición de equivalencia
- Análisis de valores límite
- Tabla de decisión
- Pruebas negativas
- Pruebas combinatorias