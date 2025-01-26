# random library to generate a random number.
# run a loop for 5 times
# if the user guesses outside the specifieg range -> issue a warning.
# if user guesses the number right -> terminate the loop
# define a function that will guide the user.


import random


def guess(rand_int):
    guess_int = int(input("enter a number: "))
    if(guess_int > 100 or guess_int < 0):
        print("Out of range input!")
    elif(guess_int == rand_int):
        return "match"
    elif(guess_int > rand_int):
        print("Try a smaller number!")
    elif(guess_int < rand_int):
        print("Try a larger number!")



rand_int = random.randint(0,100)
print("You will get 5 tries to guess the number (0-100)")

flag = 0
for i in range(0,5):
    ans = guess(rand_int)
    if(ans == "match"):
        flag = 1
        break

if(flag == 1):
    print("!!CONGRATULATIONS YOU GOT IT RIGHT!!")
else:
    print("Try again later :(")
    print("The right answer was:", rand_int)