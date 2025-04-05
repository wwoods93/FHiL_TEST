import logging
from queue import PriorityQueue
import logger_constants
from observer import ObserverAbstract


DEBUG: int = 0
INFO: int = 1
WARNING: int = 2
ERROR: int = 3
EXCEPTION: int = 4
CRITICAL: int = 5


class Logger(ObserverAbstract):
    def __init__(self, name, supports_console=True, supports_logfile=True, log_file_path=None):
        super().__init__(name)

        self._supports_console: bool = True
        self._enable_console: bool = True

        self._supports_logfile: bool = True
        self._enable_logfile: bool = True

        self._logger = logging.getLogger(name)
        self._logger.setLevel(logging.DEBUG)
        self._message_buffer = PriorityQueue()

        self._console_handler = logging.StreamHandler()
        self._console_handler.setLevel(logging.DEBUG)

        if supports_logfile is True and log_file_path is not None:
            self._file_handler = logging.FileHandler(log_file_path)

        self._file_handler.setLevel(logging.DEBUG)

        self._formatter = logging.Formatter("%(asctime)s :: %(levelname)s :: %(message)s")
        self._console_handler.setFormatter(self._formatter)
        self._file_handler.setFormatter(self._formatter)


    def update(self, message, message_type=None):
        if message_type is None or message_type is DEBUG:
            self.debug(message)
        elif message_type is INFO:
            self.info(message)
        elif message_type is WARNING:
            self.warning(message)
        elif message_type is ERROR:
            self.error(message)
        elif message_type is EXCEPTION:
            self.exception(message)


    def debug(self, message):
        if self._supports_logfile & self._enable_logfile:
            self._logger.addHandler(self._file_handler)
            self._logger.debug(message)
            self._logger.removeHandler(self._file_handler)
        if self._supports_console & self._enable_console:
            self._logger.addHandler(self._console_handler)
            self._logger.debug(message)
            self._logger.removeHandler(self._console_handler)

    def info(self, message):
        if self._supports_logfile & self._enable_logfile:
            self._logger.addHandler(self._file_handler)
            self._logger.info(message)
            self._logger.removeHandler(self._file_handler)
        if self._supports_console & self._enable_console:
            self._logger.addHandler(self._console_handler)
            self._logger.info(message)
            self._logger.removeHandler(self._console_handler)

    def warning(self, message):
        if self._supports_logfile & self._enable_logfile:
            self._logger.addHandler(self._file_handler)
            self._logger.warning(message)
            self._logger.removeHandler(self._file_handler)
        if self._supports_console & self._enable_console:
            self._logger.addHandler(self._console_handler)
            self._logger.warning(message)
            self._logger.removeHandler(self._console_handler)

    def error(self, message):
        if self._supports_logfile & self._enable_logfile:
            self._logger.addHandler(self._file_handler)
            self._logger.error(message)
            self._logger.removeHandler(self._file_handler)
        if self._supports_console & self._enable_console:
            self._logger.addHandler(self._console_handler)
            self._logger.error(message)
            self._logger.removeHandler(self._console_handler)

    def exception(self, message):
        if self._supports_logfile & self._enable_logfile:
            self._logger.addHandler(self._file_handler)
            self._logger.exception(message)
            self._logger.removeHandler(self._file_handler)
        if self._supports_console & self._enable_console:
            self._logger.addHandler(self._console_handler)
            self._logger.exception(message)
            self._logger.removeHandler(self._console_handler)






# log = Logger("debug_logger", True, True, logger_constants.GENERAL_LOG_DEFAULT_PATH)
# log.error("error message")
# log.warning("warning message")
# log.exception("exception message")