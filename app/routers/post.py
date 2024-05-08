from fastapi import HTTPException, Response, status, APIRouter
from fastapi import FastAPI, File, UploadFile

router = APIRouter(
    prefix="/api/posts",
    tags=["Posts"]
)

router = APIRouter()

@router.post("/image_file/")
def create_upload_file(file: UploadFile):
    return {"filename": file.filename}