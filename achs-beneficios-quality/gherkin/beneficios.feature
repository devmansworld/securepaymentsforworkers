Feature: Cálculo de Prestaciones ACHS

  Scenario: Sin beneficio cuando grado es menor a 15
    Given un SBM de 1500000
    And un grado de incapacidad de 10
    When se calcula el beneficio
    Then el tipo de beneficio debe ser "NINGUNO"
    And el monto debe ser 0

  Scenario: Indemnización global en tramo 15-17.5
    Given un SBM de 1500000
    And un grado de incapacidad de 16
    When se calcula el beneficio
    Then el tipo de beneficio debe ser "INDEMNIZACION"

  Scenario: Pensión parcial entre 40 y 70
    Given un SBM de 1500000
    And un grado de incapacidad de 45
    When se calcula el beneficio
    Then el tipo de beneficio debe ser "PENSION_PARCIAL"

  Scenario: Pensión total mayor o igual a 70
    Given un SBM de 1500000
    And un grado de incapacidad de 75
    When se calcula el beneficio
    Then el tipo de beneficio debe ser "PENSION_TOTAL"

  Scenario: Suplemento por gran invalidez
    Given un SBM de 1500000
    And un grado de incapacidad de 75
    And gran invalidez es verdadero
    When se calcula el beneficio
    Then el monto debe incluir 30% adicional del SBM

  Scenario: Grado inválido negativo
    Given un SBM de 1500000
    And un grado de incapacidad de -5
    When se calcula el beneficio
    Then debe retornar error 400

  Scenario: SBM inválido negativo
    Given un SBM de -100
    And un grado de incapacidad de 50
    When se calcula el beneficio
    Then debe retornar error 400

  Scenario: Límite exacto 15%
    Given un SBM de 1500000
    And un grado de incapacidad de 15
    When se calcula el beneficio
    Then el tipo de beneficio debe ser "INDEMNIZACION"

  Scenario: Límite exacto 40%
    Given un SBM de 1500000
    And un grado de incapacidad de 40
    When se calcula el beneficio
    Then el tipo de beneficio debe ser "PENSION_PARCIAL"

  Scenario: Límite exacto 70%
    Given un SBM de 1500000
    And un grado de incapacidad de 70
    When se calcula el beneficio
    Then el tipo de beneficio debe ser "PENSION_TOTAL"