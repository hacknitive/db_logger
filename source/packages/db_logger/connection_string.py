from os import environ

name = environ.get('name')
if name:
    name = name.lower()
else:
    name = 'sqlite'

driver = environ.get('driver')
if driver:
    driver = driver.lower()
database = environ.get('database')
if not database:
    database = 'log_db'

username = environ.get('username')
password = environ.get('password')
host = environ.get('host')
port = environ.get('port')


def create_connection_string():
    # dialect+driver://username:password@host:port/database
    connection_string = f'+{driver}://{username}:{password}@{host}:{port}/{database}'
    if name in ("postgresql",):
        return "postgresql" + connection_string

    elif name in ('mysql', ):
        return 'mysql' + connection_string

    elif name in ('oracle', ):
        return "oracle" + connection_string

    elif name in ('microsoft sql server', 'mssql'):
        return "mssql" + connection_string

    elif name in ("sqlite", 'sqlite3'):
        # sqlite://<nohostname>/<path>
        return f'sqlite:///{database}.sqlite3'
