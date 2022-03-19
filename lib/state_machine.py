from asyncio import create_task, sleep
from transitions import Machine

from lib.parsing_controller import ParsingController

class UpdateFSM:
    def __init__(self, parsing_controller: ParsingController):
        self.parsing_controller = parsing_controller
        parsing_controller.set_fsm(self)
        self.machine = Machine(self, ['idle', 'fetching_ids', 'fetching_data', 'updating_db'], 'idle')
        self.machine.add_transition('start_update', 'idle', 'fetching_ids', after='start_fetching_ids')
        self.machine.add_transition('fetching_ids_finish', 'fetching_ids', 'fetching_data', after='start_fetching_data')
        self.machine.add_transition('fetching_data_finish', 'fetching_data', 'updating_db', after='start_updating_db')
        self.machine.add_transition('uploading_data_finish', 'updating_db', 'idle')

    def start_fetching_ids(self):
        print('FSM: id fetching start')
        create_task(self.parsing_controller.parse_inns())
    
    def start_fetching_data(self):
        print('FSM: data fetching start')
        create_task(self.parsing_controller.parse_suppliers())
    
    def start_updating_db(self):
        print('FSM: data uploading start')
        create_task(self.parsing_controller.save_data())

    