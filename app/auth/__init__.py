from flask import Blueprint

# 必须加个前缀,不然会报错
auth = Blueprint('auth', __name__,url_prefix='/auth')


# from .users import *
from . import views, error