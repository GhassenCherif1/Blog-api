from fastapi import FastAPI , Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine , text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker , Session
from .routers import posts , users , auth
from . import models
from .database import engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="Blog API", version="1.0", description="A simple blog API")
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
@app.get("/")
def read_root():
    return {"message":"Hello World"}