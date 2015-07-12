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


class Board(object):
    """
    Game board.
    """

    def is_empty(self):
        return True
