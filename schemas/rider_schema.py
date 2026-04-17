from pydantic import BaseModel, Field
from typing import List, Optional
from schemas.dragon_schema import DragonResponse

class RiderBase(BaseModel):
    name: str = Field(..., min_length=2)
    house: str
    title: Optional[str] = None
    is_active: bool = True

class RiderCreate(RiderBase):
    pass

class RiderResponse(RiderBase):
    id: int
    # Menampilkan daftar naga yang dimiliki rider ini
    dragons: List[DragonResponse] = []

    class Config:
        from_attributes = True