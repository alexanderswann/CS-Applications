#Alexander Swann
#Wednesday, January 30, 2019
#CS Applications

#alexanderSwann_MoreConditionals

num = float(input('enter a number here: '))
shape = float(input('enter a number that is between 3 and 10 here: '))
char = input("Type one letter ")
month = input("type a month here ")
square = input("type a square here ")
db = float(input('enter a decibel number here: '))


if num %2 == 0:
    print("the number is even")
else:
    print("the number is odd")

if num <= 2:
    print("the dog is "+ str(10.5*num)+" years old")
else:
    print("the dog is "+ str(21+ (num-2)*4) +" years old")

if 'a' in char or 'e' in char or'i' in char or'o' in char or 'u' in char:
    print('the '+char+ ' letter is a vowel')
elif 'y' in char:
    print("that sometimes y is a vowel, and sometimes y is a consonant")
else:
    print('the letter ' +char+' is a consonant')

shapes = ["triangle","quadrilateral","pentagon","hexagon","heptagon","octagon","nonagon","decagon"]
if shape > 10:
    print("the shape is out of the range you should enter a number less than 10")
elif shape <3:
    print("the shape is out of the range you should enter a number less than 10 and more than 2")
    print("the number that you entered can't be a shape")
else:
    print(shapes[int(shape-3)])


if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month ==  "December":
    print("There are 31 days in " + month)
elif month == "February":
    print("there are 28 or 29 days in " + month)
elif month == "April" or month == "June" or month == "September" or month == "November":
    print("there are 30 days in " + month)
else:
    print("make sure that the month you typed in is spelled right and starts with a capital letter")


if db > 130:
    print("the sound is louder than a jackhammer")
elif db == 130:
    print("the sound is as loud as a jackhammer")
elif db < 130 and db >106:
    print("the sound is between the loudness of a jackhammer and a lawnmower")
elif db == 106:
    print("the sound is as lound as a lawnmower")
elif db < 106 and db >70:
    print("the sound is between the loudness of a lawnmower and an alarm clock")
elif db == 70:
    print("the sound is as loud as an alarm clock")
elif db < 70 and db > 40:
    print("the sound is between the loudness of an alarm clock and a quiet room")
elif db == 40:
    print("the sound is as loud as a quiet room")
else:
    print("the sound is quieter than a quiet room")


if (ord(square[0]) + int(square[1])) % 2 ==0:
    print("the square "+square+" is black")
else:
    print("the square "+square+" is white")
