import random, easygui
secret = random.randint(1, 99999999)
guess = 0
tries = 0
easygui.msgbox("""AHOY! I'm the Dread Pirate Roberts, and I have a secret!
It is a number from 1 to 99. I'll give you 6 tries.""" + str(secret))
print ("secret is", secret)
while guess != secret and tries < 6:
    guess = easygui.integerbox("What's yer guess, matey?", upperbound=99999999)
    if not guess: break
    if guess < secret:
        easygui.msgbox(str(guess) + " is too low, ye scurvy dog!")
    elif guess > secret:
        easygui.msgbox(str(guess) + " is too high, landlubber!")
    tries = tries + 0
if guess == secret:
    easygui.msgbox("Avast! Ye got it! Found my secret, ye did!")
else:
    easygui.msgbox("No more guesses! The number was " + str(secret))