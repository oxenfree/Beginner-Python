import random


class Deck:
    def __init__(self):
        self.faces = ['A', 'K', 'Q', 'J']
        self.suits = ['\u2666', '\u2665', '\u2663', '\u2660']
        self.shuffle()

    @property
    def cards(self):
        numerals = [i for i in range(2, 11)]
        numerals.extend(self.faces)

        return numerals

    def shuffle(self):
        new_deck = [
            f'{suit} {card}' for card in self.cards for suit in self.suits
        ]
        random.shuffle(new_deck)
        self.deck = new_deck

        return self.deck


class Participant:
    def __init__(self):
        self.hand = []

    def add_a_card(self, card):
        self.hand.append(card)

    def sum_hand(self, hand):
        total = {
            'total': 0,
            'aces': 0,
            'faces': 0
        }

        for card in hand:
            if isinstance(card[-1], int):
                total['total'] += card[-1]
            else:
                if card[-1] is 'A':
                    total['total'] += 11
                    total['aces'] += 1
                else:
                    total += 10
                    total['faces'] += 1

        return total


class Dealer(Participant):
    def __init__(self):
        super().__init__()
        new_deck_shuffle = Deck()
        self.deck = new_deck_shuffle.deck

    def draw_a_card(self):
        card = self.deck.pop()

        return card


class Player(Participant):
    def __init__(self):
        super().__init__()
        self.hand = []

    def add_a_card(self, card):
        self.hand.append(card)
