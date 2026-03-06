
// tests/payments.spec.ts

import { test, expect } from '@playwright/test'

test('calculate indemnization', async ({ request }) => {

  const response = await request.post('http://127.0.0.1:3333/payments/calcular', {
    data: {
      salary: 1000000,
      disability: 20
    }
  })

  const body = await response.json()

  expect(body.benefit).toBe('INDEMNIZATION')

})
