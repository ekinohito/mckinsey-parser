from asyncio import sleep
from lib.parsers.id_parsers.id_parser import IdParser
from types_.category_id import CategoryId


class MockIdParser(IdParser):
    async def parse(self, cat_id: CategoryId):
        await sleep(1)
        return [
            5247004695,
            3435000467,
            6320002223,
            7414001428,
            5406981240,
        ]
