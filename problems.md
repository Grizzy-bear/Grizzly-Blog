### 以下是我之前遇到的一些问题，我一般都是打开一个文档编辑器，一边遇到问题就会写上，一般情况都会有解决的时候，不过真心是难受

* extends 相对的是Templates下的绝对路径,如果新建了目录,需要填写路径
---
* 完成了网页与flask的结合,接下来是数据库方面的了

* 使用sqlalchemy到的时候,需要使用
```
 from sqlalchemy.ext.declarative import declarative_base
 Base = declarative_base()
 ```
* 调用declarative_base作为基类,但是使用flask-sqlalchemy的时候,已经封装好了

```
one = Blog(id=str(uuid4()),image='',content="海i",create_time=default)
``` 
* sqlite:定义表单的时候,id避免出现重复,使用uuid4.hex,来定义随机的字符,使用default=uuid.uuid4().hex()自增,但是需注意:id = db.Column(db.UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)目前无法使用,可能和数据库有关,sqlite对UUID有偏见

---
* 报错:Table 'blogs' is already defined for this MetaData instance
* 解决:__table_args__ = {"useexisting": True}
---

* 报错:SAWarning: This declarative base already contains a class with the same class name and module name as app.models.blog.Blog, 
* 解决:解决了id之后就不显示了

---------------------------------------------
* 弃用sqlite,换用mysql,希望不会出现类似的错误
    创建用户：CREATE USER 'username'@'host' IDENTIFIED BY 'password';
删除用户: DROP USER 'username'@'host';
数据库层级的赋权：GRANT ALL ON db_name.* to ()和REVOKE ALL ON db_name.* from ()授予和撤销数据库权限。
---

* user和database和 table 名字最好不一样，不然会出现1044问题
--- 
* 出错：新增加数据库表，如何更新？
* 解决：Mysql里，之所以没有出现更新，是因为model配置里，db.model，没有引入对应表单
* 新问题：即便是引入了，还是无法解决，有人知道码？
---
* 三时间设置默认值，可以导入:
```
from class Test(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32))
    create_date = db.Column(TIMESTAMP, default = datetime.datetime)sqlalchemy.sql.sqltypes import TIMESTAMP
```
---
* 使用ipython操作sqlalchemy的时候，要出入争取的格式和编码类型，img的格式一定要先转化成二进制编码形式

----------------------------------------------
* 记下来就是，数据库与前端的交互了，先从管理界面开始还是从前端开始呢？