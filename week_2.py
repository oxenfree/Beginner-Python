import random


def roll_dice():
    return random.randint(1, 6)

dealer_hand = []
player_hand = []

print('Welcome to this dice game.')

for i in range(3):
    dealer_hand.append(roll_dice())

for i in range(2):
    player_hand.append(roll_dice())

print('Dealer got:')
for die in dealer_hand:
    print(die)

print('You got.')
for die in player_hand:
    print(die)

matches = 0

for die in dealer_hand:
    if die == player_hand[0]:
        matches = matches + 1
    if die == player_hand[1]:
        matches += 1

print('You got', matches, 'matches.')

if matches > 0:
    print('You won!')
else:
    print('You lost.')
