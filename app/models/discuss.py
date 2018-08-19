import base64
import uuid
from sqlalchemy import MetaData
# from sqlalchemy.dialects.sqlite import UUID
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql import func
from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from app import db
# from datetime import datetime
import datetime

class Discuss(db.Model):
    __tablename__ = "discusses"
    __table_args__ = {"useexisting": True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=True)
    create_time  = db.Column(db.DateTime, nullable=True,default=datetime.date.today())
    phone = db.Column(db.String(50), nullable=True)
    message=db.Column(db.Text,nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name