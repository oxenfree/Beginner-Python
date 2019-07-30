from time import sleep
from random import randint

computer_choices = ['rock', 'paper', 'scissors']
scores = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}

print('Welcome to Rock Paper Scissors')
keep_going = True

while keep_going is True:
    # print('1')
    # sleep(1)  # stops for a second
    # print('2')
    # sleep(1)  # stops
    # print('3')
    # player_choice = input('your choice! ')
    computer_choice = computer_choices[randint(0, 2)]
    # print(f'you chose {player_choice}')
    print(f'the computer chose {computer_choice}')
    # player_score = scores[player_choice]
    # computer_score = scores[computer_choice]

    # if player_choice == 'scissors' and computer_choice == 'rock':
    #     print('computer won')
    # elif computer_choice == 'scissors' and player_choice == 'rock':
    #     print('you won!')
    # elif computer_score > player_score:
    #     print('computer won')
    # elif player_score > computer_score:
    #     print('you won!')
    # else:
    #     print('tie')

    play_game = input('do you want to play again? ')  # YES
    if 'y' in play_game.lower():  # yes
        keep_going = True
    else:
        keep_going = False
