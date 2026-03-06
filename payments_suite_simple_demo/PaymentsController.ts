
// app/Controllers/Http/PaymentsController.ts
// Simple endpoint based on the original idea

export default class PaymentsController {

  public async calcular({ request }) {

    const { salary, disability } = request.body()

    if (disability < 15) {
      return { benefit: "NONE", amount: 0 }
    }

    if (disability < 40) {
      return { benefit: "INDEMNIZATION", amount: salary * 1.5 }
    }

    if (disability < 70) {
      return { benefit: "PARTIAL_PENSION", amount: salary * 0.30 }
    }

    return { benefit: "TOTAL_PENSION", amount: salary * 0.70 }
  }

}
