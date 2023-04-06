from fastapi import APIRouter
from app.fault_model import FaultMessage
# from datetime import datetime
from app.emit_alarm import Publisher
import json

router = APIRouter(
    tags=["send-message"],
    responses={404: {"description": "Not found"}},
)

publisher = Publisher()
@router.post("/send-message")
async def post_message(faultMessage: FaultMessage):
    # dt = datetime.now()
    
    fault_detection = { 
        # "date":dt.strftime("%d/%m/%Y"),
        # "hour":dt.strftime("%H:%M:%S"), 
        "brand": faultMessage.brand,   
        "model": faultMessage.model,
        "type": faultMessage.type,  
        "category": faultMessage.category, 
        "severity": faultMessage.severity,
        "description": faultMessage.description     
    } 

    queue = f'{faultMessage.brand}.{faultMessage.model}.{faultMessage.type}.{faultMessage.category}.{faultMessage.severity}'
    message = json.dumps(fault_detection)
    publisher.publish(queue, message)
    return {"confirmation":"Fault Message Sent!"}