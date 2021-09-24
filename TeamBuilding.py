player_list = []

#Needs to be in WHILE loop incase they enter wrong input

while True:
    question = input('Would you like to add a player to the list? [yes] or [no]: ')
    
    if question == 'yes':
        name = input('Enter player name: ')
        player_list.append(name)
    elif question == 'no':
        for x in range(len(player_list)):
            print(f'{x+1} {player_list[x]}')
        break
    else:
        print('Invalid input, please try again.\n')

#Incase they choose someone who isnt on the team to be a goal keeper

def correct_number():
    try:
#Now we choose who will be the goalkeeper
        goal_keeper = int(input('Select what player number will be the goalkeeper: '))
#Make goal_keeper number list zero based index
        goal_keeper = goal_keeper - 1

        if goal_keeper <= len(player_list):    
            print(f'{player_list[goal_keeper]} is the goalkeeper!')
        else:
            raise IndexError
        
    except IndexError:
        print('There is no one on the team with that number')
        correct_number()
        
correct_number()