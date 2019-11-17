## 函数

1.函数使用def关键字定义，不需要指定函数参数或返回值类型。

2.python中每一个对象都有一个关联的真值，表示这个对象计算为True或者False

> ​	如果计算为0、值None、空窜或者一个空的内置数据结构，则为False。其它为True
>
> ​	可以向bool函数传递任何对象来确定它是True还是False。任何非空数据结构都计算为True

3.使用函数注解来提供参数和返回说明

```python
# str 注解说明希望word参数类型是字符串，->set 说明函数将返回一个set
# 注解添加与否，解释器同样不会对输入和返回进行检验
def search_for_vowels_by_ann(word: str) -> set:
    """Display any vowels found in an supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))

```

4.""" show Display""" 三重引号可以添加多行注释

5.任何参数都可以指定一个默认值

```python
def search_for_vowels_by_ann(phrase: str,letters:str='aeiou') -> set:
    """ 参数指定默认值"""
    return set(letters).intersection(set(phrase))
```

6.python支持位置赋值的同时还支持**关键字赋值**

```python
def search (phrase:str,letters:str='aeiou') -> set:
      return set(letters).intersection(set(phrase))
#位置赋值:严格按照参数顺序
search('galaxy','xyz')
#关键字赋值：指定关键字之后，可以不按照参数顺序
search(letters='xyz',phrase='galaxy')
```

7.使用setuptool安装模块到site-packages中

```python
#第一步：创建一个发布描述：至少为模块创建两个描述文件：setup.py和README.txt
from setuptools import setup

setup(
    name='vsearch',#指定发布包。按照模块命名发布包
    version='1.0',
    description='The Head First Python Search Tools',
    author='head',
    author_email='head@gmail.com',
    url='yinhaijun.com',
    py_modules=['vsearch'],#指定需要包含的.py文件列表
)

#第二步：生成一个发布文件，在包路径下执行命令
python3  setup.py sdist
成功会在当前目录下生成 dist文件夹 里面的vsearch-1.0.tar.gz 就是可安装文件
#第三步：使用安装发布文件
#在dist文件夹目录下执行命令：
python3 -m pip install vsearch-1.0.tar.gz

```