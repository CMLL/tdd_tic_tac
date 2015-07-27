# -*- coding: utf-8 -*-
"""
Simple Tic Tac Toe game.
"""
from tictac import TicTac, NotInTurnError, InvalidMoveError
from pprint import pprint

def play():
    """
    Simple interaction with a game of tic tac toe.
    """
    print "Welcome to the game of Tic Tac Toe."
    game = TicTac()
    while not game.is_over():
        for row in game.show_game_board():
            pprint(row)
        print "Make a move: "
        try:
            input_x = int(raw_input('Position X: '))
            input_y = int(raw_input('Position Y: '))
            try:
                game.player_one.make_move(input_x, input_y)
            except NotInTurnError:
                game.player_two.make_move(input_x, input_y)
        except InvalidMoveError as error:
            print error.message
    if game.is_a_draw():
        print "Ended in a draw."
    else:
        for row in game.show_game_board():
            pprint(row)
        print 'Player {} won.'.format(game.who_won().player_mark)

if __name__ == '__main__':
    play()
