# -*- coding: utf-8 -*-
"""
Tic Tac Toe game for practicing TDD.
"""


class TicTac(object):
    """
    Game of Tic Tac Toe.
    """

    def __init__(self):
        self.board = Board()
        self.player_one = Player(self, 'x')


class Board(object):
    """
    Game board.
    """

    def __init__(self):
        row = [0, 0, 0]
        self._body = [row, row, row]

    def is_empty(self):
        """
        Verify that the board is empty. A board is empty if all the rows
        are contain only 0.
        """
        for row in self._body:
            for column in row:
                if bool(column):
                    return False
        return True

    def place_move(self, mark, *args):
        """
        Place a move into the board with the requested mark.

        :param mark: String, unique mark.
        :param coord_x: Integer, x position.
        :param coord_y: Integer, y position.
        """
        self._body[args[0]][args[1]] = mark


class Player(object):
    """
    A tic tac player.
    """

    def __init__(self, game, mark):
        self.game = game
        self.player_mark = mark

    def make_move(self, coord_x, coord_y):
        """
        Make a move into a game board using a x,y coordinates point.

        :param coord_x: Integer, must be between 0 and 2.
        :param coord_y: Integer, must be between 0 and 2.
        """
        self.game.board.place_move(self.player_mark, coord_x, coord_y)
