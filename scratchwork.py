# def diff21(n):
#   if n > 21:
#     return(2*(n-21))
#   else:
#     return (21-n)
#
#   def parrot_trouble(talking, hour):
#       return ((hour<7 or hour >20) and talking)
#
#       def makes10(a, b):
#         return(( a==10 or b==10 ) or a+b==10)
#
#         def near_hundred(n):
#           return (abs(100- n) <= 10 or abs(200-n) <=10)
#
#           def pos_neg(a, b, negative):
#   if negative:
#     return (a < 0 and b < 0)
#   else:
#     return ((a < 0 and b > 0) or (a > 0 and b < 0))
#
#     def not_string(str):
#   if 'not' in str[:3]:
#     return (str)
#   else:
#     return( 'not ' + str)
#
#     def missing_char(str, n):
#       front = str[:n]
#       back = str[n+1:]
#       return front + back


# animal = 'Aardvark'
#
# for letter in animal:
#     print(letter)

# aList = [3,-2,1,2]
# for item in aList:
#     print(item*2)

# word = 'Aardvark'
# a = 0
# for letter in word:
#     if letter == 'a' or letter == 'A':
#         a+=1
# print(a)

#with .lower method
# word = 'Aardvark'
# a = 0
# for letter in word:
#     if str.lower(letter) == 'a':
#         a+=1
# print(a)

# lower = 0
# upper = 0
# other = 0
# word = str(input('enter a phrase '))
# for letter in word:
#     if ord(letter)  >= 65 and ord(letter) <= 90:
#         upper+=1
#     elif ord(letter)  >= 97 and ord(letter) <= 122:
#         lower+=1
#     else:
#         other+=1
# print(lower,'lower', upper, 'upper', other, 'other')

# lower = 0
# upper = 0
# other = 0
# word = str(input('enter a phrase '))
# for letter in word:
#     if ord(letter)  <= ord('z') and ord(letter) >= ord('a'):
#         lower+=1
#     elif ord(letter)  >= ord('A') and ord(letter)  <= ord('Z'):
#         upper+=1
#     else:
#         other+=1
# print(lower,'lower', upper, 'upper', other, 'other')

# y = 8
# total = 0
# for i in range(y):
#     total += y
#     print(total)

# print(bin(6)[:] )
# print(bin(6)[::-1] )
# print('{0:08b}'.format(6)[::-1])
# print ( int('{0:08b}'.format(6)[::-1]), 2)
#
# x ='{0:08b}'.format(6)[::-1]
#
# print(int(x,2))


# x = 127
# y = 63
# num1 = list(str('{0:08b}'.format(x)[::-1]))
# num2 = list(str('{0:08b}'.format(y)[::-1]))
# carry = [0]
# answer = []
# for i in range(len(num1)):
#     if num1[i] == '0' and num1[i] == num2[i] == carry[i]:
#         answer.append('0')
#         carry.append('0')
#     elif num1[i] == '1' and num1[i] == num2[i] == carry[i]:
#         answer.append('1')
#         carry.append('1')
#     elif (num1[i] == '1' and num2[i] == '1') or (num1[i] == '1' and carry[i] == '1') or (num2[i] == '1' and carry[i] == '1'):
#         answer.append('0')
#         carry.append('1')
#     elif num1[i] == '1' or num2[i] == '1' or carry[i] == '1':
#         carry.append('0')
#         answer.append('1')
# print(int(''.join(answer)[::-1],2))


# x = 127
# y = 63
#
# num1 = list(str('{0:08b}'.format(x)[::-1]))
# num2 = list(str('{0:08b}'.format(y)[::-1]))
# carry = [0]
# answer = []
#
# for i in range(len(num1)):
#     if num1[i] == '0' and num1[i] == num2[i] == carry[i]:
#         print('zero')
#         answer.append('0')
#         carry.append('0')
#     elif num1[i] == '1' and num1[i] == num2[i] == carry[i]:
#         print('one carry one')
#         answer.append('1')
#         carry.append('1')
#     elif (num1[i] == '1' and num2[i] == '1') or (num1[i] == '1' and carry[i] == '1') or (num2[i] == '1' and carry[i] == '1'):
#         print('zero carry one')
#         answer.append('0')
#         carry.append('1')
#     elif num1[i] == '1' or num2[i] == '1' or carry[i] == '1':
#         print('one')
#         carry.append('0')
#         answer.append('1')
#
#
# print('\n',''.join(num1), 'plus', ''.join(num2), 'equals', ''.join(answer) )
#
# print('or', int(''.join(answer)[::-1],2))

