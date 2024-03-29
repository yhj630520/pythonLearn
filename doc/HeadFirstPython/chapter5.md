## 构建一个web程序

1.使用Flask构建一个web程序

```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'


app.run()

```

**\_\_name\_\_ **:类型值由python解释器维护：

​	1.该类值称之为：dunder name 也称之为 dunders

​	2.使用单个下划线字符为某些变量名前缀：称之为 wonder（one underscore 的缩写）

@app.route('/')

称之为：修饰符（decorator），可以调整一个现有函数的行为，而无需修改这个函数的代码

修饰符可用于函数和类。多用于函数，也被称为：函数修饰符

2.dunder name dunder main

**\_\_name\_\_ **: 单在当前活动命名空间时总是为：**\_\_main\_\_ ** ，如果作为一个模块导入就是模块的名字

3.Flask中请求redirect和多route

```python
#使用redirect进行重定向 import redirect
@app.route('/')
def hello() -> '302':
    return redirect('/entry')

#多路径支持
@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')

```



