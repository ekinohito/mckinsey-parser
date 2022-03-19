from asyncio import create_task, sleep
from fastapi import FastAPI
from lib.parsers.data_parsers.contacts_parser import ContactsParser
from lib.parsers.id_parsers.mock_id_parser import MockIdParser
from lib.parsing_controller import ParsingController

from lib.state_machine import UpdateFSM

app = FastAPI()

controller = ParsingController(id_parsers=[MockIdParser()], data_parsers=[ContactsParser()])
fsm = UpdateFSM(controller)

@app.get("/")
async def root():
    return {"message": 'ok', "fsm": fsm.state}

@app.get("/update/start")
async def update_start():
    fsm.start_update()
    return {"message": "update started"}

@app.get("/update/status")
async def update_status():
    return {"message": "ok", "db": fsm.db}
