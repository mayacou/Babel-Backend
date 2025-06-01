from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import translation_router

app = FastAPI(title="Babel Translation API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(translation_router.router, prefix="/api/v1") 