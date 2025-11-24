from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from blog.database import Base


class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String())
    content = Column(Text)
    creator_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship("User", back_populates="blogs")

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String())
    email = Column(String())
    password = Column(String(72))

    blogs = relationship("Blog", back_populates="creator")