from pydantic import BaseModel, Field
from typing import Optional

class FaultMsgModel(BaseModel):
    id: str = Field(..., alias="_id")
    brand: str = Field(...)
    model: str = Field(...)
    type: str = Field(...)
    category: str = Field(...)
    severity: int = Field(..., gt=0, lt=4)
    description: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "brand": "Epson",
                "model": "L210",
                "type": "laser",
                "category": "drivers",
                "severity": 1,
                "description":"Wrong driver installed!"
            }
        }


class UpdateFaultMsgModel(BaseModel):
    brand: Optional[str]
    model: Optional[str]
    type: Optional[str]
    category: Optional[str]
    severity: Optional[int]
    description: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "brand": "Epson",
                "model": "L210",
                "type": "laser",
                "category": "drivers",
                "severity": 1,
                "description":"Wrong driver installed!"
            }
        }
        
class SelectedParameters(BaseModel):
    brand: Optional[str]
    model: Optional[str]
    type: Optional[str]
    category: Optional[str]
    severity: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "brand": "Epson",
                "model": "L210",
                "type": "laser",
                "category": "drivers",
                "severity": 1
            }
        }