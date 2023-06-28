from sqlalchemy import create_engine
from database.tables import create_tables

sqlite_database = "sqlite:///./database.db"
engine = create_engine(sqlite_database)

create_tables(engine)