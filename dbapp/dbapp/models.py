from sqlalchemy import Table
from dbapp import app, meta, engine

actors = Table('actor', meta, autoload=True, autoload_with=engine)
