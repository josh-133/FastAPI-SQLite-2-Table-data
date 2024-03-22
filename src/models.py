import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import datetime as _dt

import database as _database

class User(_database.Base):
    __tablename__ = "users"
    user_id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    user_name = _sql.Column(_sql.String, unique=True)
    email = _sql.Column(_sql.String, unique=True, index=True)
    hashed_password = _sql.Column(_sql.String)
    is_active = _sql.Column(_sql.Boolean, default=True)
    # When you fetch a User you will also get all the posts they have created
    posts = _orm.relationship("Post", back_populates="owner")
    
class Post(_database.Base):
    __tablename__ = "posts"
    post_id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    title = _sql.Column(_sql.String, index=True)
    content = _sql.Column(_sql.String, index=True)
    owner_id = _sql.Column(_sql.Integer, _sql.ForeignKey("users.user_id"))
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    date_last_updated = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    
    owner = _orm.relationship("User", back_populates="posts")
    