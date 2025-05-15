from fastapi import FastAPI
from routes.routes import setup_routes
import uvicorn

# Added ../documentParsing to the Python import path so it can be used anywhere in backend
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "documentParsing")))

# # Add ../useModels to import path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "useModels")))

app = FastAPI()
setup_routes(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)