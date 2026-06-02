from sqlalchemy import Column, Integer, String
from event_service.config import Base, engine

class User(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    event_name = Column(String)


Base.metadata.create_all(bind=engine)