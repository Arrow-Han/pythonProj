# about set 的一些东西
lst11 = ["李嘉诚", "麻花藤", "⻩海峰", "刘嘉玲"]
str11 = '_'.join(lst11)
print(str11)
print('----------')

str12 = '黄花大闺女'
str121 = '***'.join(str12)
print(str121)

print('---------------')
lst12 = [12, 14, 23, 26, 46, 48, 51, 55]
for ele01 in lst12:
    lst12.remove(ele01)
    print(lst12)
print('---------------')
print('---------------')

# for ele02 in range(0, len(lst12)):
#     del lst12[ele02]
#     print(lst12)
# 以上这种是会报错的，不行

# 需要用一个单独的列表来记录
lst13 = [12, 14, 23, 26, 46, 48, 51, 55]
delLst = []
for ele02 in lst13:
    delLst.append(ele02)
    print(delLst)
print('---------------')
for ele02 in delLst:
    lst13.remove(ele02)
    print(lst13)

print('=================----=========')
#   迭代循环的时候无法直接删除字典中的item

dicDelLst = []
dic01 = {'k1': 'alex', 'k2': 'wusir', 's1': '⾦⽼板', 's2': 'hanxinjiang'}
for item in dic01:
    if 'k' in item:
        dicDelLst.append(item)
for ele03 in dicDelLst:
    print(ele03)
    del dic01[ele03]
print(dic01)

print('----------这是一条优美的分割线-------------')

lst14 = [45, 5, "哈哈", 45, '哈哈', 50]
lst14 = list(set(lst14))
print(lst14)
print('----------这是一条优美的分割线-------------')
set01 = {"刘嘉玲", '关之琳', "王祖贤"}
set01.add('hanxinjiang')
print(set01)
print('----------***************-------------')
set01.add('张曼玉')
print(set01)
set01.remove('hanxinjiang')
set01.add('hxj-pku')
print(set01)
print('----------***************-------------')
for ele04 in set01:
    print(ele04)
print('----------***************-------------')
set02 = {"刘能", "赵四", "⽪皮⻓长⼭山"}
set03 = {"刘科⻓长", "冯乡⻓长", "⽪皮⻓长⼭山"}
print(set03 & set02)
print(set02.intersection(set03))
print('----------***************-------------')

print(set02 | set03)
print('----------***************-------------')

str21 = 'abc'
str22 = str21.join('非常牛逼')
print(str22)

lst15 = ["周杰伦", "周润发", "周星星", "马化腾", "周树人"]
delLst02 = []
for ele05 in lst15:
    if ele05.startswith('周'):
        delLst02.append(ele05)
        print(delLst02)
print('----------***************-------------')

for ele06 in delLst02:
    lst15.remove(ele06)
    print(lst15)
print('----------***************-------------')

set04 = set()
print(set04)

print('----------***************-------------')
lst17 = ["周杰伦", "周润发", "周星星", "马化腾", "周树人"]
lst16 = lst17
lst17.append('韩鑫江')
print(lst16)
print(id(lst17), id(lst16))
print('----------***************-------------')
lst18 = lst17.copy()
lst17.append('王五')
print(lst18)
print(lst17)
print(id(lst17), id(lst18))
print('----------***************-------------')

import copy

lst19 = ["超人", "七龙珠", "葫芦娃", "山中小猎人", ["金城武", "王力宏", "渣渣辉"]]
lst20 = copy.deepcopy(lst19)
lst19[4].append('韩鑫江')
print(lst19, lst20)
print(id(lst19), id(lst20))
print('----------***************-------------')
