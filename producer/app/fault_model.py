from pydantic import BaseModel

class FaultMessage(BaseModel):
    brand: str
    model: str
    type: str
    category: str
    severity: int
    description: str