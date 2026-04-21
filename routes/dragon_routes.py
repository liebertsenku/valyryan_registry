from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models.dragon import Dragon
from models.rider import Rider
from models.user import User
from schemas.dragon_schema import DragonCreate, DragonResponse
from auth.security import get_current_user

router = APIRouter(
    prefix="/dragons",
    tags=["Dragons"]
)

# TERPROTEKSI: Hanya bisa diakses dengan JWT
@router.post("/", response_model=DragonResponse, status_code=status.HTTP_201_CREATED)
def create_dragon(
    dragon: DragonCreate, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user) # Injeksi proteksi
):
    db_rider = db.query(Rider).filter(Rider.id == dragon.rider_id).first()
    if not db_rider:
        raise HTTPException(
            status_code=404, 
            detail=f"Rider dengan ID {dragon.rider_id} tidak ditemukan."
        )
    
    new_dragon = Dragon(**dragon.model_dump())
    db.add(new_dragon)
    db.commit()
    db.refresh(new_dragon)
    return new_dragon

# PUBLIK: Siapa saja bisa melihat sejarah naga
@router.get("/", response_model=list[DragonResponse])
def get_all_dragons(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    return db.query(Dragon).offset(skip).limit(limit).all()

# PUBLIK
@router.get("/{dragon_id}", response_model=DragonResponse)
def get_dragon_by_id(dragon_id: int, db: Session = Depends(get_db)):
    dragon = db.query(Dragon).filter(Dragon.id == dragon_id).first()
    if not dragon:
        raise HTTPException(status_code=404, detail="Naga tidak ditemukan di Citadel")
    return dragon

# TERPROTEKSI
@router.put("/{dragon_id}", response_model=DragonResponse)
def update_dragon(
    dragon_id: int, 
    updated_data: DragonCreate, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    dragon_query = db.query(Dragon).filter(Dragon.id == dragon_id)
    db_dragon = dragon_query.first()
    
    if not db_dragon:
        raise HTTPException(status_code=404, detail="Naga tidak ditemukan")
    
    dragon_query.update(updated_data.model_dump(), synchronize_session=False)
    db.commit()
    return dragon_query.first()

# TERPROTEKSI
@router.delete("/{dragon_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_dragon(
    dragon_id: int, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    dragon = db.query(Dragon).filter(Dragon.id == dragon_id).first()
    if not dragon:
        raise HTTPException(status_code=404, detail="Naga tidak ditemukan")
    
    db.delete(dragon)
    db.commit()
    return {"message": "Data naga berhasil dihapus"}