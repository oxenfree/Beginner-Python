import random

print('welcome to blackjack!')
print('\n')


deck = {
    'diamond': ['A', 'K', 'Q', 'J', 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'heart': ['A', 'K', 'Q', 'J', 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'club': ['A', 'K', 'Q', 'J', 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'spade': ['A', 'K', 'Q', 'J', 2, 3, 4, 5, 6, 7, 8, 9, 10]
}


def draw_card():
    suit_random = random.randint(0, 3)  # 2
    card_random = random.randint(0, 12)  # 10
    suit = list(deck.keys())[suit_random]
    card = deck[suit][card_random]

    return suit, card


print('player hand!')
for i in range(2):
    suit, card = draw_card()
    print(f'{card} of {suit}s ')

print('\n')
print('dealer hand!')
for i in range(2):
    suit, card = draw_card()
    print(f'{card} of {suit}s ')
