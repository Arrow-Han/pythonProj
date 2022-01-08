"""
python是一门解释型的语言，这样的好处就是执行效率比较高，然后可以脱离语言环境独立运行，优雅，并且明确，简单
"""

# 命名规则就是尽量用驼峰式的就可以
msg = "hanxinjaing\n"
print(msg * 8)
print('------------------------')
testBool = (88 < 34)
print(testBool)
print('------------------------')
str01 = 'hello'
str02 = '2022!'
print(str01 + str02)  # 字符串只有+这一种哦
print('----------')

# msgInput = input("请输入一个你能想到的数字")
# print(msgInput)
#
# if int(msgInput) < 23:  # 这里输入的应该是一个str类型的，所以要转化成int类型的
#     print("还是不够的")
# else:
#     print("还不错")
print('---------------------')
#  以下是属于homework
# homework01
i = 1
while i <= 10:
    print(i)
    i = i+1
print('------------')
# homework02，求和：0-100
sumZeroToOne = 0
i01 = 0
while i01 < 100:
    i01 = i01 + 1
    sumZeroToOne = sumZeroToOne + i01
    print(i01)
print(sumZeroToOne)
print('---------homework03')
# homework03 求1-00内的所有奇数和
i02 = 1
sumZeroToOne02 = 0
while i02 < 100:

    sumZeroToOne02 = sumZeroToOne02 + i02
    i02 = i02 + 2
    print(sumZeroToOne02)
print('----------homework04')
# homework04 求1-00内的所有偶数和
i03 = 0
sumZeroToOne03 = 0
while i03 < 101:

    sumZeroToOne03 = sumZeroToOne03 + i03
    i03 = i03 + 2
    print(sumZeroToOne03)
print('----------')

sumAll = sumZeroToOne02 + sumZeroToOne03
print(sumAll == sumZeroToOne)
print('--------homework05')
loopI = 0
sumLoop = 0
while loopI < 100:
    if loopI % 2 == 0:
        index = -1
        sumLoop = sumLoop - loopI
        loopI = loopI + 1
        print(str(loopI) + '这是偶数')
        print(sumLoop)
    else:
        sumLoop = sumLoop + loopI
        loopI = loopI + 1
        print(str(loopI) + '这是奇数')
        print(sumLoop)

# 格式化输出的一些东西
# 用百分号用来占位，然后在最后使用百分号加一个括号用于表明每个占位符都是填什么变量
"""
name = input('please input your name:')
age = input('please input your age:')
job = input('please input your job:')
hobby = input('please input your hobby:')

info = '''
--------info of %s---------
Name : %s
Age : %s
Job : %s
Hobby : %s
-----------end-----------
''' % (name,name,age,job,hobby)
print(info)
"""



print('--------')
print('我叫 %s 今年 %s 岁了，已经学了2%%的python' %('hanxinjiang', 22))

# 关于while的一些补充
index02 = 1
while index02 < 11:
    if index02 == 8:
        pass
    else:
        print(index02)
    index02 = index02 + 1
else:
    print('hello hanxinjiang')

# 用户登陆，用户名：hanxinjiang 密码：123456

count = 1
while count < 3:
    username = input('please input your usermane:').strip()
    password = input('please input your password:').strip()
    if username == 'hanxinjiang' and password == '123456' :
        print('successful!!!')
        break # 到这儿登陆成功就要退出循环了
    else:
        print('login fail')
    print('you have %d times' %(3 - count))
    count = count +1
else:
    print('you are so stupid!!!')


print('----------------')
print(2**16)
print('--------------')
lengthOfWord = (256).bit_length()
print(lengthOfWord)

print('---------------')










