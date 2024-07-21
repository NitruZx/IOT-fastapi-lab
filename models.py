from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP, DateTime,Text
# from sqlalchemy.orm import relationship
import enum
from sqlalchemy import Enum
from database import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    year = Column(Integer, index=True)
    is_published = Column(Boolean, index=True)
    description = Column(Text, index=True)
    synopsis = Column(Text, index=True)
    image_url = Column(Text, index=True)

class Sex(enum.Enum):
    male = 1
    female = 2

class Student(Base):
    __tablename__ = 'students'

    id = Column(String, primary_key=True, index=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    dob = Column(DateTime(timezone=True))
    sex = Column(Enum(Sex))