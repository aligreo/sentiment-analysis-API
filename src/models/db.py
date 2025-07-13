
from sqlalchemy import create_engine, Column, Integer, String, LargeBinary, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from helpers import get_settings

sqlite_database_path = get_settings().DATA_BASE_URI

engine = create_engine(url=sqlite_database_path)
sessionLocal = sessionmaker(engine)
Base = declarative_base()

class Texts(Base):
    __tablename__ = 'Texts'
    id = Column(Integer, primary_key=True, nullable=False)
    text = Column(String, nullable=False)
    label = Column(String, nullable=False)
    score = Column(DECIMAL, nullable=False)

def init_db():
    Base.metadata.create_all(engine)