from abc import ABC, abstractmethod
from typing import List
from lib.parsers.parser import Parser
from types_.category_id import CategoryId


class IdParser(Parser, ABC):
    @abstractmethod
    async def parse(self, cat_id: CategoryId):
        """
        parses inns for one organization
        """
        pass

    async def parse_many(self, cat_ids: List[CategoryId]):
        """
        parses inns for many organizations
        """
        return [await self.parse(cat_id) for cat_id in cat_ids]
