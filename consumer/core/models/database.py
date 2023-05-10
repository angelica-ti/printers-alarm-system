import motor.motor_asyncio
from dotenv import load_dotenv
import os

class MongoDataBase:    
    
    @staticmethod
    def create_connection(var_name='MONGO_DB'):
        load_dotenv()
        MONGO_DB = os.getenv(var_name)
        client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DB)
        return client
    

client = MongoDataBase.create_connection()    
db = client.fault_messages