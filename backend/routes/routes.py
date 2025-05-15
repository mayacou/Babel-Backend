from fastapi import APIRouter, FastAPI
from controllers.text_translation_controller import translate_text
from controllers.file_translation_controller import translate_file

def setup_routes(app: FastAPI):
    router = APIRouter()

    router.add_api_route("/api/translate/text", translate_text, methods=["POST"])
    router.add_api_route("/api/translate/file", translate_file, methods=["POST"])

    app.include_router(router)
