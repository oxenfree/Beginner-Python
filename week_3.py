import random

print('Welcome to the dice game.')


def roll_die():
        return random.randint(1, 6)

dealer_hand = []
player_hand = []
matched_die = []


for i in range(2):
        player_hand.append(roll_die())

for i in range(5):
        dealer_die = roll_die()
        dealer_hand.append(dealer_die)

matches = 0

for current_die in player_hand:
        if current_die in dealer_hand:
                matched_die.append(current_die)
                matches = matches + 1

print(f'You got {matches} matches.')
print(matched_die)
