from logging import basicConfig, getLogger, DEBUG, FileHandler, Formatter
from os import environ

environ['name'] = 'sqlite'
environ['database'] = 'log_db'

from db_logger.handlers import DBHandler

basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%d-%b-%y %H:%M:%S',
            level=DEBUG)
format = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

backup_logger = getLogger('backup_logger')
file_handler = FileHandler('file.log')
file_handler.setLevel(DEBUG)
file_handler.setFormatter(format)
backup_logger.addHandler(file_handler)

db_logger = getLogger('logger')
db_handler = DBHandler(backup_logger_name='backup_logger')
db_handler.setLevel(DEBUG)
db_handler.setFormatter(format)
db_logger.addHandler(db_handler)

if __name__ == "__main__":
    db_logger.debug('debug: hello world!')
    db_logger.info('info: hello world!')
    db_logger.warning('warning: hello world!')
    db_logger.error('error: hello world!')
    db_logger.critical('critical: hello world!!!!')
