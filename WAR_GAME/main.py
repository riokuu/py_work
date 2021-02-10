# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import war_game


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # card_deck = war_game.deck()
    # card_deck.createDeck()

    game = war_game.Game_Running()
    game.deal_cards()
    game.play_war_game()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
