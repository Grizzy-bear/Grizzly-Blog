from flask import render_template, session, redirect, url_for

# from ..models import user 
from . import auth
from .. import db

@auth.route('/home', endpoint='Home')
def blog():
    return render_template('/blog/index.html')

@auth.route('/article', endpoint='Article')
def home():
    return render_template('/blog/blog.html')
    
    # return 'shishi'
@auth.route('/test')
def test():
    return render_template('test.html')

@auth.route('/portfolio',endpoint='Portfolio')
def portfolio():
    return render_template('/blog/portfolio.html')

@auth.route('/about', endpoint='About')
def portfolio():
    return render_template('/blog/about.html')

@auth.route('/contact', endpoint='Contact')
def portfolio():
    return render_template('/blog/contact.html')

@auth.route('/contactMe', endpoint='ContactMe')
def portfolio():
    return render_template('/contact/contactMe.html')