#  这是关于列表的一些coding
lst01 = ['hanxinjiang', 'pku', 'cces', 'shanxi', 'friends', 'shuangyushu']
print(lst01[0])
print(lst01[3])

lst01[3] = 'shuozhou'  # 列表的元素是可以用于修改的
print(lst01)
print(lst01[1:3])
print(lst01[:4])
print('-------')
lst01.append('beijing')
print(lst01)

# lst02 = []
# while True:
#     contentInput = input("please input your information, and input Q to quit")
#     if contentInput.upper() == 'Q':
#         break
#     lst02.append(contentInput)
# print(lst02)

print('-=-----------')
lst01.insert(2, 'student')
print(lst01)
#
# lst01.extend(['pku', 'peking University'])
# print(lst01)
#
#
print('----------')
for ele in lst01:
    print(ele)

countPku = lst01.count('pku')
print('pku出现的次数是：', countPku)
print('-------------')
lst01.reverse()
print(lst01)
print('--------')
length01 = len(lst01)
print(length01)
print('-------------------')
lst02 = ['shanxi', 'beijing', 'shanghai', ['pku', 'sichuanUniversity', ['hxj', 'what'], 'xmu'], 'guangdong']
print(lst02[3])
print(lst02[1])
print(lst02[3][2])
print(lst02[1])
str01 = lst02[1]
str01 = str01.capitalize()
print(str01)
lst02[1] = str01
print(lst02)
print('------------------------')

lst02[2] = lst02[2].capitalize()
print(lst02)

lst02[0] = lst02[0].replace('shanxi', 'shuozhou')
print(lst02)

print(lst02.count('Shanghai'))

print('--------')
# range 的用法
for num in range(10):
    print(num)

print('----------')
for num02 in range(19, 88, 2):
    print(num02)

# 用range实现1-2+3...
sum = 0

for key in range(1, 101):
    if key % 2 == 0:
        sum = sum - key
    else:
        sum = sum + key
print(sum)


