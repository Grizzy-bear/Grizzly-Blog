from app import db

class User(db.Model):
    __tablename = "users"

    id = db.Column(db.Integer, primary_key=True)
    Usercode = db.Column(db.String(64),unique=True, index = True)
    Password = db.Column(db.String(128))

    def __init__(self, Usercode=None, Password=None):
        self.Usercode = Usercode
        self,Password = Password
    
    def __repr__(self):
        return '<User %>' % self.Usercode

