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

    def test_a_player_cannot_introduce_negative_values_x_axis(self):
        """
        If a player tries to make a negative move on the x coordinates
        a InvalidMove exception must be raised.
        """
        game = TicTac()
        with pytest.raises(InvalidMoveError):
            game.player_one.make_move(-1, 2)

    def test_a_player_cannot_introduce_negative_value_y_axis(self):
        """
        If a player tries to make a negative move on the y coordinates
        a InvalidMove exception must be raised.
        """
        game = TicTac()
        with pytest.raises(InvalidMoveError):
            game.player_one.make_move(1, -1)

    def test_a_newly_started_game_cannot_be_over(self):
        """
        A new game cannot be considered over.
        """
        game = TicTac()
        assert not game.is_over()

    def test_a_game_with_empty_tiles_cannot_be_over(self):
        """
        A game in which there are still empty tiles cannot be considered
        over.
        """
        game = TicTac()
        game.player_one.make_move(1, 1)
        assert not game.is_over()

    def test_a_without_empty_tiles_can_be_considered_over(self):
        """
        A game in which therer are no more empty tiles can
        be considered over.
        """
        game = TicTac()
        game.board.body = [
            ['x', 'x', 'y'],
            ['y', 'x', 'x'],
            ['x', 'y', 'x'],
        ]
        assert game.is_over()

    def test_a_player_wons_by_having_any_row_with_its_mark(self):
        """
        The first player can win by having any row complete
        with its mark.
        """
        game = TicTac()
        game.board.body = [
            ['x', 'x', 'x'],
            ['x', 'y', 'y'],
            ['y', 'y', 'x'],
        ]
        assert game.who_won() == game.player_one

    def test_a_player_can_win_by_having_a_column_filled(self):
        """
        The player can win by having a complete column with
        its mark.
        """
        game = TicTac()
        game.board.body = [
            ['x', 'x', 'y'],
            ['y', 'x', 'y'],
            ['x', 'y', 'y'],
        ]
        assert game.who_won() == game.player_two

    def test_a_player_can_win_by_filling_a_diagonal(self):
        """
        A player can win by filling one of the two possible
        diagonals available.
        """
        game = TicTac()
        game.board.body = [
            ['x', 'x', 'y'],
            ['y', 'x', 'y'],
            ['y', 'y', 'x'],
        ]
        assert game.who_won() == game.player_one

    def test_a_player_can_win_by_filling_a_second_diagonal(self):
        """
        A player can win by filling the second diagonal.
        """
        game = TicTac()
        game.board.body = [
            ['x', 'x', 'y'],
            ['x', 'y', 'x'],
            ['y', 'x', 'y'],
        ]
        assert game.who_won() == game.player_two

    def test_a_game_without_a_clear_victor_is_a_draw(self):
        """
        A game without victor is a draw.
        """
        game = TicTac()
        game.board.body = [
            ['y', 'x', 'y'],
            ['y', 'x', 'y'],
            ['x', 'y', 'x'],
        ]
        assert game.is_a_draw()
