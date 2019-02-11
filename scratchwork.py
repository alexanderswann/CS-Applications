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
#   if "not" in str[:3]:
#     return (str)
#   else:
#     return( "not " + str)
#
#     def missing_char(str, n):
#       front = str[:n]
#       back = str[n+1:]
#       return front + back


# animal = "Aardvark"
#
# for letter in animal:
#     print(letter)

# aList = [3,-2,1,2]
# for item in aList:
#     print(item*2)

# word = "Aardvark"
# a = 0
# for letter in word:
#     if letter == 'a' or letter == 'A':
#         a+=1
# print(a)

#with .lower method
# word = "Aardvark"
# a = 0
# for letter in word:
#     if str.lower(letter) == "a":
#         a+=1
# print(a)

# lower = 0
# upper = 0
# other = 0
# word = str(input("enter a phrase "))
# for letter in word:
#     if ord(letter)  >= 65 and ord(letter) <= 90:
#         upper+=1
#     elif ord(letter)  >= 97 and ord(letter) <= 122:
#         lower+=1
#     else:
#         other+=1
# print(lower,"lower", upper, "upper", other, "other")

lower = 0
upper = 0
other = 0
word = str(input("enter a phrase "))
for letter in word:
    if ord(letter)  <= ord('z') and ord(letter) >= ord("a"):
        lower+=1
    elif ord(letter)  >= ord('A') and ord(letter)  <= ord('Z'):
        upper+=1
    else:
        other+=1
print(lower,"lower", upper, "upper", other, "other")
