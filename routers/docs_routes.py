# routers/docs_routes.py
from fastapi import APIRouter, UploadFile, File
from controllers import docs_controllers

router = APIRouter(prefix="/dl", tags=["Deep Learning"])

@router.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    return await docs_controllers.handle_prediction(file)