listChar = [1, 2, 3]
print(listChar)
person1 = {listChar[1]: ["list:1", 2, 3], 'Age': 28, 'Gender': 'Male'}
print(person1)
print(person1[2][0])

coll = {'a', 'e', 'i', 'o', 'u', 'U', 'a'}
print(coll)
print(sorted(coll))
#

word = 'jack'
# set快速创建集合
print(set(word))
# 两个集合取并集： {'o', 'j', 'e', 'i', 'a', 'U', 'c', 'u', 'k'}
print(coll.union(set(word)))
# 找出存在于coll但是set(word)集合不存在的集合 {'o', 'i', 'u', 'U', 'e'}
print(coll.difference(set(word)))
# 找出共同存在的数据集合： {'a'}
print(coll.intersection(set(word)))
