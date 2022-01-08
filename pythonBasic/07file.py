
# homework 01
num01 = input('please input a number hundreds:')
res01 = int(num01[0])**3 + int(num01[1])**3 + int(num01[2])**3
if int(num01) == res01:
    print("这是一个水仙花数")
else:
    print('这不是一个水仙花树')

# 交税问题
salary = int(input('please input your salary:'))
if salary > 2000:
    if salary > 4000:
        if salary > 6000:
            if salary > 10000:
                tax = (salary - 10000)*0.2 + 4000*0.08 + 2000*0.05 + 2000*0.03
            else:
                tax = (salary -4000)*0.08 + 2000*0.05 + 2000*0.03
        else:
            tax = (salary -4000)*0.05 + 2000*0.3
    else:
        tax = (salary - 2000)*0.03
else:
    tax = 0
print(tax)


# 这是关于文件的一些操作

file01 = open('../file02', mode='r', encoding='utf-8')
content = file01.read(2)
print(content)
content03 = file01.read(3)
print(content03)
file02 = open('../file02', mode='rb')
content02 = file02.read(1)
print(content02)
print('=============******================')
file03 = open('../helloworld.txt', mode='r', encoding='utf-8')
content04 = file03.readline()
content05 = file03.readline()
print(content04.strip())
print(content05)
print('=============******================')

for line in file03:
    print(line.strip())


file04 = open('../helloworld.txt', mode='a', encoding='utf-8')
file04.write('这是新加入的一些东西在pycharm里边\n')
file04.flush()

file04.close()
print('=============******================')
print(file03.tell())
print(file03.read())

file03.close()








