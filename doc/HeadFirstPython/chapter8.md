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



### 二 级刑庭