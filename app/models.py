from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class TaskModel(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    done = Column(Boolean, default=False)