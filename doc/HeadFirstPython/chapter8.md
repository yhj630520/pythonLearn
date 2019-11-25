## 抽象行为和状态

### 一 创建类

#### 1.pass关键字

当用python写代码时，有时可能还没想好代码怎么写，但为了保证语法正确，必须输入一些东西，这种情况下，我们会使用pass语句。**在解释器希望找到具体代码的任何地方都可以使用pass**

```python
def func(*args):
    pass
```

#### 2.类命名约定

函数使用小字母命名（另外有下划线来强调），而类使用CamelCase形式命名，首字母大写。

#### 3.创建类,类共享行为（方法/函数），但不共享状态（属性）

```python
class CountFormBy:
	pass
```

#### 4.调用方法

对象方法的代码只有一个副本，所有这些对象都使用这个代码。不过每个对象都会维护它自己的属性值

```python
c=CountFormBy()
#与 CountFormBy.increase(c) 等价
c.increase()

```

c.increase() 会被解释器转化为：**CountFormBy.increase(c)** 。所以每个方法都至少有一个参数（约定为：self）。

#### 5.python中属性初始化

在python中，在对变量赋值之前不能使用这个变量，而不论在哪里使用。使用变量都必须有一个初始化的值。

python中对象实例化由解释器自动处理，使用**\_\_init\_\_ **根据需要初始化属性。

#### 6.object中的dunder方法和 \_\_init\_\_方法

所有python类都自动继承object类，dunder方法来自object中继承的方法。同时也可以自己实现来进行覆盖。

创建一个新对象时，提供给类的所以参数会传递到\_\_init\_\_ 方法

```python
class CountFromBy:
    def increase(self) -> None:
        self.val += self.incr

    def __init__(self, v: int, i: int) -> None:
        self.val = v
        self.incr = i

c = CountFromBy(100, 1)
```



### 二 级