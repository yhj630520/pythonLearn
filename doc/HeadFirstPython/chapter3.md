1.字典，用来保持一个键/值对集合（其它语言也称为 映射、散列和表）

2.创建： person={’Name’:’Ford’,’Gender’:’Male'}

3.python中没有++ 和 — 操作符 可以使用 += 和 -= 替代

4.循环输出字典中的数据

```python
  found={'apple':1,'banan':2}   
  for k in found: 
       print(k," " ,  found[k]  )
```
​     循环获取的k 为键

5. 循环字典输出的顺序随机，可以使用内置函数 sorted进行排序 for k in  sorted(found):

6. 字典内置方法 items() 可以返回 k/v是循环的首选方式：for k，v in sorted(found.itmes())

7. 字典内置方法：setdefault  单没有key不存在时设置默认值，存在key时不做任何操作 

     found.setdefault(‘apple’,0) 

8.集合（不允许有重复，查找速度快） 

```python
# 创建一个集合
coll = {'a', 'e', 'i', 'o', 'u', 'U', 'a'}
print(coll) 
#输出结果 {'o', 'e', 'U', 'i', 'a', 'u'} ，去除了重复数据且输出顺序随机
print(sorted(coll))
#输出结果 ['U', 'a', 'e', 'i', 'o', 'u'],去除了重复数据且排序输出为集合



```

