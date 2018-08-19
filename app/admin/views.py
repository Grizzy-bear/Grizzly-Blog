from flask import render_template, session, redirect, url_for

from . import admin
from .. import db

@admin.route('/home',endpoint='Home')
def hello():
    return render_template('/admin/index.html')