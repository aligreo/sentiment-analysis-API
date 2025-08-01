
from sqlalchemy import create_engine, Column, Integer, String, LargeBinary, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from helpers import get_settings

<<<<<<< HEAD
engine = create_engine(url=get_settings().database_url, connect_args={"check_same_thread": False})
=======
sqlite_database_path = get_settings().DATA_BASE_URI

engine = create_engine(url=sqlite_database_path)
>>>>>>> 3815eccddffd122448034a66c6df5ec620cdbab9
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