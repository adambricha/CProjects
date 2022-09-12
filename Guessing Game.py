# Adam Bricha (U9233-5585) and Hanz Chua U26738740
# Driver - Adam(50%)
# Navigator - Hanz (50%)

# This program generates a random integer for the user to guess. This number is between 1 and 100. The user has 10 tries
# to get the value correct, if not the program will give the user the answer. If the user inputs a number smaller than
#the random value assinged to x, the program will prompt it is too low and vise versa. If the user guesses the number
#correct it will display the amount of tries it took





import random

x=random.randint(1,100)

num = int(input('Enter a number between 1 and 100 (inclusive): '))

while num <1 or num > 100:
    num = int(input('Very funny. Enter a number between 1 and 100 (inclusive): '))


for i in range(1,10):
    if num < x:
        num=(int(input('Too low. Enter another guess: ')))
    if num > x:
        num=(int(input('Too high. Enter another guess: ')))
    if num == x:
        print('You guessed it right!! You got it in ',i+1,'guesses.')
        break
else:
    print('Sorry, the number was',x)

