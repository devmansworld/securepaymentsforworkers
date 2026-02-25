Feature: Cálculo beneficios

Scenario: Grado 15 exacto
  Given SBM 1500000
  And grado 15
  When calcular
  Then tipo INDEMNIZACION