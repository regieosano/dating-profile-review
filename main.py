from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import post
from fastapi import FastAPI

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to Profile Checker"}

@app.get("/favicon.ico")
def favicon():
    return {"message": "Regie's Favicon!"}
  
app.include_router(post.router)
