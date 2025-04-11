import pyvisa # type: ignore
print(pyvisa.__version__)

from observer import ObservableAbstract
from logger import Logger
import logger_constants
import embedded_test.scripts.dho900_defs as dho900_defs

class Dho900(ObservableAbstract):

    W_CMD_RUN = ':RUN\n'
    W_CMD_STOP = ':STOP\n'
    W_CMD_SING = ':SING\n'
    W_CMD_AUT = ':AUT\n'
    W_CMD_CLE = ':CLE\n'
    W_CMD_TFOR = ':TFOR\n'

    # autoset peak-to-peak priority
    Q_CMD_AUT_PEAK = ':AUT:PEAK?\n'
    W_CMD_AUT_PEAK = ':AUT:PEAK {setting}\n'    # 1|ON or 0|OFF

    # autoset open (read all channels (OFF) or only enabled (ON))
    Q_CMD_AUT_OPEN = ':AUT:OPEN?\n'
    W_CMD_AUT_OPEN = ':AUT:OPEN {setting}\n'  # 1|ON or 0|OFF

    # autoset waveform overlap
    Q_CMD_AUT_OVER = ':AUT:OVER?\n'
    W_CMD_AUT_OVER = ':AUT:OVER {setting}\n'  # 1|ON or 0|OFF

    # autoset keep coupling for subsequent AUTO operations
    Q_CMD_AUT_KEEP = ':AUT:KEEP?\n'
    W_CMD_AUT_KEEP = ':AUT:KEEP {setting}\n'  # 1|ON or 0|OFF

    # autoset lock AUTO key (lock AUTO key and disable AUTO function (ON) or unlock AUTO key and enable AUTO function (OFF)))  
    Q_CMD_AUT_LOCK = ':AUT:LOCK?\n'
    W_CMD_AUT_LOCK = ':AUT:LOCK {setting}\n'  # 1|ON or 0|OFF

    # autoset enable
    Q_CMD_AUT_ENA = ':AUT:ENA?\n'
    W_CMD_AUT_ENA = ':AUT:ENA {setting}\n'  # 1|ON or 0|OFF

    
    # acquire average (number of samples taken in average acquisition mode)
    Q_CMD_ACQ_AVER = ':ACQ:AVER?\n'
    W_CMD_ACQ_AVER = ':ACQ:AVER {samples}\n'  # samples is a base 2 number 2^n with 1 <= n <= 16 

    # acquire mdepth
    Q_CMD_ACQ_MDEP = ':ACQ:MDEP?\n'
    W_CMD_ACQ_MDEP = ':ACQ:MDEP {depth}\n'
    # for 1 channel  enabled: AUTO, 1k, 10k, 100k, 1M, 5M, 10M, 25M, 50M (50M is DHO900 only)
    # for 2 channels enabled: AUTO, 1k, 10k, 100k, 1M, 5M, 10M, 25M (25M is DHO900 only)
    # for 4 channels enabled: AUTO, 1k, 10k, 100k, 1M, 5M, 10M (10M is DHO900 only)

    # acquire type
    Q_CMD_ACQ_TYPE = ':ACQ:TYPE?\n'
    W_CMD_ACQ_TYPE = ':ACQ:TYPE {type}\n'  # types: NORM | PEAK | AVER | ULTR

    # acquire sample rate
    Q_CMD_ACQ_SRAT = ':ACQ:SRAT?\n'

    Q_CMD_ACQ_ULTR_MODE = ':ACQ:ULTR:MODE?\n'
    W_CMD_ACQ_ULTR_MODE = ':ACQ:ULTR:MODE{mode}\n' # modes: ADJ | OVER | WAT | PERS | MOS

    Q_CMD_ACQ_ULTR_TIM = ':ACQ:ULTR:TIM?\n'
    W_CMD_ACQ_ULTR_TIM = ':ACQ:ULTR:TIM {timeout}\n' # timeout: 1us to 1s in decimal or scientific notation




    Q_CMD_IDN = '*IDN?\n'

    def __init__(self, arg_model, arg_name, arg_ip_address, arg_instrument, arg_logger):
        super().__init__(arg_name)
        self.model = arg_model
        self.name = arg_name
        self.ip_address = arg_ip_address
        self.instrument = arg_instrument
        self.attach(arg_logger)
        self.notify('initializing DHO900 series oscilloscope', message_type=1)  # INFO level
        self.notify(f'model: {self.model}, name: {self.name}, ip_address: {self.ip_address}', message_type=1)  # INFO level

    def execute_command_set(self, cmd_, a0_=None, a1_=None, a2_=None):
        """Execute a command"""
        if cmd_== False or cmd_== None:
            self.notify(f'type(self).__name__: invalid or missing command', message_type=3)
            return 1
        else:
            args = [a0_, a1_, a2_]
            for arg in args:
                if arg == None:
                    arg = ''
            self.write_cmd(cmd_.format(*args))
            return 0
  
    def execute_command_get(self, cmd_, a0_=None, a1_=None, a2_=None):
        """Execute a command and return the response"""
        if cmd_== False or cmd_== None:
            self.notify(f'type(self).__name__: invalid or missing command', message_type=3)
            return 1
        else:
            args = [a0_, a1_, a2_]
            for arg in args:
                if arg == None:
                    arg = ''
            return self.query_cmd(cmd_.format(*args))
        
    def execute_ch_command_set(self, ch_cmd_, ch_, a0_=None, a1_=None, a2_=None):
        """Execute a command"""
        if ch_cmd_== False or ch_cmd_== None:
            self.notify(f'type(self).__name__: invalid or missing command', message_type=3)
            return 1
        elif ch_== False or ch_== None:
            self.notify(f'type(self).__name__: invalid or missing channel < 1 | 2 | 3 | 4 >', message_type=3)
            return 1
        else:        
            args = [ch_, a0_, a1_, a2_]
            for arg in args:
                if arg == None:
                    arg = ''
            self.write_cmd(ch_cmd_.format(*args))
            return 0

    def execute_ch_command_get(self, ch_cmd_, ch_, a0_=None, a1_=None, a2_=None):
        """Execute a command and return the response"""
        if ch_cmd_== False or ch_cmd_== None:
            self.notify(f'type(self).__name__: invalid or missing command', message_type=3)
            return 1
        elif ch_== False or ch_== None:
            self.notify(f'type(self).__name__: invalid or missing channel < 1 | 2 | 3 | 4 >', message_type=3)
            return 1
        else:
            args = [a0_, a1_, a2_]
            for arg in args:
                if arg == None:
                    arg = ''
            return self.query_cmd(ch_cmd_.format(*args))
    


    def query_cmd(self, command):
        """Send a command to the instrument and return the response"""
        try:
            response = self.instrument.query(command)
            self.notify(f'{self.name}: instrument query | command= {command}, response= {response}', message_type=1)  # INFO level
            return response
        except Exception as e:
            self.notify(f'{self.name}: command failed | error= {str(e)}', message_type=3)
            return None
        
    def write_cmd(self, command):
        """Send a command to the instrument without response"""
        try:
            self.instrument.write(command)
            self.notify(f'{self.name}: instrument write | command= {command}', message_type=1)  # INFO level
        except Exception as e:
            self.notify(f'{self.name}: command {command} failed | error= {str(e)}', message_type=3)



    # def exec_cmd_run(self):
    #     """Start running the oscilloscope (=RUN button)"""
    #     self.write_cmd(Dho800900.W_CMD_RUN)

    # def exec_cmd_stop(self):
    #     """Stop running the oscilloscope (=STOP button)"""
    #     self.write_cmd(Dho800900.W_CMD_STOP)



rm = pyvisa.ResourceManager()
print(rm.list_resources())
instr = rm.open_resource('TCPIP::192.168.1.100::INSTR')

log = Logger("oscilloscope_logger", supports_console=True, supports_logfile=True, log_file_path=logger_constants.GENERAL_LOG_DEFAULT_PATH)

dho924s = Dho900(dho900_defs.DHO924S.NAME, 'dho924s',  '192.168.1.100', instr, log)


dho924s.execute_command_set(Dho900.W_CMD_STOP)
# dho924s.execute_command_set(Dho900.W_CMD_RUN)
# dho924s.exec_cmd_run()