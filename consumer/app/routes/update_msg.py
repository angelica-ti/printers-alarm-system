from fastapi import Body, HTTPException, APIRouter
from core.schemas.schemes import FaultMsgModel, UpdateFaultMsgModel
from core.models.database import db 

router = APIRouter(
    tags=["update-message"],
    responses={404: {"description": "Not found"}},
)

@router.put("/fault-messages/{id}", response_description="Update a fault message", response_model=FaultMsgModel)
async def update_fault_message(id: str, fault_message: UpdateFaultMsgModel = Body(...)):
    fault_message = {k: v for k, v in fault_message.dict().items() if v is not None}

    if len(fault_message) >= 1:
        update_result = await db["messages"].update_one({"_id": id}, {"$set": fault_message})

        if update_result.modified_count == 1:
            if (
                updated_fault_message := await db["messages"].find_one({"_id": id})
            ) is not None:
                return updated_fault_message

    if (existing_fault_message := await db["messages"].find_one({"_id": id})) is not None:
        return existing_fault_message

    raise HTTPException(status_code=404, detail=f"Fault message {id} not found")

