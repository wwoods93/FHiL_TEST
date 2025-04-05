# fhil_system.py
# by wilson
# 2025.03.06

import yaml
from singleton_meta import SingletonMeta
from observer import ObservableAbstract
import fhil_constants
import logger_constants
import logger
from logger import Logger



class FhilSystem(ObservableAbstract, metaclass=SingletonMeta):

    _fhil_config_default_path : str = ""
    _fhil_config_d : dict = None
    _instrument_config_d: dict = None

    _config_path: str = None
    _src_path : str = None
    _log_path: str = None

    _fhil_config_file: str = None
    _instrument_config_file: str = None
    _startup_log_file: str = None
    _fhil_log_file : str = None

    _fhil_config_file_path: str = None
    _instrument_config_file_path: str = None
    _startup_log_file_path: str = None
    _fhil_log_file_path: str = None

    _startup_log : Logger = Logger("startup_log", True, True, logger_constants.STARTUP_LOG_DEFAULT_PATH)
    _fhil_log : Logger = None

    def __init__(self, name, fhil_config_default_path):
        super().__init__(name)
        self.attach(self._startup_log)
        self.notify(f"created startup log at: {logger_constants.STARTUP_LOG_DEFAULT_PATH} [SUCCESS]", logger.INFO)
        _fhil_config_default_path = fhil_config_default_path

        # open fhil_config.yaml
        try:
            with open(_fhil_config_default_path, "r") as fhil_config_f:
                # store fhil_config.yaml in dict
                FhilSystem._fhil_config_d = yaml.safe_load(fhil_config_f)

                self.notify(f"read fhil config file at: {_fhil_config_default_path} [SUCCESS]", logger.INFO)
        except FileNotFoundError as e:
            self.notify(f"exception: {e}", logger.EXCEPTION)
        except PermissionError as e:
            self.notify(f"exception: {e}", logger.EXCEPTION)
        except Exception as e:
            self.notify(f"exception: {e}", logger.EXCEPTION)

        FhilSystem._src_path = FhilSystem._fhil_config_d["system_config"]["src_path_rel"]
        FhilSystem._log_path = FhilSystem._fhil_config_d["system_config"]["log_path_rel"]
        FhilSystem._config_path = FhilSystem._fhil_config_d["system_config"]["config_path_rel"]

        FhilSystem._startup_log_file = FhilSystem._fhil_config_d["system_config"]["startup_log"]
        FhilSystem._fhil_log_file = FhilSystem._fhil_config_d["system_config"]["fhil_log"]

        FhilSystem._fhil_config_file = FhilSystem._fhil_config_d["system_config"]["fhil_config"]
        FhilSystem._instrument_config_file = FhilSystem._fhil_config_d["system_config"]["instrument_config"]

        FhilSystem._startup_log_file_path = FhilSystem._log_path + FhilSystem._startup_log_file
        FhilSystem._fhil_log_file_path = FhilSystem._log_path + FhilSystem._fhil_log_file
        FhilSystem._fhil_config_file_path = FhilSystem._config_path + FhilSystem._fhil_config_file
        FhilSystem._instrument_config_file_path = FhilSystem._config_path + FhilSystem._instrument_config_file

    @property
    def config_path(self):
        return self._config_path

    @property
    def src_path(self):
        return self._src_path

    @property
    def log_path(self):
        return self._log_path

    @property
    def fhil_config_file(self):
        return self._fhil_config_file

    @property
    def instrument_config_file(self):
        return self._instrument_config_file

    @property
    def startup_log_file(self):
        return self._startup_log_file

    @property
    def fhil_log_file(self):
        return self._fhil_log_file

    @property
    def fhil_config_file_path(self):
        return self._fhil_config_file_path

    @property
    def instrument_config_file_path(self):
        return self._instrument_config_file_path

    @property
    def startup_log_file_path(self):
        return self._startup_log_file_path

    @property
    def fhil_log_file_path(self):
        return self._fhil_log_file_path




fhil_system = FhilSystem("fhil_system", fhil_constants.SYS_CONFIG_DEFAULT_PATH)

# print(fhil_system.fhil_log_file_path)
# print(fhil_system.startup_log_file_path)
# print(fhil_system.fhil_config_file_path)
# print(fhil_system.instrument_config_file_path)

