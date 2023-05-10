from fastapi import HTTPException, APIRouter, Body
from typing import List
from core.models.database import db 
from core.schemas.schemes import FaultMsgModel, SelectedParameters


router = APIRouter(
    tags=["read-message"],
    responses={404: {"description": "Not found"}},
)

@router.post(
    "/fault-messages/selected", response_description="Selected all fault messages", response_model=List[FaultMsgModel]
)
async def selected_fault_messages(parameters: SelectedParameters = Body(...)):
    parameters = {k: v for k, v in parameters.dict().items() if v is not None}
    messages = await db["messages"].find(parameters).to_list(1000)
    return messages

@router.get(
    "/fault-messages/", response_description="List all fault messages", response_model=List[FaultMsgModel]
)
async def list_fault_messages():
    messages = await db["messages"].find().to_list(1000)
    return messages

@router.get(
    "/fault-messages/{id}", response_description="Get a single fault message", response_model=FaultMsgModel
)

async def show_fault_messages(id: str):
    if (fault_message := await db["messages"].find_one({"_id": id})) is not None:
        return fault_message

    raise HTTPException(status_code=404, detail=f"Fault message {id} not found")