from sqlalchemy import Column, Integer, String, Boolean, ForeignKey,Enum as Sqlalchemy_enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base
import enum
class ReactionType(str,enum.Enum):
    LIKE = "like"
    LOVE = "love"
    ANGRY = "angry"
    SAD = "sad"
    WOW = "wow"

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post")
    reacts = relationship("React", back_populates="post")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    posts = relationship("Post", back_populates="owner")
    comments = relationship("Comment", back_populates="owner")
    reacts = relationship("React", back_populates="owner")

class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    parent_id = Column(Integer, ForeignKey("comments.id", ondelete="CASCADE"))
    
    post = relationship("Post", back_populates="comments")
    owner = relationship("User", back_populates="comments")
    parent = relationship("Comment", remote_side=[id], back_populates="comments")
    comments = relationship("Comment", back_populates="parent")
    reacts = relationship("React", back_populates="comment")

class React(Base):
    __tablename__ = "reacts"
    id = Column(Integer, primary_key=True, nullable=False)
    type = Column(Sqlalchemy_enum(ReactionType),nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    comment_id = Column(Integer, ForeignKey("comments.id", ondelete="CASCADE"))
    
    post = relationship("Post", back_populates="reacts")
    owner = relationship("User", back_populates="reacts")
    comment = relationship("Comment", back_populates="reacts")