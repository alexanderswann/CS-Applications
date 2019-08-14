wrong_guesses = ['']
guessed_letters = []
word = 'jahseh dwyane ricardo onfroy'
guessed_word = ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_']
the_prisoner = ['  ___\n  |   |\n      |\n      |\n      |\n  ____|__','  ___\n  |   |\n  0   |\n      |\n      |\n  ____|__','   ___\n   |   |\n   0   |\n   |   |\n       |\n   ____|__','   ___\n   |   |\n   0   |\n  /|   |\n       |\n   ____|__','   ___\n   |   |\n   0   |\n  /|\\  |\n       |\n   ____|__','   ___\n   |   |\n   0   |\n  /|\\  |\n  /    |\n   ____|__','   ___\n   |   |\n   0   |\n  /|\\  |\n  / \\  |\n   ____|__']
def check():
    letter= (input('enter a guess '))
    guessed_letters.append(letter)
    for i in range(len(word)):
        if word[i] == letter.lower():
            guessed_word[i] = letter.lower()
    if letter.lower() not in word:
        wrong_guesses.append(letter)
    return(' '.join(guessed_word), '\n', 'incorrect guesses ',  str(len(wrong_guesses)-1), '\n', 'guessed letters ',''.join(guessed_letters))
while len(wrong_guesses)<7 and word != ''.join(guessed_word):
    print(''.join(check()), '\n',the_prisoner[len(wrong_guesses)-1], '\n\n\n')
if len(wrong_guesses)>6:
    print('sorry you lost')
else:
    print('nice job! you won')
