from fastapi import HTTPException, Response, status, APIRouter
from fastapi import FastAPI, File, UploadFile
from app.services.post_service import image_post_service

router = APIRouter(
    prefix="/api/posts",
    tags=["Posts"]
)

router = APIRouter()

@router.post("/image_file/")
def create_upload_file(uploaded_file: UploadFile):
    return image_post_service(uploaded_file.file)