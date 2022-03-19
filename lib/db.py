import imp
import os
from typing import Dict, List
from types_.supplier import Supplier
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
from types_.contacts import Contacts

from types_.inn import Inn

load_dotenv()
mongodb_uri = os.environ.get("MONGODB_URI")
assert mongodb_uri is not None
client = AsyncIOMotorClient(mongodb_uri, serverSelectionTimeoutMS=5000)
db = client['5deneg']
collection_id = "test"
collection = db[collection_id]


async def update_contacts(inn: Inn, contacts: Contacts):
    return await collection.update_one({"inn": inn}, {"$set": {"contacts": contacts.dict(exclude_none=True)}})

async def get_suppliers() -> List[Supplier]:
    return [Supplier(**entry) for entry in await collection.find().to_list(None)]

async def update_supplier(inn: Inn, data: Dict):
    return await collection.update_one({"inn": inn}, {"$set": data}, upsert=True)
