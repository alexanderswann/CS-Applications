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


x = 127
y = 63

num1 = list(str('{0:08b}'.format(x)[::-1]))
num2 = list(str('{0:08b}'.format(y)[::-1]))
carry = [0]
answer = []

for i in range(len(num1)):
    if num1[i] == '0' and num1[i] == num2[i] == carry[i]:
        print('zero')
        answer.append('0')
        carry.append('0')
    elif num1[i] == '1' and num1[i] == num2[i] == carry[i]:
        print('one carry one')
        answer.append('1')
        carry.append('1')
    elif (num1[i] == '1' and num2[i] == '1') or (num1[i] == '1' and carry[i] == '1') or (num2[i] == '1' and carry[i] == '1'):
        print('zero carry one')
        answer.append('0')
        carry.append('1')
    elif num1[i] == '1' or num2[i] == '1' or carry[i] == '1':
        print('one')
        carry.append('0')
        answer.append('1')


print('\n',''.join(num1), 'plus', ''.join(num2), 'equals', ''.join(answer) )

print('or', int(''.join(answer)[::-1],2))
