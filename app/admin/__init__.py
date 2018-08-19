from flask import Blueprint

# 必须加个前缀,不然会报错
auth = Blueprint('admin', __name__,url_prefix='/admin')


# from .users import *
from . import views