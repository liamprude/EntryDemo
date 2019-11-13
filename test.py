# Write a simple Hangman program. Your game should do the following:
# - Select a random word from a list of ten words when a "START" button widget is pressed.
# - Display a sequence of dashes on a text widget. The number of dashes should correspond
#   with the number of letters in the word.
# - The user should be prompted to guess a letter. If the user's guess appears in the word,
#   the letter should replace the dash where it is located.
# - The all of the guessed letters should be displayed before each new guess.
# - The user can make six incorrect guesses before he/she dies.
# - The user wins if he/she guesses the word or if he/she correctly guess all of the letters.

from Tkinter import*
import random

root=Tk()
#### MODEL(Data and Methods) ####

wordBank = ['goat', 'seven', 'blanket', 'beanie', 'astounding', 'magazine', 'homosapien', 'icicle', 'bucket', 'wonder']

def restart(): #Start New Game. Clear board and select a new word to display. Sets 'dashes' variable to the correct number of dashes
    global term, mistakes, dashes, guesses
    dashes, guesses = '', ''
    term = random.choice(wordBank)
    for x in term:
        dashes += '- '
    mistakes = 0
    output.delete("1.0", END)
    output.insert(END, "Guess the word: "+dashes+'\n')
    output.insert(END, 'Guesses remaining: 6' + '\n')

def getGuess(): #Get guess from entry box
    guess = guessX.get()
    guessX.delete(0, END)
    guessX.insert(0, "")
    return guess

def enterGuess(): # Check guess against word. Replaces and prints dashes string with guesses
    output.delete("1.0", END)
    j = -1
    global dashes, term, guesses, mistakes
    guess = getGuess()
    guesses += guess + ', '
    check = 0
    for i in term:
        j += 1
        if guess  == term[j]:
            # reassign the index of dashes (j) times two with guess
            dashes = dashes[:j * 2] + guess + dashes[(j * 2)+1:]
            check = 1
    output.insert(END, dashes + "\n")
    output.insert(END, 'Your previous guesses were: '+guesses+"\n")
    if check == 0:
        mistakes += 1
    output.insert(END, 'Guesses remaining: '+ str(6-mistakes)+"\n")
    output.insert(END, mistakeCount())

def mistakeCount(): #Keep track of how many guesses there have been, keep a list of previous guesses to display
    if mistakes >= 6:
        return 'You Lose! The word was '+ term + '!'
    elif '-' not in dashes:
        return 'You win! Congratulations!'
    else:
        return '\n'

#### CONTROLLER(Buttons and Entry Widgets) ####

begin = Button(root, fg="black", text="Start Game", command=restart)
begin.grid(row="1", column="0")

submit = Button(root, fg="black", text="Enter Guess", command=enterGuess)
submit.grid(row="1", column="1")

guessX = Entry(root, fg="black")
guessX.grid(row=1, column="2")

### VIEW (Text Widget)####
title = Label(root, fg="black", text="H A N G M A N")
title.grid(row="0", column="1")

output = Text(root, fg="black")
output.grid(row="2", column="0", rowspan="2", columnspan="3")
root.mainloop()