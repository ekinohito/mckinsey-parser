from typing import Dict, List
from lib.parsers.parser import Parser
from types_.inn import Inn


class DataParser(Parser):
    key_name = None
    """
    name for a key in final storage
    """

    async def parse(self, inn: Inn) -> Dict:
        """
        parses data for one organization
        """
        pass

    async def parse_many(self, inns: List[Inn]):
        """
        async generator that parses data for many organizations
        """
        for inn in inns:
            yield self.parse(inn)
