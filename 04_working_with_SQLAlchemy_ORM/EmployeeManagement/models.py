from sqlalchemy import Column, Integer, String, Date
from config import Base,engine

class Employee(Base):
    __tablename__ = "events"
    emp_id = Column(Integer, primary_key=True, index=True)
    emp_name = Column(String, index=True)
    designation = Column(String, index=True)
    salary = Column(Integer)

Base.metadata.create_all(bind=engine)
