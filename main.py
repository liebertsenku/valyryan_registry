from fastapi import FastAPI
from database import engine, Base
from routes import rider_routes, dragon_routes, auth_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Valyrian Heritage & Dragon Chronicle",
    description="Sistem arsip sejarah penunggang naga dan naga mereka",
    version="1.0.0"
)

# Mendaftarkan Router
app.include_router(auth_routes.router)
app.include_router(rider_routes.router)
app.include_router(dragon_routes.router)

@app.get("/")
def root():
    return {"message": "Selamat datang di Arsip Citadel. Buka /docs untuk dokumentasi API."}