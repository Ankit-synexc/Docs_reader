# controllers/docs_controllers.py
from fastapi import UploadFile, HTTPException
from services import docs_services

async def handle_prediction(file: UploadFile):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file type")

    image_bytes = await file.read()
    prediction = docs_services.predict(image_bytes)

    return {
        "filename": file.filename,
        "prediction": prediction
    }