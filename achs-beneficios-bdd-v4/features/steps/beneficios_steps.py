from behave import given, when, then
from decimal import Decimal
from core.api_client import BeneficiosAPI
from core.expected_engine import ExpectedCalculator
from core.validator import BeneficioResponse

api=BeneficiosAPI()

@given("un SBM de {sbm}")
def step_sbm(context,sbm):
    context.sbm=Decimal(sbm)

@given("un grado {grado}")
def step_grado(context,grado):
    context.grado=Decimal(grado)

@given("gran invalidez {gran}")
def step_gran(context,gran):
    context.gran=gran.lower()=="true"

@when("calculo el beneficio")
def step_call(context):
    payload={
        "sbm":float(context.sbm),
        "gradoIncapacidad":float(context.grado),
        "opciones":{"granInvalidez":context.gran}
    }
    context.response=api.calcular(payload)
    context.data=context.response.json()

@then('el tipo debe ser "{tipo}"')
def step_validate(context,tipo):
    esperado=ExpectedCalculator.calculate(context.sbm,context.grado,context.gran)
    validado=BeneficioResponse(**context.data)
    assert validado.tipoBeneficio==tipo
    assert Decimal(str(validado.monto))==esperado["monto"]