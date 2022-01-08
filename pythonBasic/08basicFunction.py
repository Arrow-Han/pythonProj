def yuePao(girl):
    print('+++++++++-----++++++++++')

    print('open your phone')
    print('open momo')
    print('find a beautiful girl:' + girl)
    print('go? yue?')
    print('ok!')
    print('+++++++++-----++++++++++')
    return 'your yue is successful!', 'you are happy'


yuePao('g1')
yuePao('g2')
yuePao('g3')
print(yuePao('g4'))
print(type(yuePao('g5')))


def twoNum(a, b):
    if a > b:
        return a
    else:
        return b


# (num01, num02) = list(input('input two numbers:').split(','))
# maxOne = twoNum(num01, num02)
#
# print(maxOne)

maxOne = twoNum(76, 77)

print(maxOne)
print('+++++++++-----++++++++++')

lst01 = ["麻花藤", "刘嘉玲", "詹姆斯"]
def fun02():
    lst01.append('hanxinjiang')
    print(lst01)


fun02()
print(lst01)

