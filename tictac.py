# -*- coding: utf-8 -*-
"""
Tic Tac Toe game for practicing TDD.
"""


class NotInTurnError(Exception):
    pass


class TicTac(object):
    """
    Game of Tic Tac Toe.
    """

    def __init__(self):
        self.board = Board()
        self.player_one = Player(self, 'x')
        self.last_played = None

    def show_game_board(self):
        """
        Show the current status of the game board.
        """
        return self.board.body


class Board(object):
    """
    Game board.
    """

    def __init__(self):
        self.body = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

    def is_empty(self):
        """
        Verify that the board is empty. A board is empty if all the rows
        are contain only 0.
        """
        for row in self.body:
            for column in row:
                if bool(column):
                    return False
        return True

    def place_move_in_board(self, mark, *args):
        """
        Place a move into the board with the requested mark.

        :param mark: String, unique mark.
        :param coord_x: Integer, x position.
        :param coord_y: Integer, y position.
        """
        self.body[args[0]][args[1]] = mark


class Player(object):
    """
    A tic tac player.
    """

    def __init__(self, game, mark):
        self.game = game
        self.player_mark = mark

    def _check_if_is_my_turn(self):
        """
        Validate that the last player to make a move was not me. This
        object is no cheater.
        """
        if self.game.last_played == self:
            raise NotInTurnError('Playing out of turn.')

    def _mark_my_turn_as_done(self):
        """
        Player finished making a move, so mark it as the last player
        to play and pass the turn to the other player.
        """
        self.game.last_played = self

    def make_move(self, coord_x, coord_y):
        """
        Make a move into a game board using a x,y coordinates point.

        :param coord_x: Integer, must be between 0 and 2.
        :param coord_y: Integer, must be between 0 and 2.
        """
        self._check_if_is_my_turn()
        self.game.board.place_move_in_board(self.player_mark, coord_x, coord_y)
        self._mark_my_turn_as_done()
