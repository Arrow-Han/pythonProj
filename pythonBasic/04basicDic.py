# about dictionary
# practise01
dic01 = {
    'name': ['alex', 2, 3, 5],
    'job': 'teacher',
    'oldboy': {'alex': ['python01', 'python02', 100]}
}
print(dic01)
dic01.get('name').append('wusir')
print(dic01)
print('--------------')
dic01.get('name')[0] = dic01.get('name')[0].capitalize()
print(dic01)
print('--------------')
dic01.get('oldboy')['老男孩'] = 'linux'
print(dic01)
print('===============')
# 删除操作需要注意一下
temp01 = dic01.get('oldboy')
print(temp01)
temp02 = temp01.get('alex')
print(temp02)
del temp02[1]
print(temp02)
print(dic01)

print('---------')
dic02 = {"李晨": "范冰冰", "邓超": "孙俪", "王祖蓝": "李亚男"}
dic03 = {"李晨": "张馨予", "郑凯": "baby", "王宝强": "马蓉"}
dic03.update(dic02)  # 已经存在的就不会被替换
print(dic03)

print(dic03.keys())
print('----------')
for keyMan in dic03.keys():
    print(keyMan)
print('-----------------')
for valueMen in dic03.values():
    print(valueMen)
print('--------------------------------------')

for key, value in dic03.items():
    itemMan = (key, value)
    print(itemMan)

print('=======================')

for item in dic03:
    print(item)
    print(dic03[item])
    print('+++++++++++++')








