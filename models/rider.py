from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Rider(Base):
    __tablename__ = "riders"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    house = Column(String, nullable=False)
    title = Column(String)
    is_active = Column(Boolean, default=True)

    # Relasi ke tabel naga (1 Rider bisa punya banyak Naga)
    dragons = relationship("Dragon", back_populates="rider", cascade="all, delete-orphan")