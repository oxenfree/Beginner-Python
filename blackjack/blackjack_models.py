import random
from config import default_bankroll, house_bank, table_min, table_max


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
        self.hit = True

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
                    total['total'] += 10
                    total['faces'] += 1

        return total

    def stand(self):
        self.hit = False


class Dealer(Participant):
    def __init__(self):
        super().__init__()
        self.bank = house_bank
        self.shuffle_deck()
        self.name = 'dealer'

    def shuffle_deck(self):
        new_deck_shuffle = Deck()
        self.deck = new_deck_shuffle.deck

    def draw_a_card(self):
        card = self.deck.pop()

        return card

    def does_deck_need_shuffling(self):
        return len(self.deck) < 15

    def payout(self, player, amount):
        self.bank -= amount
        player.win(amount)

    def ask_hit_or_stand(self):
        hit = input('hit or stand? ')
        if 'h' in hit.lower():
            return True

        return False

    def call_blackjack_for_dealer(self):
        print('dealer blackjack.')
        self.game.active = False

        return False, False

    def call_dealer_bust(self):
        print('dealer bust')
        self.payout(self.game.player, self.game.player.ante)
        self.game.active = False

        return False, False

    def call_player_bust(self):
        print('player bust.')
        self.game.active = False

        return False, False

    def call_blackjack_for_player(self):
        print('player blackjack.')
        self.payout(self.game.player, self.game.player.ante * 2)
        self.game.active = False

        return False, False

    def evaluate_hands(self):
        player_hand = self.game.player.hand
        dealer_hand = self.hand

        player_sum = self.sum_hand(player_hand)
        dealer_sum = self.sum_hand(dealer_hand)

        if dealer_sum['total'] == 21:
            if len(dealer_sum.get('aces')) == 1 \
                    and len(dealer_sum.get('faces')) == 1:
                self.call_blackjack_for_dealer()

            return self, dealer_sum

        if player_sum['total'] == 21:
            if len(player_sum.get('aces')) == 1 \
                    and len(player_sum.get('faces')) == 1:
                self.call_blackjack_for_player()

            return self.game.player, player_sum

        if player_sum['total'] > 21:
            self.call_player_bust()

        if dealer_sum['total'] > 21:
            self.call_dealer_bust()


class Player(Participant):
    def __init__(self):
        super().__init__()
        self.bankroll = default_bankroll
        self.min_bet = table_min
        self.max_bet = table_max
        self.name = 'player'

    def bet(self, amount):
        self.bankroll -= amount
        self.ante = amount

    def win(self, amount):
        self.bankroll += amount


class GamePlay:
    def __init__(self):
        self.dealer = Dealer()
        self.dealer.game = self
        self.player = Player()
        self.active = True

    def play_opening_round(self, amount):
        self.player.bet(amount)
        for _ in range(2):
            self.dealer_hit()
            self.player_hit()

        self.see_dealer_top_card()
        self.see_player_cards()

    def dealer_hit(self):
        dealer_card = self.dealer.draw_a_card()
        self.dealer.add_a_card(dealer_card)

    def player_hit(self):
        player_card = self.dealer.draw_a_card()
        self.player.add_a_card(player_card)

    def see_dealer_top_card(self):
        print(f'dealer top card: \n{self.dealer.hand[0]}')

    def see_player_cards(self):
        print('your cards', sep='')
        for card in self.player.hand:
            print(card)

    def get_player_bet(self):
        valid_bet = False
        while not valid_bet:
            try:
                bet = int(input('place your bet. '))
                valid_bet = True
            except ValueError:
                print('c\'mon, you can\'t bet that.')
                print('try again.')

        return bet
