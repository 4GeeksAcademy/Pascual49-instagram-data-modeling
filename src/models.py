import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    country = Column(String(50))
    birthday = Column(String(50))
    email = Column(String(50))

class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_from_relationship = relationship(User)
    user_to_id = Column(Integer, ForeignKey('user.id'))
    user_to_relationship = relationship(User)


class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_id_relationship = relationship(User)
    
class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    caption = Column(String(250))
    created_time = Column(String(50))
    img_link = Column(String(250))
    video_link = Column(String(250))
    views = Column(Integer)
    likes = Column(Integer)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post_relationship = relationship(Posts)
    location_id = Column(Integer, ForeignKey('location.id'))
    location_relationship = relationship(Location)

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    caption = Column(String(250))
    created_time = Column(String(50))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship(Posts)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e