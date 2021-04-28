from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from .models import base
from traceback import print_exc


class Crud:
    def __init__(self, connection_string=f'sqlite:///log_db.sqlite3',
                 encoding='utf-8',
                 pool_size=10,
                 max_overflow=20,
                 pool_recycle=3600):

        self.connection_string = connection_string
        self.encoding = encoding
        self.pool_size = pool_size
        self.max_overflow = max_overflow
        self.pool_recycle = pool_recycle
        self.engine = None
        self.session = None

    def initiate(self):
        self.create_engine()
        self.create_session()
        self.create_tables()

    def create_engine(self):
        self.engine = create_engine(self.connection_string)

    def create_session(self):
        self.session = Session(bind=self.engine)

    def create_tables(self):
        base.metadata.create_all(self.engine)

    def insert(self, instances):
        try:
            self.session.add(instances)
            self.session.commit()
            self.session.flush()
        except:
            self.session.rollback()
            self.initiate()
            raise

    def __del__(self):
        self.close_session()
        self.close_all_connections()

    def close_session(self):
        try:
            self.session.close()
        except:
            print_exc()
        else:
            self.session = None

    def close_all_connections(self):
        try:
            self.engine.dispose()
        except:
            print_exc()
        else:
            self.engine = None





