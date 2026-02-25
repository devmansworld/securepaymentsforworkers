Feature: Motor de Cálculo ACHS

  Scenario Outline: Cobertura completa límites
    Given un SBM de <sbm>
    And un grado <grado>
    And gran invalidez <gran>
    When calculo el beneficio
    Then el tipo debe ser "<tipo>"

    Examples:
      | sbm      | grado  | gran  | tipo              |
      | 1500000  | 14.99  | false | NINGUNO           |
      | 1500000  | 15     | false | INDEMNIZACION     |
      | 1500000  | 17.5   | false | INDEMNIZACION     |
      | 1500000  | 39.99  | false | INDEMNIZACION     |
      | 1500000  | 40     | false | PENSION_PARCIAL   |
      | 1500000  | 69.99  | false | PENSION_PARCIAL   |
      | 1500000  | 70     | false | PENSION_TOTAL     |
      | 1500000  | 75     | true  | PENSION_TOTAL     |