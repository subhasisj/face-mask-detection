import logging
import os

# self._logger = Logger(f'validation_{process}_logs_{self._time_created.date()}_{self._time_created.strftime("%H%M%S")}.log')
class Logger:
    def __init__(self,logfile):
        self._logfile = logfile
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        # logging.basicConfig(filename=f'logs/{self._logfile}',
        # format='%(asctime)s %(levelname)s %(message)s',
        # datefmt='%d-%b-%y %H:%M:%S',level=logging.DEBUG)
        logging.basicConfig(handlers=[logging.FileHandler(f'logs/{self._logfile}', mode='w')],
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt='%d-%b-%y %H:%M:%S',level=logging.DEBUG)

    def log(self, log_message,level='info'):
        getattr(logging, level)(log_message)

