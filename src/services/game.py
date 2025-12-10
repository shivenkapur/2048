from typing import Dict, Optional, Tuple
from readchar import key

from custom_types.direction import Direction
from custom_types.round_result import RoundResult
from services.game_controller import GameController

key_to_direction_map: Dict[str, Direction] = {
    key.UP: Direction.UP,
    key.DOWN: Direction.DOWN,
    key.LEFT: Direction.LEFT,
    key.RIGHT: Direction.RIGHT
}


class Game:
    def __init__(self, game_controller: GameController):
        self._game_controller = game_controller

    def start_round(self, input_key: str) -> Tuple[RoundResult, Optional[str]]:
        if input_key == "a":
            return RoundResult.CONTINUE, self._game_controller.ask_ai()

        if input_key not in key_to_direction_map.keys():
            return RoundResult.WRONG_INPUT, None

        direction = key_to_direction_map[input_key]
        board, any_changes = self._game_controller.move(
            direction=direction,
            dry_run=False
        )

        win = board.has_final_tile()

        if win:
            return RoundResult.WON, None
        elif not self._game_controller.any_possible_moves():
            return RoundResult.LOST, None
        elif any_changes:
            board.add_random_value()

        return RoundResult.CONTINUE, None
