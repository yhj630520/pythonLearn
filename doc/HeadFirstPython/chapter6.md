## python数据处理

1.python打开、处理和关闭文件

```python
#打开文件，a 表示采用追加模式。默认为‘读’模式
todos=open('todos.txt','a')
#使用print函数写入，指定文件流
print('Put out the trash.',file=todos)
#close()关闭流
todos.close()
```

2.open模式说明：如果第一个参数指定的文件不存在，除	**'r'** 外，都会创建新的空文件

​	**'r'** : 读数据模式，默认模式，参数可选

​	**'w'** : 写数据，如果已有内容会清空

​	**'a'** : 追加模式，在文件末尾增加新数据

​	**'x'** :打开新文件来写数据，如果文件存在则失败

在模式中添加	**'b'** 来指定**二进制**模式（**'wb'**: 写二进制数据 ）

**'+'**：表示会打开文件来完成读写（**'x+b'**: 读写一个新的二进制文件）

3.**with**语句管理上下文

```python
# 使用with结束，系统会调用close()
with open('todos.txt') as tasks:
    for chore in tasks:
        print(chore, end='')
```

4.