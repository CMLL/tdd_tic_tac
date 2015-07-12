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

    def test_after_player_one_moves_board_is_not_empty(self):
        """
        After the player one makes a move to the board,
        then the board of the game cannot be considered empty.
        """
        game = TicTac()
        game.player_one.make_move(1, 1)
        assert not game.board.is_empty()
