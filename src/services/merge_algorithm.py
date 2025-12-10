from typing import List, Optional
from services.board import Board


class MergeAlgorithm:
    def __init__(self, board: Board, dry_run: bool):
        self._board = board
        self._dry_run = dry_run
        self._changes = False

    @property
    def board(self):
        return self._board

    @property
    def changes(self):
        return self._changes

    def merge_horizontal(self, reverse=False) -> Board:
        for row_index, row in enumerate(self._board.values):
            new_row = self._merge(row, reverse)

            if self._dry_run:
                continue

            self._board.values[row_index] = new_row

        return self._board

    def merge_vertical(self, reverse=False) -> Board:
        for column_index, _ in enumerate(self._board.values[0]):
            column = [row[column_index] for row in self._board.values]
            new_column = self._merge(column, reverse)

            if self._dry_run:
                continue

            for row_index, row in enumerate(self._board.values):
                row[column_index] = new_column[row_index]

        return self._board

    def _merge(
        self, array: List[Optional[int]],
        reverse: bool
    ) -> List[Optional[int]]:
        comparison_index = 0
        current_index = 1

        transformed_array = array[::]
        if reverse:
            transformed_array = array[::-1]

        while current_index < len(array):
            current_cell = transformed_array[current_index]
            comparison_cell = transformed_array[comparison_index]

            if comparison_index >= current_index:
                comparison_index = current_index
                current_index += 1
            elif current_cell is None:
                current_index += 1
            elif comparison_cell is None:
                transformed_array[comparison_index] = current_cell
                transformed_array[current_index] = None
                current_index += 1
                self._changes = True
            elif comparison_cell == current_cell:
                transformed_array[comparison_index] = current_cell * 2
                transformed_array[current_index] = None
                comparison_index += 1
                current_index += 1
                self._changes = True
            else:
                comparison_index += 1

        if reverse:
            return transformed_array[::-1]

        return transformed_array
