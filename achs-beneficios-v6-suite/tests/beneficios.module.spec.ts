import { test, expect } from '@playwright/test';

interface Scenario {
  sbm: number;
  grado: number;
  gran: boolean;
  expectedTipo: string;
}

const boundaryScenarios: Scenario[] = [
  { sbm: 1500000, grado: 14.9999, gran: false, expectedTipo: 'NINGUNO' },
  { sbm: 1500000, grado: 15, gran: false, expectedTipo: 'INDEMNIZACION' },
  { sbm: 1500000, grado: 40, gran: false, expectedTipo: 'PENSION_PARCIAL' },
  { sbm: 1500000, grado: 70, gran: true, expectedTipo: 'PENSION_TOTAL' }
];

test.describe('Beneficios Module Suite', () => {

  for (const scenario of boundaryScenarios) {

    test(`Validate grado ${scenario.grado}`, async ({ request }) => {

      const response = await request.post('/api/v1/beneficios/calcular', {
        data: {
          sbm: scenario.sbm,
          gradoIncapacidad: scenario.grado,
          opciones: { granInvalidez: scenario.gran }
        }
      });

      expect(response.ok()).toBeTruthy();
      const body = await response.json();

      expect(body.tipoBeneficio).toBe(scenario.expectedTipo);

    });

  }

});