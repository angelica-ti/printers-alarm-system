from fastapi import HTTPException, status, APIRouter
from fastapi.responses import Response
from app.database import db 

router = APIRouter(
    tags=["delete-message"],
    responses={404: {"description": "Not found"}},
)

@router.delete("/fault-messages/{id}", response_description="Delete a fault message")
async def delete_fault_message(id: str):
    delete_result = await db["messages"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Fault message {id} not found")