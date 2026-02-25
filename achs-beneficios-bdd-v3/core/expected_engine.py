from decimal import Decimal, ROUND_HALF_EVEN
from typing import Dict

class ExpectedCalculator:

    @staticmethod
    def _round(value: Decimal) -> Decimal:
        return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_EVEN)

    @staticmethod
    def calculate(sbm: Decimal, grado: Decimal, gran: bool=False) -> Dict[str, object]:

        if grado < Decimal("0") or grado > Decimal("100"):
            raise ValueError("Grado fuera de rango")

        if sbm <= Decimal("0"):
            raise ValueError("SBM inválido")

        if grado < Decimal("15"):
            return {"tipoBeneficio":"NINGUNO","monto":Decimal("0.00"),"periodicidad":None}

        if grado < Decimal("40"):
            tabla=[
                (Decimal("17.5"),Decimal("1.5")),
                (Decimal("20.0"),Decimal("3.0")),
                (Decimal("22.5"),Decimal("4.5")),
                (Decimal("25.0"),Decimal("6.5")),
                (Decimal("27.5"),Decimal("7.5")),
                (Decimal("30.0"),Decimal("9.0")),
                (Decimal("32.5"),Decimal("10.5")),
                (Decimal("35.0"),Decimal("12.0")),
                (Decimal("37.5"),Decimal("13.5")),
            ]
            factor=Decimal("15.0")
            for limite,valor in tabla:
                if grado < limite:
                    factor=valor
                    break
            return {
                "tipoBeneficio":"INDEMNIZACION",
                "monto":ExpectedCalculator._round(sbm*factor),
                "periodicidad":"UNICO"
            }

        if grado < Decimal("70"):
            monto=sbm*Decimal("0.30")
            if gran:
                monto+=sbm*Decimal("0.30")
            return {
                "tipoBeneficio":"PENSION_PARCIAL",
                "monto":ExpectedCalculator._round(monto),
                "periodicidad":"MENSUAL"
            }

        monto=sbm*Decimal("0.70")
        if gran:
            monto+=sbm*Decimal("0.30")
        return {
            "tipoBeneficio":"PENSION_TOTAL",
            "monto":ExpectedCalculator._round(monto),
            "periodicidad":"MENSUAL"
        }