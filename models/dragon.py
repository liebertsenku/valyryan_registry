from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Dragon(Base):
    __tablename__ = "dragons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    color = Column(String)
    size_category = Column(String) # Small, Medium, Colossal
    status = Column(String, default="Alive")
    
    # Foreign Key mengarah ke id di tabel riders
    rider_id = Column(Integer, ForeignKey("riders.id"))

    # Relasi balik ke Rider
    rider = relationship("Rider", back_populates="dragons")