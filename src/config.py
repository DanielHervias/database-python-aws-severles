import motor.motor_asyncio
import os
password = os.getenv("MONGODB_PASSWORD")

mongo_url = f"mongodb+srv://daniel:{password}@chatbot-ws.udglcx0.mongodb.net/?retryWrites=true&w=majority"

client = motor.motor_asyncio.AsyncIOMotorClient(mongo_url)

# connect to database name
database = client["chatbot1"]