# def swapHalves(x):
#     return str(x)[int((len(x)/2)):int(len(x)):] + str(x)[0:int((len(x)/2)):]
# print(swapHalves("hippos"))
#
#
# def firstLast(x):
#     first = str(x)[0:1:]
#     last = str(x)[int(len(x)-1)::]
#     return  'the first letter of '+x+' is ' + first + ' and the last letter is ' + last
# print(firstLast("gucci"))
#
#
# def charList(x):
#     list = []
#     for i in x:
#         list.append(i)
#     return print(list)
# charList("gucci")
#
#
# import string
# def numDigits(x):
#     digits = 0
#     for i in x:
#         if i in string.digits:
#             digits += 1
#     return digits
# print(numDigits("ripx2018"))
#
#
# def abba(x):
#     str = []
#     for i in x:
#         if i in string.ascii_letters:
#             str.append('a')
#         else:
#             str.append('b')
#     return print(''.join(str))
# abba("yuh234gg!")
#
#
# def check(x):
#     digits = 0
#     floats = 0
#     booleans = 0
#     strings = 0
#     for i in range(len(x)):
#         if isinstance(x[i], bool):
#             booleans += 1
#         elif isinstance(x[i], str):
#             strings += 1
#         elif isinstance(x[i], float):
#             floats += 1
#         elif isinstance(x[i], int):
#             digits += 1
#     return print('there are ' + str(booleans) + ' booleans ' + str(strings) + ' strings ' + str(digits) + ' digits '+ str(floats)+ ' floats ')
#
# check([True, True ,16.0, 16, 'hello', 23, False, 34])

# def getEvens(aList):
#     evens = []
#     for i in range(len(aList)):
#         if aList[i] % 2 == 0:
#             evens.append(aList[i])
#     return print(evens)
# getEvens([3,4,4,2,5,6,45,7,65,7,66])

# def numberString(num):
#     numlist = ""
#     for i in range(int(num)):
#         numlist+=(str(i+1))
#     return numlist
# print(numberString(9))
#
# def hill(n):
#     numlist = ""
#     for i in range(int(n+1)):
#         numlist+=(str(i)*i)+('\n')
#     return numlist
# print(hill(9))
#
# def valley(n):
#     numlist = ""
#     for i in range(int(n+1)):
#         numlist+=((str(i)*i)+(str(' '*((2*n)-(2*i))))+(str(i)*i)+('\n'))
#     return (numlist)
# print(valley(9))
#
#
# def endsZero(aList):
#     numzero = 0
#     for i in aList:
#         if i % 10 == 0:
#             numzero+=1
#     return numzero
# print(endsZero([3000,90,324,234,2,4]))
#
#
# def countLengths(litsOfLists):
#     numlist = []
#     for i in range(len(litsOfLists)):
#         numlist.append(len(litsOfLists[i]))
#     return numlist
# print(countLengths([[3,4,2],[],[90,23,234,True]]))
#
#
# def findAverages(numLists):
#     numlist = []
#     for i in range(len(numLists)):
#         avg = 0
#         for ii in numLists[i]:
#             avg += ii
#         numlist.append(avg/len(numLists[i]))
#     return numlist
# print(findAverages([[3,4,2],[3,3],[9]]))

# def makeID(infoList):
#     idfile = open(infoList[0] + infoList[1] + 'ID.txt', 'w')
#     idfile.write('Name: ' + infoList[1] + ', ' + infoList[0]+'\nAge: ' + infoList[2]+ '\nOccupation: ' + infoList[3])
#     idfile.close()
#
#
#
# ids = [ ['Alexander','Swann', '15', 'Student'], ['Jahseh', 'Onfroy', '20', 'rapper']]
#
# print(list[0][1])

# def makeID(infoList):
#     for i in range(len(infoList)):
#         idfile = open(infoList[i][0] + infoList[i][1] + 'ID.txt', 'w')
#         idfile.write('Name: ' + infoList[i][1] + ', ' + infoList[i][0]+'\nAge: ' + infoList[i][2]+ '\nOccupation: ' + infoList[i][3])
#         idfile.close()
#
# makeID([['Alexander','Swann', '15', 'Student'], ['Jahseh', 'Onfroy', '20', 'rapper'], ['Timothy', 'Hornor', '89', 'Army'], ['Gekyume','Onfroy','3 weeks', 'religious figure']])
