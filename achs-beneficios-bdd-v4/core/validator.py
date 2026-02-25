from pydantic import BaseModel, Field

class BeneficioResponse(BaseModel):
    tipoBeneficio: str
    monto: float | int
    periodicidad: str | None

class BeneficioRequest(BaseModel):
    sbm: float = Field(gt=0)
    gradoIncapacidad: float = Field(ge=0, le=100)