from typing import Tuple
from services.board import Board
from services.merge_algorithm import MergeAlgorithm
from custom_types.direction import Direction
from services.recommendation_engine import ask_ai_for_recommendation


class GameController:
    def __init__(self, board):
        self._board = board

    def ask_ai(self) -> str:
        response = ask_ai_for_recommendation(self._board.values)
        if response and any(
            member.value == response.upper() for member in Direction
        ):
            return response.upper()

        return "Sorry, our AI is not being able to recommend your next move."

    def move(self, direction: Direction, dry_run: bool) -> Tuple[Board, bool]:
        merge_algorithm = MergeAlgorithm(self._board, dry_run)

        if direction == Direction.LEFT:
            self._move_left(merge_algorithm)
        elif direction == Direction.RIGHT:
            self._move_right(merge_algorithm)
        elif direction == Direction.UP:
            self._move_up(merge_algorithm)
        elif direction == Direction.DOWN:
            self._move_down(merge_algorithm)

        return merge_algorithm.board, merge_algorithm.changes

    def any_possible_moves(self) -> bool:
        merge_algorithm = MergeAlgorithm(self._board, dry_run=True)

        self._move_left(merge_algorithm)
        self._move_right(merge_algorithm)
        self._move_up(merge_algorithm)
        self._move_down(merge_algorithm)

        return merge_algorithm.changes

    def _move_left(self, merge_algorithm) -> Board:
        return merge_algorithm.merge_horizontal(reverse=False)

    def _move_right(self, merge_algorithm) -> Board:
        return merge_algorithm.merge_horizontal(reverse=True)

    def _move_up(self, merge_algorithm) -> Board:
        return merge_algorithm.merge_vertical(reverse=False)

    def _move_down(self, merge_algorithm) -> Board:
        return merge_algorithm.merge_vertical(reverse=True)
