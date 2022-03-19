import asyncio
from lib.db import get_suppliers, update_contacts
from lib.parse_contacts import parse_contacts

async def update_all_contacts():
    suppliers = await get_suppliers()
    async for (inn, contacts) in parse_contacts([supplier.inn for supplier in suppliers]):
        await update_contacts(inn, contacts)
        print(contacts, ' for ', inn)
        await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(update_all_contacts())