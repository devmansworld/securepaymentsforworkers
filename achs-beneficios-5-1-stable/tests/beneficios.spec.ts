import { test, expect } from '@playwright/test';

const boundaryCases = [
  { sbm: 1500000, grado: 0, expected: 'NINGUNO' },
  { sbm: 1500000, grado: 14.9999, expected: 'NINGUNO' },
  { sbm: 1500000, grado: 15, expected: 'INDEMNIZACION' },
  { sbm: 1500000, grado: 17.4999, expected: 'INDEMNIZACION' },
  { sbm: 1500000, grado: 17.5, expected: 'INDEMNIZACION' },
  { sbm: 1500000, grado: 39.9999, expected: 'INDEMNIZACION' },
  { sbm: 1500000, grado: 40, expected: 'PENSION_PARCIAL' },
  { sbm: 1500000, grado: 69.9999, expected: 'PENSION_PARCIAL' },
  { sbm: 1500000, grado: 70, expected: 'PENSION_TOTAL' },
  { sbm: 1500000, grado: 100, expected: 'PENSION_TOTAL' },
];

for (const scenario of boundaryCases) {
  test(`Boundary Test - grado ${scenario.grado}`, async ({ request }) => {
    const response = await request.post('/api/v1/beneficios/calcular', {
      data: {
        sbm: scenario.sbm,
        gradoIncapacidad: scenario.grado,
        opciones: { granInvalidez: false }
      }
    });

    expect(response.ok()).toBeTruthy();
    const body = await response.json();
    expect(body.tipoBeneficio).toBe(scenario.expected);
  });
}