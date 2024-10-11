from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    first_name: str
    phone: str
    plasticidad: str
    permeabilidad: str
    densidad: str
    porosidad: str
    oleosidad: str
    hebra: str
    textura: str
