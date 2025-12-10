import random

from custom_types.board_values import BoardValues

LAST_TILE = 2048


class Board:
    def __init__(self):
        self._values: BoardValues = [[None] * 4 for _ in range(4)]
        self._initialise_board_with_random_values()

    @property
    def values(self) -> BoardValues:
        return self._values

    @values.setter
    def values(self, new_values: BoardValues) -> BoardValues:
        self._values = new_values
        return self._values

    def _initialise_board_with_random_values(self):
        number_of_initial_values = random.randint(1, 8)

        values_added = 0

        while values_added < number_of_initial_values:
            random_x = random.randint(0, 3)
            random_y = random.randint(0, 3)

            if self._values[random_y][random_x] is None:
                self._values[random_y][random_x] = 2
                values_added += 1

    def add_random_value(self):
        empty_values = []
        for row in range(len(self._values)):
            for column in range(len(self._values[row])):
                if self._values[row][column] is None:
                    empty_values.append((row, column))

        random_coordinate = empty_values[
            random.randint(0, len(empty_values) - 1)
        ]

        print(f"Added new value at"
              f" row {random_coordinate[0] + 1}"
              f" column {random_coordinate[1] + 1}\n")
        # 70% chance of getting a 2, 30% chance of getting a 4
        self._values[random_coordinate[0]][random_coordinate[1]] = \
            random.choices([2, 4], weights=[0.7, 0.3], k=1)[0]

    def has_final_tile(self) -> bool:
        for row_index, row in enumerate(self._values):
            for column_index in range(len(row)):
                if self._values[row_index][column_index] == LAST_TILE:
                    return True

        return False
