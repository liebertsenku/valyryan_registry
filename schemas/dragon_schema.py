from pydantic import BaseModel, Field

class DragonBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    color: str
    size_category: str = Field(..., description="Kategori ukuran: Small, Medium, Colossal")
    status: str = "Alive"

class DragonCreate(DragonBase):
    rider_id: int

class DragonResponse(DragonBase):
    id: int
    rider_id: int

    class Config:
        from_attributes = True # Wajib agar Pydantic bisa membaca model SQLAlchemy