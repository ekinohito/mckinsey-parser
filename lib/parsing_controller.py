from typing import Any, List, Optional
from lib.parsers.data_parsers.data_parser import DataParser
from lib.parsers.id_parsers.id_parser import IdParser
from types_.category_id import CategoryId
from lib.db import update_supplier

class ParsingController:
    def __init__(self, id_parsers: List[IdParser]=None, data_parsers: List[DataParser]=None):
        self.fsm: Any = None
        self.cat_id: str = ''
        self.id_parsers = id_parsers or [] 
        self.data_parsers = data_parsers or []
        self.inns = []
        self.suppliers = {}

    def set_fsm(self, fsm):
        self.fsm = fsm

    def set_cat_id(self, cat_id: CategoryId):
        self.cat_id = cat_id

    def trigger(self, event: str):
        if (self.fsm):
            self.fsm.trigger(event)

    async def parse_inns(self):
        self.inns = []
        self.suppliers = {}
        for id_parser in self.id_parsers:
            for inn in await id_parser.parse(self.cat_id):
                self.inns.append(inn)
        self.trigger('fetching_ids_finish')
        return self.inns
    
    async def parse_supplier(self, inn):
        result = {}
        for data_parser in self.data_parsers:
            data = await data_parser.parse(inn)
            if data_parser.key_name is None:
                for (k, v) in data.items():
                    result[k] = v
            else:
                result[data_parser.key_name] = data
        self.suppliers[inn] = result
        return result
    
    async def parse_suppliers(self):
        for inn in self.inns:
            print('fetching supplier', inn)
            await self.parse_supplier(inn)
        self.trigger('fetching_data_finish')

    async def save_data(self):
        for inn in self.inns:
            supplier = self.suppliers[inn]
            await update_supplier(inn, supplier)
        self.trigger('uploading_data_finish')
            
