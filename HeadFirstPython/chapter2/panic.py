phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

# 目标字符串：on tap
# 删除列表后四个字符
for i in range(4):
    plist.pop()
# 删除列表第一个字符
plist.pop(0)
# 删除列表中特定字符"'"
plist.remove("'")
print(plist)
# 先弹出列表最后两个元素：'a','p'生成新队列 然后插入到plist末尾中
plist.extend([plist.pop(), plist.pop()])
print(plist)
# 弹出索引3的值' '，插入到索引2 't'之前
plist.insert(2, plist.pop(3))

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
