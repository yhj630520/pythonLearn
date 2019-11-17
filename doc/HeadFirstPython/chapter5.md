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

2.