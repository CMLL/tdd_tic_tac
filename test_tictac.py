# -*- coding: utf-8 -*-
"""
Practice run at TDD as if you meant it workshop by
Keith Braithwaite.
"""
from tictac import TicTac, NotInTurnError, InvalidMoveError
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

    def test_board_can_be_visualized_as_a_list_at_game_start(self):
        """
        The game board can be visualized as a list of coordinates
        at game start.
        """
        game = TicTac()
        row = [0,0,0]
        expected = [row, row, row]
        assert game.show_game_board() == expected

    def test_board_reflects_the_movement_made_by_player_one(self):
        """
        The board must reflect the movements made by each player
        after is done.
        """
        game = TicTac()
        game.player_one.make_move(1, 1)
        expected = [[0,0,0], [0, 'x', 0], [0, 0, 0]]
        assert game.show_game_board() == expected

    def test_board_does_not_let_a_move_into_occupied_space(self):
        """
        If a player tries to make a move into a space already occupied by
        another player, a error will be raised.
        """
        game = TicTac()
        game.player_one.make_move(1, 1)
        with pytest.raises(InvalidMoveError):
            game.player_two.make_move(1, 1)

    def test_a_player_cannot_make_a_move_outside_the_board(self):
        """
        If a player tries to make a move with the x coordinates
        outside of the board, then a InvalidMove exception must
        be raised.
        """
        game = TicTac()
        with pytest.raises(InvalidMoveError):
            game.player_one.make_move(3, 1)

    def test_a_player_cannot_make_a_move_outside_the_y_axis(self):
        """
        If a player tries to make a move with the y coordinates
        outside of the board, then a InvalidMove exception
        must be raises.
        """
        game = TicTac()
        with pytest.raises(InvalidMoveError):
            game.player_one.make_move(1, 3)

