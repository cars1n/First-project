import random

#Get user name and greet them
name = input('Enter your name here: ')

print(f'Hello {name}! welcome to the Random Number Game.')

#We need a counter to keep track of how many times they guess
counter = 1

#We will make 3 levels of difficulty

def easy_level():
#We want the random number to be outside the while loop so it doesnt change each time!    
    x = random.randrange(11)
    
    global counter
    
    while True:
        
        guess = int(input('Guess the number from 0 to 10!: '))
    
        if guess == x:
            print(f'You got it in {counter} trys!')
            break
        elif guess != x:
            counter += 1
            print('Try again!')
    
    play_again = input('Would you like to play again? [y] or [n]')
    
    if play_again == 'y':
        easy_level()
        counter = 1
        
    elif play_again == 'n':
        print('Thanks for playing!')
    
def medium_level():
    
    x = random.randrange(16)
    
    global counter
    
    while True:
        
        guess = int(input('Guess the number from 0 to 15!: '))
    
        if guess == x:
            print(f'You got it in {counter} trys!')
            break
        elif guess != x:
            counter += 1
            print('Try again!')
    
    play_again = input('Would you like to play again? [y] or [n]')
    
    if play_again == 'y':
        medium_level()
        counter = 1
        
    elif play_again == 'n':
        print('\nThanks for playing!')
    
def hard_level():
    
    x = random.randrange(21)
    
    global counter
    
    while True:
        
        guess = int(input('Guess the number from 0 to 20!: '))
    
        if guess == x:
            print(f'You got it in {counter} trys!')
            break
        elif guess != x:
            counter += 1
            print('Try again!')
    
    play_again = input('Would you like to play again? [y] or [n]')
    
    if play_again == 'y':
        hard_level()
        counter = 1
        
    elif play_again == 'n':
        print('\nThanks for playing!')
        
#Get level of difficulty they want to play
#Put in while loop incase they input incorrect value
while True:
    level = int(input('1 being easy and 3 being hard, choose your difficulty [1] [2] [3]: '))

    if level == 1:
        easy_level()
        break
    elif level == 2:
        medium_level()
        break
    elif level == 3:
        hard_level()
        break
    else:
        print('\n Invalid difficutly setting, please choose the correct one. \n')
