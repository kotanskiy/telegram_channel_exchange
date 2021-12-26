from databases import Database
from sqlalchemy import create_engine, MetaData

from config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME


DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


database = Database(DATABASE_URL)
metadata = MetaData()
db_engine = create_engine(DATABASE_URL)


__all__ = (
    'database',
    'metadata',
    'db_engine',
)
