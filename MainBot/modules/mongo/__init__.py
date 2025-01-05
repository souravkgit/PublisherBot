from MainBot import DB_URI
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient(DB_URI)
db = client.PublisherBot
