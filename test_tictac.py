# -*- coding: utf-8 -*-
"""
Practice run at TDD as if you meant it workshop by
Keith Braithwaite.
"""
from tictac import TicTac


class TestsTicTacToe:

    def test_a_game_starts_with_a_empty_board(self):
        """
        When a new Tic Tac Toe game is created the board of the
        game must be empty.
        """
        game = TicTac()
        assert game.board.is_empty()
