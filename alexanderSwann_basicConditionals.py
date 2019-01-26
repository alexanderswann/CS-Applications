#Alexander Swann
#Friday, January 25, 2019
#CS Applications

#alexanderSwann_basicConditionals

word = input("Type a word ")
number = float(input("Type a number "))
character = input("Type one letter ")

if 'sh' in word:
    print('Has sh')
if number % 7 != 0:
    print ('Not divisible by 7')
if number >= 90 and number <= 100:
    print('You got an A!')
if bool("f" in word) ^ bool("g" in word):
    print('Contains either an f or a g')
if not 'a' in word and not 'e' in word and not 'i' in word and not 'o' in word and not 'u' in word:
    print('Possibly not a real word')
if ord(character)  >= 65 and ord(character) <= 90:
    print('Is a capital letter')
if number % 3 == 0:
    if number % 2 == 0:
         print('Bazinga!')


#user input is when the user of your program inputs data and your
#program takes that data and says something about that data
#user input is important to have in your program so that the user of
#your program can interact with your program and it makes your program more useful
