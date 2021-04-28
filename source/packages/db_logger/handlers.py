from logging import Handler, getLogger
from traceback import print_exc
from .crud import Crud
from .models import Log
from .connection_string import create_connection_string


my_crud = Crud(
    connection_string=create_connection_string(),
    encoding='utf-8',
    pool_size=10,
    max_overflow=20,
    pool_recycle=3600)

my_crud.initiate()


class DBHandler(Handler):
    backup_logger = None

    def __init__(self, level=0, backup_logger_name=None):
        super().__init__(level)
        if backup_logger_name:
            self.backup_logger = getLogger(backup_logger_name)

    def emit(self, record):
        try:
            message = self.format(record)
            try:
                last_line = message.rsplit('\n', 1)[-1]
            except:
                last_line = None

            try:
                new_log = Log(module=record.module,
                              thread_name=record.threadName,
                              file_name=record.filename,
                              func_name=record.funcName,
                              level_name=record.levelname,
                              line_no=record.lineno,
                              process_name=record.processName,
                              message=message,
                              last_line=last_line)
                # raise

                my_crud.insert(instances=new_log)
            except:
                if self.backup_logger:
                    try:
                        getattr(self.backup_logger, record.levelname.lower())(record.message)
                    except:
                        print_exc()
                else:
                    print_exc()

        except:
            print_exc()
