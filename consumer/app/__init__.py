from fastapi import FastAPI
from app.routes import create_msg, read_msg, update_msg, delete_msg
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(create_msg.router)
app.include_router(read_msg.router)
app.include_router(update_msg.router)
app.include_router(delete_msg.router)