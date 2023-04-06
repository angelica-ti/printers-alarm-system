from fastapi import APIRouter, Body, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.schemes import FaultMsgModel
from app.database import db 

router = APIRouter(
    tags=["create-message"],
    responses={404: {"description": "Not found"}},
)

@router.post("/fault-messages/", response_description="Add new fault message", response_model=FaultMsgModel)
async def create_fault_message(fault_message: FaultMsgModel = Body(...)):
    fault_message = jsonable_encoder(fault_message)
    new_fault_message = await db["messages"].insert_one(fault_message)
    created_fault_message = await db["messages"].find_one({"_id": new_fault_message.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_fault_message)

