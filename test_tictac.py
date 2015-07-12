# -*- coding: utf-8 -*-
"""
Practice run at TDD as if you meant it workshop by
Keith Braithwaite.
"""
from tictac import TicTac, NotInTurnError
import pytest


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

    def test_player_one_cannot_make_consecutive_moves(self):
        """
        After player one has make a move it cannot attempt to
        make another one.
        """
        game = TicTac()
        game.player_one.make_move(1, 1)
        with pytest.raises(NotInTurnError) as exc_info:
            game.player_one.make_move(1, 2)
