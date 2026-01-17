import unittest
from custom_types.direction import Direction
from services.board import Board
from services.merge_algorithm import MergeAlgorithm

def _get_board_values_with_row(row):
    return [
        row
    ] + [[None, None, None, None]] * 3

class TestMergeAlgorithm(unittest.TestCase):
    def test_move_left_occupy_empty_spot(self):
        board = Board()
        board.values = _get_board_values_with_row(
            [None, 2, None, None]
        )

        merge_algorithm = MergeAlgorithm(board, dry_run=False)
        latest_board = merge_algorithm.merge_horizontal(
            reverse=False
        )
        actual = latest_board.values

        expected = _get_board_values_with_row(
            [2, None, None, None]
        )

        self.assertEqual(
            expected, actual
        )

    def test_move_values_multiple_cells(self):
        board = Board()
        board.values = _get_board_values_with_row(
            [None, None, None, 2]
        )

        merge_algorithm = MergeAlgorithm(board, dry_run=False)
        latest_board = merge_algorithm.merge_horizontal(
            reverse=False
        )
        actual = latest_board.values

        expected = _get_board_values_with_row(
            [2, None, None, None]
        )

        self.assertEqual(
            expected, actual
        )

    def test_single_column_combine(self):
        board = Board()
        board.values = _get_board_values_with_row(
            [2, 2, None, None]
        )

        merge_algorithm = MergeAlgorithm(board, dry_run=False)
        latest_board = merge_algorithm.merge_horizontal(
            reverse=False
        )
        actual = latest_board.values

        expected = _get_board_values_with_row(
            [4, None, None, None]
        )

        self.assertEqual(
            expected, actual
        )

    def test_single_column_combine_with_single_space(self):
        board = Board()
        board.values = _get_board_values_with_row(
            [2, None, 2, None]
        )

        merge_algorithm = MergeAlgorithm(board, dry_run=False)
        latest_board = merge_algorithm.merge_horizontal(
            reverse=False
        )
        actual = latest_board.values

        expected = _get_board_values_with_row(
            [4, None, None, None]
        )

        self.assertEqual(
            expected, actual
        )

    def test_single_column_combine_with_two_spaces(self):
        board = Board()
        board.values = _get_board_values_with_row(
            [2, None, None, 2]
        )

        merge_algorithm = MergeAlgorithm(board, dry_run=False)
        latest_board = merge_algorithm.merge_horizontal(
            reverse=False
        )
        actual = latest_board.values

        expected = _get_board_values_with_row(
            [4, None, None, None]
        )

        self.assertEqual(
            expected, actual
        )

    def test_single_column_combine_with_third_spot_used_for_merge(self):
        board = Board()
        board.values = _get_board_values_with_row(
            [None, 2, None, 2]
        )

        merge_algorithm = MergeAlgorithm(board, dry_run=False)
        latest_board = merge_algorithm.merge_horizontal(
            reverse=False
        )
        actual = latest_board.values

        expected = _get_board_values_with_row(
            [4, None, None, None]
        )

        self.assertEqual(
            expected, actual
        )
    
    def test_double_column_combine(self):
        board = Board()
        board.values = _get_board_values_with_row(
            [2, 2, 2, 2]
        )

        merge_algorithm = MergeAlgorithm(board, dry_run=False)
        latest_board = merge_algorithm.merge_horizontal(
            reverse=False
        )
        actual = latest_board.values

        expected = _get_board_values_with_row(
            [4, 4, None, None]
        )

        self.assertEqual(
            expected, actual
        )

    def test_merge_with_different_cell_values(self):
        board = Board()
        board.values = _get_board_values_with_row(
            [2, 4, None, None]
        )

        merge_algorithm = MergeAlgorithm(board, dry_run=False)
        latest_board = merge_algorithm.merge_horizontal(
            reverse=False
        )
        actual = latest_board.values

        expected = _get_board_values_with_row(
            [2, 4, None, None]
        )

        self.assertEqual(
            expected, actual
        )

    def test_merge_with_different_cell_values_with_space(self):
        board = Board()
        board.values = _get_board_values_with_row(
            [2, None, None, 4]
        )

        merge_algorithm = MergeAlgorithm(board, dry_run=False)
        latest_board = merge_algorithm.merge_horizontal(
            reverse=False
        )
        actual = latest_board.values

        expected = _get_board_values_with_row(
            [2, 4, None, None]
        )

        self.assertEqual(
            expected, actual
        )

    def test_merge_with_multiple_different_cell_values_with_space(self):
        board = Board()
        board.values = _get_board_values_with_row(
            [2, None, 4, 8]
        )

        merge_algorithm = MergeAlgorithm(board, dry_run=False)
        latest_board = merge_algorithm.merge_horizontal(
            reverse=False
        )
        actual = latest_board.values

        expected = _get_board_values_with_row(
            [2, 4, 8, None]
        )

        self.assertEqual(
            expected, actual
        )

    def test_merge_with_multiple_different_cell_values_right_aligned(self):
        board = Board()
        board.values = _get_board_values_with_row(
            [None, None, 4, 8]
        )

        merge_algorithm = MergeAlgorithm(board, dry_run=False)
        latest_board = merge_algorithm.merge_horizontal(
            reverse=False
        )
        actual = latest_board.values

        expected = _get_board_values_with_row(
            [4, 8, None, None]
        )

        self.assertEqual(
            expected, actual
        )

    def test_merge_all_different_values(self):
        board = Board()
        board.values = _get_board_values_with_row(
            [2, 4, 8, 16]
        )

        merge_algorithm = MergeAlgorithm(board, dry_run=False)
        latest_board = merge_algorithm.merge_horizontal(
            reverse=False
        )
        actual = latest_board.values

        expected = _get_board_values_with_row(
            [2, 4, 8, 16]
        )

        self.assertEqual(
            expected, actual
        )

    def test_combine_in_middle_rows(self):
        board = Board()
        board.values = _get_board_values_with_row(
            [2, 4, 4, 8]
        )

        merge_algorithm = MergeAlgorithm(board, dry_run=False)
        latest_board = merge_algorithm.merge_horizontal(
            reverse=False
        )
        actual = latest_board.values

        expected = _get_board_values_with_row(
            [2, 8, 8, None]
        )

        self.assertEqual(
            expected, actual
        )

    def test_combine_in_end_rows(self):
        board = Board()
        board.values = _get_board_values_with_row(
            [2, 4, 8, 8]
        )

        merge_algorithm = MergeAlgorithm(board, dry_run=False)
        latest_board = merge_algorithm.merge_horizontal(
            reverse=False
        )
        actual = latest_board.values

        expected = _get_board_values_with_row(
            [2, 4, 16, None]
        )

        self.assertEqual(
            expected, actual
        )

    def test_empty_array(self):
        board = Board()
        board.values = _get_board_values_with_row(
            [None, None, None, None]
        )

        merge_algorithm = MergeAlgorithm(board, dry_run=False)
        latest_board = merge_algorithm.merge_horizontal(
            reverse=False
        )
        actual = latest_board.values

        expected = _get_board_values_with_row(
            [None, None, None, None]
        )

        self.assertEqual(
            expected, actual
        )

    def test_merge_with_reverse_enabled(self):
        board = Board()
        board.values = _get_board_values_with_row(
            [2, None, None, 4]
        )

        merge_algorithm = MergeAlgorithm(board, dry_run=False)
        latest_board = merge_algorithm.merge_horizontal(
            reverse=True
        )
        actual = latest_board.values

        expected = _get_board_values_with_row(
            [None, None, 2, 4]
        )

        self.assertEqual(
            expected, actual
        )

    def test_merge_with_dry_run_with_changes(self):
        board = Board()
        board.values = _get_board_values_with_row(
            [2, None, None, 4]
        )

        merge_algorithm = MergeAlgorithm(board, dry_run=True)
        latest_board = merge_algorithm.merge_horizontal(
            reverse=True
        )
        actual = latest_board.values

        # Dry run should not alter board
        expected = _get_board_values_with_row(
            [2, None, None, 4]
        )

        self.assertEqual(
            expected, actual
        )

        self.assertTrue(merge_algorithm.changes)

    def test_merge_with_dry_run_with_no_changes(self):
        board = Board()
        board.values = _get_board_values_with_row(
            [2, 4, 2, 4]
        )

        merge_algorithm = MergeAlgorithm(board, dry_run=True)
        latest_board = merge_algorithm.merge_horizontal(
            reverse=True
        )
        actual = latest_board.values

        expected = _get_board_values_with_row(
            [2, 4, 2, 4]
        )

        self.assertEqual(
            expected, actual
        )

        self.assertFalse(merge_algorithm.changes)

    def test_merge_vertical(self):
        board = Board()
        board.values = [
            [2, None, None, None],
            [2, None, 4, 8],
            [None, None, None, 8],
            [None, None, 4, None]
        ]

        merge_algorithm = MergeAlgorithm(board, dry_run=False)
        latest_board = merge_algorithm.merge_vertical(
            reverse=False
        )
        actual = latest_board.values

        expected = [
            [4, None, 8, 16],
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None]
        ]

        self.assertEqual(
            expected, actual
        )

        self.assertTrue(merge_algorithm.changes)
