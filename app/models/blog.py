from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from app import db
# from datetime import datetime
import datetime
import base64
import uuid
from sqlalchemy import MetaData
# from sqlalchemy.dialects.sqlite import UUID
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql import func



def generateUUID(prefix = ""):
    generatedUuid4 = uuid.uuid4()
    generatedUuid4Str = str(generatedUuid4)
    newUuid = prefix + generatedUuid4Str
    gLog.debug("prefix=%s, generatedUuid4Str=%s, newUuid=%s", prefix, generatedUuid4Str, newUuid)
    return newUuid

class Blog(db.Model):
    
    __tablename__ = "blogs"
    __table_args__ = {"useexisting": True}

    id = db.Column(db.Integer, primary_key=True)


    names = db.Column(db.String(50), nullable=False)
    images = db.Column(db.LargeBinary,nullable=False)
    content = db.Column(db.Text,nullable=False)
    create_time  = db.Column(db.DateTime, nullable=True,default=datetime.date.today())

    

    def __repr__(self):
        return "Role: %s %s" % (self.id,self.content[:10])
    
    def __init__(self,image,content,create_time):

        self.image = image
        self.content = content
        self.create_time = create_time
    
    def save(self):
        db.session.add(self)
        db.session.commit()

class Portfolio(db.Model):
    __tablename__ = "portfolios"
    __table_args__ = {"useexisting": True}


    id = db.Column(db.Integer, primary_key=True)
   
    name = db.Column(db.String(50), nullable=False)
    illus = db.Column(db.String(120), nullable=False)
    image = db.Column(db.LargeBinary,nullable=False)
    content = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime, nullable=True, default=datetime.date.today())

    def __repr__(self):
        return '<User %r>' % self.name

    def __init__(self,image,content,create_time):
        # self.id = id
        self.image = image
        self.content = content
        self.create_time = create_time
        self.name = name
        self.illus = illus
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    

class Test(db.Model):
    __tablename__ = "testBlog"
    __table_args__ = {"useexisting": True}
    
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(50), nullable=False)
    illus = db.Column(db.String(150), nullable=False)
    image = db.Column(db.LargeBinary,nullable=False)
    content = db.Column(db.Text,nullable=False)
    
    create_time = db.Column(db.DateTime, nullable=True, default=datetime.date.today())
   

    
    def __repr__(self):
       
        return '<User %r>' % self.name
    
    def __init__(self,image,content,create_time):
       
        self.image = image
        self.content = content
        self.create_time = create_time
        self.name = name
        self.illus = illus

    def save(self):
        db.session.add(self)
        db.session.commit()
