import shutil
from pathlib import Path

from fastapi import APIRouter, File, UploadFile

from app.schemas.upload import UploadResponse
from app.services.ingestion_service import IngestionService

router = APIRouter()

UPLOAD_DIR = Path("data")

UPLOAD_DIR.mkdir(exist_ok=True)

@router.post("/upload",response_model=UploadResponse)
async def upload_document(file: UploadFile = File(...)):
    destination = UPLOAD_DIR/file.filename
    with destination.open("wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    IngestionService().ingest(str(destination))

    return UploadResponse(success=True,filename= file.filename, message="Document uploaded and indexed successfully")