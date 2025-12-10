import unittest

from custom_types.direction import Direction
from services.board import Board
from services.game_controller import GameController

class TestGameController(unittest.TestCase):
    def test_move_left_single_column_combine(self):
        board = Board()
        board.values = [
            [2, 2, None, None],
            [None, None, None, None],
            [None, None, 4, None],
            [None, 8, None, None]
        ]

        game_controller = GameController(board)
        latest_board, changes = game_controller.move(direction=Direction.LEFT, dry_run=False)

        expected = [
            [4, None, None, None],
            [None, None, None, None],
            [4, None, None, None],
            [8, None, None, None]
        ]

        self.assertEqual(
            expected, latest_board.values
        )

        self.assertTrue(changes)

    def test_move_left_no_changes(self):
        board = Board()
        board.values = [
            [2, None, None, None],
            [None, None, None, None],
            [4, 16, None, None],
            [8, 32, None, None]
        ]

        game_controller = GameController(board)
        latest_board, changes = game_controller.move(direction=Direction.LEFT, dry_run=False)

        expected = [
            [2, None, None, None],
            [None, None, None, None],
            [4, 16, None, None],
            [8, 32, None, None]
        ]

        self.assertEqual(
            expected, latest_board.values
        )

        self.assertFalse(changes)

    def test_move_left_multi_row_combine(self):
        board = Board()
        board.values = [
            [2, None, None, 2],
            [4, None, 4, None],
            [8, 8, 8, None],
            [16, 16, None, None]
        ]

        game_controller = GameController(board)
        latest_board, changes = game_controller.move(direction=Direction.LEFT, dry_run=False)

        expected = [
            [4, None, None, None],
            [8, None, None, None],
            [16, 8, None, None],
            [32, None, None, None]
        ]

        self.assertEqual(
            expected, latest_board.values
        )

        self.assertTrue(changes)


    def test_move_right_single_column_combine(self):
        board = Board()
        board.values = [
            [2, None, 2, 2],
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None]
        ]

        game_controller = GameController(board)
        latest_board, changes = game_controller.move(direction=Direction.RIGHT, dry_run=False)

        expected = [
            [None, None, 2, 4],
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None]
        ]

        self.assertEqual(
            expected, latest_board.values
        )

        self.assertTrue(changes)

    def test_move_right_multi_row_combine(self):
        board = Board()
        board.values = [
            [2, None, None, 2],
            [4, None, 4, None],
            [8, 8, 8, None],
            [16, 16, None, None]
        ]

        game_controller = GameController(board)
        latest_board, changes = game_controller.move(direction=Direction.RIGHT, dry_run=False)

        expected = [
            [None, None, None, 4],
            [None, None, None, 8],
            [None, None, 8, 16],
            [None, None, None, 32]
        ]

        self.assertEqual(
            expected, latest_board.values
        )

        self.assertTrue(changes)

    def test_move_right_two_combines(self):
        board = Board()
        board.values = [
            [2, 2, 2, 2],
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None]
        ]

        game_controller = GameController(board)
        latest_board, changes = game_controller.move(direction=Direction.RIGHT, dry_run=False)

        expected = [
            [None, None, 4, 4],
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None]
        ]

        self.assertEqual(
            expected, latest_board.values
        )

        self.assertTrue(changes)

    def test_move_up_single_combine(self):
        board = Board()
        board.values = [
            [2, None, None, 2],
            [2, None, 2, None],
            [None, None, None, None],
            [None, None, None, None]
        ]

        game_controller = GameController(board)
        latest_board, changes = game_controller.move(direction=Direction.UP, dry_run=False)

        expected = [
            [4, None, 2, 2],
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None]
        ]

        self.assertEqual(
            expected, latest_board.values
        )

        self.assertTrue(changes)

    def test_move_up_multi_rowcombine(self):
        board = Board()
        board.values = [
            [2, None, None, None],
            [2, None, 4, 8],
            [None, None, None, 8],
            [None, None, 4, None]
        ]

        game_controller = GameController(board)
        latest_board, changes = game_controller.move(direction=Direction.UP, dry_run=False)

        expected = [
            [4, None, 8, 16],
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None]
        ]

        self.assertEqual(
            expected, latest_board.values
        )

        self.assertTrue(changes)

    def test_move_down_single_combine(self):
        board = Board()
        board.values = [
            [2, None, None, 2],
            [2, None, 2, None],
            [None, None, None, None],
            [None, None, None, None]
        ]

        game_controller = GameController(board)
        latest_board, changes = game_controller.move(direction=Direction.DOWN, dry_run=False)

        expected = [
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
            [4, None, 2, 2]
        ]

        self.assertEqual(
            expected, latest_board.values
        )

        self.assertTrue(changes)

    def test_move_down_multi_row_combine(self):
        board = Board()
        board.values = [
            [2, None, None, None],
            [2, None, 4, 8],
            [None, None, None, 8],
            [None, None, 4, None]
        ]

        game_controller = GameController(board)
        latest_board, changes = game_controller.move(direction=Direction.DOWN, dry_run=False)

        expected = [
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
            [4, None, 8, 16]
        ]

        self.assertEqual(
            expected, latest_board.values
        )

        self.assertTrue(changes)
