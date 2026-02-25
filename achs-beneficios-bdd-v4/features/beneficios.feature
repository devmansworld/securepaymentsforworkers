Feature: Motor de Cálculo ACHS – Cobertura Exhaustiva

  Scenario Outline: Cobertura total de límites y bordes
    Given un SBM de <sbm>
    And un grado <grado>
    And gran invalidez <gran>
    When calculo el beneficio
    Then el tipo debe ser "<tipo>"

    Examples:
      | sbm      | grado     | gran  | tipo              |
      | 1500000  | 0         | false | NINGUNO           |
      | 1500000  | 14.9999   | false | NINGUNO           |
      | 1500000  | 15        | false | INDEMNIZACION     |
      | 1500000  | 17.4999   | false | INDEMNIZACION     |
      | 1500000  | 17.5      | false | INDEMNIZACION     |
      | 1500000  | 19.9999   | false | INDEMNIZACION     |
      | 1500000  | 20        | false | INDEMNIZACION     |
      | 1500000  | 22.4999   | false | INDEMNIZACION     |
      | 1500000  | 22.5      | false | INDEMNIZACION     |
      | 1500000  | 24.9999   | false | INDEMNIZACION     |
      | 1500000  | 25        | false | INDEMNIZACION     |
      | 1500000  | 27.4999   | false | INDEMNIZACION     |
      | 1500000  | 27.5      | false | INDEMNIZACION     |
      | 1500000  | 29.9999   | false | INDEMNIZACION     |
      | 1500000  | 30        | false | INDEMNIZACION     |
      | 1500000  | 32.4999   | false | INDEMNIZACION     |
      | 1500000  | 32.5      | false | INDEMNIZACION     |
      | 1500000  | 34.9999   | false | INDEMNIZACION     |
      | 1500000  | 35        | false | INDEMNIZACION     |
      | 1500000  | 37.4999   | false | INDEMNIZACION     |
      | 1500000  | 37.5      | false | INDEMNIZACION     |
      | 1500000  | 39.9999   | false | INDEMNIZACION     |
      | 1500000  | 40        | false | PENSION_PARCIAL   |
      | 1500000  | 69.9999   | false | PENSION_PARCIAL   |
      | 1500000  | 70        | false | PENSION_TOTAL     |
      | 1500000  | 100       | true  | PENSION_TOTAL     |