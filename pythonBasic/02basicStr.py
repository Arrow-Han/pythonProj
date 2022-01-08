# 字符串的一些代码
str01 = '韩鑫江在学习关于字符串的一些知识！2022年1月3日'
print(str01[3])
print(str01[-2])  # 倒数第二个

print(str01[1:6])  # 不包括第六个
print(str01[3:7:2])  # 最后的一个参数相当于步长

str02 = 'HANxiNjiANg'
str03 = str02.capitalize()
print(str02)
print(str03)

str04 = str02.lower()
print(str04)
str05 = str02.upper()
print(str05)
print('------------')
str06 = str02.swapcase() # 大小写相互转化
print(str06)

# 关于大小写转换，用于验证码的校验
# verifyCode = 'aDbV'
# userVerifyInput = input('please input your verify code:').strip()
# if userVerifyInput.upper() == verifyCode.upper():
#     print('successful!')
# else:
#     print('your input are wrong')
# print('----------------------')
str07 = 'abcdefghij'
print(str07.strip("ab"))
print('----------')
print('-------------')

str08 = str07.center(20, '*')
print(str08)

str09 = str07.replace('abc', 'hanxinjiang$$$')
print(str09)

print('----------')
str10 = 'hanxinjiang,hxj,age,pku'
listSplit = str10.split(',')
print(listSplit)

str11 = '''
student
pkuer
cup
clock
dell'''
print(str11.split('\n'))
print('---------')
str12 = 'my name is {1}, i love {0}, my age is {2}'.format('hanxinjiang','hxj',24)
str13 = 'my name is {name}, i love {who}, my age is {age}'.format(name = 'hanxinjiang',who = 'hxj',age = 24)

print(str13)
print(str12)

print('------------')
print(len(str07))
print('---------')
str14 = '大家好，我是韩鑫江，现在正在学习python的基础知识，预计一周时间学完'
indexStr = 0
while indexStr < len(str14):
    print(str14[indexStr])
    indexStr = indexStr +1
print('----------')
for c in str14:  # 把str14中的每一个值都给c
    print(c)
print('--------')
print('韩鑫江' in str14)
print('-------')
print(len(str14))




