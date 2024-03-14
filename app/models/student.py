from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func

from app.database import Base


class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(45))
    last_name = Column(String(45))
    age = Column(Integer)


class Courses(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45))
    date = Column(DateTime(), server_default=func.now())
    description = Column(String(100))
    student_id = Column(Integer, ForeignKey(Students.id, ondelete="CASCADE"))