from blackjack_models import Player, Dealer, GamePlay

print('\nwelcome to blackjack.\n')
game = GamePlay()

is_first_round = True
player_hit = False
rount = 1
while game.active:
    if is_first_round:
        bet = game.get_player_bet()
        game.play_opening_round(bet)
        is_first_round = False
        continue
    else:
        player_hit = game.dealer.ask_hit_or_stand()

    if player_hit:
        game.player_hit()
        game.see_dealer_top_card()
        game.see_player_cards()
    participant, hand_total = game.dealer.evaluate_hands()

    if participant and hand_total:
        print(participant.name)
        print(participant.hand_total)
