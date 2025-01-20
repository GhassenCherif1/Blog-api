from fastapi import FastAPI , Depends
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Blog API", version="1.0", description="A simple blog API")
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def read_root():
    return {"message":"Hello World"}