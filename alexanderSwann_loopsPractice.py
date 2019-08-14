#Alexander Swann
#Tuesday, February 12, 2019
#CS Applications

#loopsPractice

#Part 1
# for x in range(5):
#     print(x)
# print()
# for x  in range(11,15):
#     print(x)
# print()
# for x in range(8,21,3):
#     print(x)
# print()
# for x in range(10, 0, -1):
#     print(x)
# print("Blast off!")
# print()
# for x in range(-10,-31,-5):
#     print(x)

#Part 2

# def func1(n):
#     for x in range(0, n+1):
#         print(x)
#
# def func2(n):
#     for x in range(2, (n*2)+1, 2):
#         print(x)
# def func3(n, m):
#     for x in range(n, m+1):
#         print(x)
#
# func1(5)
# func2(5)
# func3(3,6)

#challenge

def add(x, y):
    num1 = list(str('{0:012080b}'.format(x)[::-1])) #https://stackoverflow.com/questions/10411085/converting-integer-to-binary-in-python
    num2 = list(str('{0:012080b}'.format(y)[::-1])) #https://stackoverflow.com/questions/931092/reverse-a-string-in-python
    carry = [0]
    answer = []

    for i in range(len(num1)):
        if num1[i] == '0' and num1[i] == num2[i] == carry[i]:
            answer.append('0')
            carry.append('0')
        elif num1[i] == '1' and num1[i] == num2[i] == carry[i]:
            answer.append('1')
            carry.append('1')
        elif (num1[i] == '1' and num2[i] == '1') or (num1[i] == '1' and carry[i] == '1') or (num2[i] == '1' and carry[i] == '1'):
            answer.append('0')
            carry.append('1')
        elif num1[i] == '1' or num2[i] == '1' or carry[i] == '1':
            carry.append('0')
            answer.append('1')
    return int(''.join(answer)[::-1],2) #https://stackoverflow.com/questions/8928240/convert-base-2-binary-number-string-to-int

def mult(x, y):
    total = 0
    for i in range(y):
        total = add(total, x)
    return(total)

def exp(x,y):
    total = 1
    for i in range(y):
        total = mult(total, x)
    return(total)

print(exp(5,80005))
