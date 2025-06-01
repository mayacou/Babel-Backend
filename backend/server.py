from fastapi import FastAPI
from routers.translation_router import translation_router
import uvicorn

app = FastAPI()
app.include_router(translation_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)