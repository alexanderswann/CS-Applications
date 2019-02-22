#Alexander Swann & Timofei Kouzmine
#Thrusday, February 14, 2019
#CS Applications

#parntercoding

def swapHalves(x):
    return str(x)[int((len(x)/2)):int(len(x)):] + str(x)[0:int((len(x)/2)):]
print(swapHalves("hippos"))


def firstLast(x):
    first = str(x)[0:1:]
    last = str(x)[int(len(x)-1)::]
    return  'the first letter of '+x+' is ' + first + ' and the last letter is ' + last
print(firstLast("gucci"))


def charList(x):
    list = []
    for i in x:
        list.append(i)
    return print(list)
charList("gucci")


import string
def numDigits(x):
    digits = 0
    for i in x:
        if i in string.digits:
            digits += 1
    return digits
print(numDigits("ripx2018"))


def abba(x):
    str = []
    for i in x:
        if i in string.ascii_letters:
            str.append('a')
        else:
            str.append('b')
    return print(''.join(str))
abba("yuh234gg!")


def check(x):
    digits = 0
    floats = 0
    booleans = 0
    strings = 0
    for i in range(len(x)):
        if isinstance(x[i], bool):
            booleans += 1
        elif isinstance(x[i], str):
            strings += 1
        elif isinstance(x[i], float):
            floats += 1
        elif isinstance(x[i], int):
            digits += 1
    return print('there are ' + str(booleans) + ' booleans ' + str(strings) + ' strings ' + str(digits) + ' digits '+ str(floats)+ ' floats ')

check([True, True ,16.0, 16, 'hello', 23, False, 34, 'ripx', 45.234])
