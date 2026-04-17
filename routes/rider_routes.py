from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models.rider import Rider
from schemas.rider_schema import RiderCreate, RiderResponse

router = APIRouter(
    prefix="/riders",
    tags=["Riders"]
)

@router.post("/", response_model=RiderResponse, status_code=status.HTTP_201_CREATED)
def create_rider(rider: RiderCreate, db: Session = Depends(get_db)):
    new_rider = Rider(**rider.model_dump())
    db.add(new_rider)
    db.commit()
    db.refresh(new_rider)
    return new_rider

@router.get("/", response_model=list[RiderResponse])
def get_all_riders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Rider).offset(skip).limit(limit).all()

@router.get("/{rider_id}", response_model=RiderResponse)
def get_rider_by_id(rider_id: int, db: Session = Depends(get_db)):
    rider = db.query(Rider).filter(Rider.id == rider_id).first()
    if not rider:
        raise HTTPException(status_code=404, detail="Rider tidak ditemukan di Citadel")
    return rider

@router.delete("/{rider_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_rider(rider_id: int, db: Session = Depends(get_db)):
    rider = db.query(Rider).filter(Rider.id == rider_id).first()
    if not rider:
        raise HTTPException(status_code=404, detail="Rider tidak ditemukan")
    db.delete(rider)
    db.commit()
    return {"message": "Data sejarah berhasil dihapus"}