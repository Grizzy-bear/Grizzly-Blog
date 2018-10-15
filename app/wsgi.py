import os
# from . import auth
from app import create_app
import datetime

app = create_app()
@app.context_processor
def template_extras():
    """
    上下文处理。返回的字典可以在上下文使用
    """
    return {'enumerate': enumerate, 'len': len, 'datetime': datetime}
