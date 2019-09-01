import random
################################################
############### BEGINNER #######################
################################################
deck_i = {
    'diamond': ['A', 'K', 'Q', 'J', 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'heart': ['A', 'K', 'Q', 'J', 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'club': ['A', 'K', 'Q', 'J', 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'spade': ['A', 'K', 'Q', 'J', 2, 3, 4, 5, 6, 7, 8, 9, 10]
}
#
#
#
#
#
#
#
#
#
################################################
############# INTERMEDIATE #####################
################################################
cards = [i for i in range(2, 11)]
faces = ['A', 'K', 'Q', 'J']
cards.extend(faces)
deck_ii = {
    'diamond': cards,
    'heart': cards,
    'club': cards,
    'spade': cards
}

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#


################################################
############### ADVANCED #######################
################################################

cards = []
for meow_mix in range(2, 11):
    cards.append(meow_mix)
faces = ['A', 'K', 'Q', 'J']
cards.extend(faces)
suits = ['\u2666', '\u2665', '\u2663', '\u2660']
deck_iii = {entities: cards for entities in suits}

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

print('welcome to blackjack!')
print('your first card')
suit_random = random.randint(0, 3)  # 2
card_random = random.randint(0, 12)
suit = list(deck_iii.keys())[suit_random]
card = deck_iii[suit][card_random]

# This is probably not right.
# I am fiddling with git.
print(f'Player\'s hand 1: {suit}{card}')
print(f'Player\'s hand 2: {suit}{card}')
