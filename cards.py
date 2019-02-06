"""
An example script to use pdb.
"""
import random


def draw_card():
    """Draws a "card"" between 1 and 10."""
    return random.randint(1, 10)


def new_game():
    """
    Starts a new game.
    """
    # when you finish with debugger delete the line below
    # this will add a break point

    # import pdb; pdb.set_trace()

    player_cards = [draw_card(), draw_card()]
    dealer_cards = [draw_card(), draw_card()]

    print('You have drawn a %s and a %s.' % tuple(player_cards))
    print('The dealer has drawn a', dealer_cards[0], 'and a hidden card.')


if __name__ == '__main__':
    # import pdb; pdb.set_trace()
    new_game()
