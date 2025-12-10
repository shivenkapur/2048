import unittest
import random

from unittest.mock import Mock, patch
from services.board import Board

class TestBoard(unittest.TestCase):
    @patch('random.randint')
    def test_initialising_board(self, randint_mock):
        randint_mock.side_effect = [3, 0, 0, 1, 2, 2, 3]

        expected = [
            [2, None, None, None],
            [None, None, None, None],
            [None, 2, None, None],
            [None, None, 2, None]
        ]

        board = Board()

        self.assertEqual(
            expected, board.values
        )

    @patch('random.randint')
    @patch('random.choices')
    def test_adding_random_value_with_value_2(self, randchoices_mock, randint_mock):
        # last value will be used for add_random_value
        randint_mock.side_effect = [3, 0, 0, 1, 2, 2, 3, 4]
        randchoices_mock.side_effect = [[2]]

        board = Board()

        board.add_random_value()

        # 2 is added on 5th empty spot (4th with 0 index)
        expected = [
            [2, None, None, None],
            [None, 2, None, None],
            [None, 2, None, None],
            [None, None, 2, None]
        ]

        self.assertEqual(
            expected, board.values
        )

    @patch('random.randint')
    @patch('random.choices')
    def test_adding_random_value_with_value_4(self, randchoices_mock, randint_mock):
        # last value will be used for add_random_value
        randint_mock.side_effect = [3, 0, 0, 1, 2, 2, 3, 4]
        randchoices_mock.side_effect = [[4]]

        board = Board()

        board.add_random_value()

        # 4 is added on 5th empty spot (4th with 0 index)
        expected = [
            [2, None, None, None],
            [None, 4, None, None],
            [None, 2, None, None],
            [None, None, 2, None]
        ]

        self.assertEqual(
            expected, board.values
        )
