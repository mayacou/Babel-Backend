from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.routes import setup_routes
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

setup_routes(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)
