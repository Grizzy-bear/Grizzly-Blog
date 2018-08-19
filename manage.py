
from flask_script import Manager
# from flask import Flask
from flask_migrate import Migrate,MigrateCommand

from app import create_app, db




# from flask_admin import Admin, BaseView, expose

app = create_app()
# admin = Admin(app, name='后台管理')

manager = Manager(app)

from app.models.blog import Blog, Portfolio, Test
from app.models.discuss import Discuss

migrate = Migrate(app, db)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__': 
    manager.run() 