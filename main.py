from fastapi import FastAPI
from database import engine, Base
from routes import rider_routes, dragon_routes # Import keduanya

# Membuat tabel secara otomatis
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Valyrian Heritage & Dragon Chronicle",
    description="Sistem arsip sejarah penunggang naga dan naga mereka",
    version="1.0.0"
)

# Daftarkan Router
app.include_router(rider_routes.router)
app.include_router(dragon_routes.router) # Tambahkan baris ini

@app.get("/")
def root():
    return {"message": "Selamat datang di Arsip Citadel. Buka /docs untuk dokumentasi API."}