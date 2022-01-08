str01 = 'alex@'
str02 = 'alex@'
print(id(str02), id(str01))
print(str01 is str02)
lst01 = [11, 22, 33, 44]
lst02 = lst01[:]
print(lst02, lst02)
print(lst02 is lst01)
print(id(lst02), id(lst01))

#  第九题
str03 = '1,2,3'
str04 = str03.strip(',')
print(str04)
lst03 = []
for item in str04:
    lst03.append(item)
print(lst03)