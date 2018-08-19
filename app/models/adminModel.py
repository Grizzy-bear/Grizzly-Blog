import os.path as op
import os
from flask_admin.contrib.sqla import ModelView
from flask_admin import expose
# from flask_admin import render, NameForm


file_path = op.join(op.dirname(__file__), 'static/upload') # 文件上传路径

class BaseView(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated and current_username == "Grizzly":
            return True
        return False
    can_create =False

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('login', next=request.url))
    
class BlogView(BaseView):
    # pass
    can_create = False  #默认不支持新建数据扩展
    column_labels = {
        'id':u'序号',
        'title':u'标题',
        'timestamp':u'发布时间',
        'count':u'浏览次数',
        'content':u'内容',
        'img':u'图片'
    }
    column_list = ('id', 'title','timestamp','count','content','img')
    
    def __init__(self, session, **kwargs):
        super(BlogView, self).__init__(Blogs, session, **kwargs)

class MyView(BaseView):
    # 创建视图
    @expose('/admin', methods=['GET','POST'])
    def index(self):
        form = NameForm()
        return self.render('admin/index.html',form=form)

class Portfilo(BaseView):
    pass