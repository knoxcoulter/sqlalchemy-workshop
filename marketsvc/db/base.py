from sqlalchemy import create_engine

engine = create_engine("sqlite+pysqlite:///marketdb", echo=True)


from sqlalchemy.orm import DeclarativeBase
...

class Base(DeclarativeBase):
    pass
