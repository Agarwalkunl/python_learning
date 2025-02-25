import motor.motor_asyncio
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGODB_URL")
DB_NAME = os.getenv("DB_NAME") 

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)

try:
    print("Connection to MongoDB successful!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

database = client[DB_NAME]

def get_database():
    return database
