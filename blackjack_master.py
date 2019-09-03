import random


def get_cards():
    faces = ['A', 'K', 'Q', 'J']
    cards = [i for i in range(2, 11)]
    cards.extend(faces)

    return cards


def shuffle():
    print('shuffling deck')
    suits = ['\u2666', '\u2665', '\u2663', '\u2660']
    deck = {suit: get_cards() for suit in suits}

    return deck


def draw_a_card(_deck):
    suit_random = random.randint(0, 3)
    _suit = list(_deck.keys())[suit_random]
    card_random = random.randint(0, len(_deck[_suit]) - 1)
    card = _deck[_suit].pop(card_random)

    return _suit, card


hit = True
player_turn = True
deck = shuffle()
hands = {
    'player': [],
    'dealer': []
}
counter = 0
while hit:
    whose_turn = 'player' if player_turn else 'dealer'
    hands['player'].append(draw_a_card(deck))
    hands['dealer'].append(draw_a_card(deck))
    counter += 1
    if counter < 2:
        continue

    print(f'dealer\'s hand: {hands["dealer"][0]}')
    print(f'player\'s hand: {hands["player"]}')
    keep_going = input('hit or stand? ')
    if 'h' not in keep_going:
        hit = False
    player_turn = not player_turn
    if len(deck[hands['dealer'][0][0]]) == 0:
        deck = shuffle()
