import pyvisa
print(pyvisa.__version__)

from observer import Observable_Abstract
from logger import Logger
import logger_constants
import dho800900_constants

class Dho800900(Observable_Abstract):

    CMD_RUN = ':RUN\n'


    def __init__(self, arg_model, arg_name, arg_ip_address, arg_instrument, arg_logger):
        super().__init__(arg_name)
        self.model = arg_model
        self.name = arg_name
        self.ip_address = arg_ip_address
        self.instrument = arg_instrument
        self.attach(arg_logger)
        self.notify('initializing Dho800900 oscilloscope', message_type=1)  # INFO level
        self.notify(f'model: {self.model}, name: {self.name}, ip_address: {self.ip_address}', message_type=1)  # INFO level

    def run(self):
        """Start running the oscilloscope (=RUN button)"""
        try:
            self.instrument.write(Dho800900.CMD_RUN)
            self.notify(f'{self.name}: instrument write | command= {Dho800900.CMD_RUN} ', message_type=1)  # INFO level
        except Exception as e:
            self.notify(f'{self.name}: failed to run the oscilloscope | error= {str(e)}', message_type=3)



rm = pyvisa.ResourceManager()
print(rm.list_resources())
instr = rm.open_resource('TCPIP::192.168.1.100::INSTR')

log = Logger("oscilloscope_logger", supports_console=True, supports_logfile=True, log_file_path=logger_constants.GENERAL_LOG_DEFAULT_PATH)

dho924s = Dho800900(dho800900_constants.DHO914.NAME, 'dho924s',  '192.168.1.100', instr, log)