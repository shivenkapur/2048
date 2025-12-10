import unittest
from custom_types.round_result import RoundResult
from services.board import Board
from services.game import Game
from services.game_controller import GameController
from readchar import key

class TestGame(unittest.TestCase):
    def test_win(self):
        board = Board()
        game_controller = GameController(board)

        game = Game(game_controller)

        board.values = [
            [2, 2, None, None],
            [None, 32, None, None],
            [None, 1024, None, 8],
            [None, 1024, 16, None]
        ]

        actual_result, _ = game.start_round(key.UP)
        expected_result = RoundResult.WON

        self.assertEqual(
            expected_result, actual_result
        )

    def test_lost(self):
        board = Board()
        game_controller = GameController(board)

        game = Game(game_controller)

        board.values = [
            [2, 4, 8, 16],
            [4, 2, 4, 8],
            [2, 4, 8, 16],
            [4, 2, 4, 8],
        ]

        actual_result, _ = game.start_round(key.UP)
        expected_result = RoundResult.LOST

        self.assertEqual(
            expected_result, actual_result
        )

    def test_wrong_input(self):
        board = Board()
        game_controller = GameController(board)

        game = Game(game_controller)

        board.values = [
            [2, 4, 8, 16],
            [4, 2, 4, 8],
            [2, 4, 8, 16],
            [4, 2, 4, 8],
        ]

        actual_result, _ = game.start_round(key.BACKSPACE)
        expected_result = RoundResult.WRONG_INPUT

        self.assertEqual(
            expected_result, actual_result
        )

    def test_continue(self):
        board = Board()
        game_controller = GameController(board)

        game = Game(game_controller)

        board.values = [
            [2, 4, 8, 16],
            [4, 2, 4, 4],
            [2, 4, 8, 16],
            [4, 2, 4, 8],
        ]

        actual_result, _ = game.start_round(key.RIGHT)
        expected_result = RoundResult.CONTINUE

        self.assertEqual(
            expected_result, actual_result
        )
