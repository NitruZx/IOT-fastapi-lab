from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP, DateTime, Text, Float
# from sqlalchemy.orm import relationship
import enum
from sqlalchemy import Enum
from database import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    year = Column(Integer)
    is_published = Column(Boolean)
    description = Column(Text)
    synopsis = Column(Text)
    category = Column(Text)
    image_url = Column(Text)

class Sex(enum.Enum):
    male = 1
    female = 2

class Student(Base):
    __tablename__ = 'students'

    id = Column(String, primary_key=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    dob = Column(DateTime(timezone=True))
    sex = Column(Enum(Sex))
    
class Menu(Base):
    __tablename__ = 'menus'
    
    menu_id = Column(Integer, primary_key=True, index=True)
    menu_name = Column(String)
    menu_description = Column(Text)
    menu_price = Column(Float)
    menu_image = Column(Text)
    
class Order(Base):
    __tablename__ = 'orders'
    
    order_id = Column(Integer, primary_key=True, index=True)
    order_name = Column(String)
    order_tel = Column(String)
    order_item = Column(Text)
    total_price = Column(Float)