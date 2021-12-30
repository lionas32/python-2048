import numpy as np
import random

from constants import Direction


class TileMap:
    def __init__(self, size: int) -> None:
        self.size = size
        self.map = np.zeros((size, size))
        self.spawn_2_at_empty_pos()

    def spawn_2_at_empty_pos(self) -> None:
        y, x = random.choice(np.argwhere(self.map == 0))
        if random.random() < 0.9:
            self.map[y, x] = 2
        else:
            self.map[y, x] = 4

    def move_direction(self, direction: Direction) -> None:
        did_move = False
        if direction == Direction.RIGHT:
            did_move = self.move_right()
        elif direction == Direction.LEFT:
            did_move = self.move_left()
        elif direction == Direction.UP:
            did_move = self.move_up()
        elif direction == Direction.DOWN:
            did_move = self.move_down()
        if did_move:
            self.spawn_2_at_empty_pos()

    def move_left(self) -> bool:
        self.map = np.flip(self.map, axis=1)
        did_move = self.move_right()
        self.map = np.flip(self.map, axis=1)
        return did_move

    def move_down(self) -> bool:
        self.map = np.transpose(self.map)
        did_move = self.move_right()
        self.map = np.transpose(self.map)
        return did_move

    def move_up(self) -> bool:
        self.map = np.rot90(self.map, 1, (1, 0))
        did_move = self.move_right()
        self.map = np.rot90(self.map, 1, (0, 1))
        return did_move

    def move_right(self) -> bool:
        did_move = False
        for row in self.map:
            if self.move_one_row(row):
                did_move = True
            if self.combine_right(row):
                did_move = True
        return did_move

    def combine_right(self, row: np.ndarray) -> bool:
        did_move = False
        for i in reversed(range(1, len(row))):
            if row[i] == row[i - 1] and row[i] != 0:
                row[i] += row[i - 1]
                row[i - 1] = 0
                self.move_one_row(row)
                did_move = True
        return did_move

    def move_one_row(self, row: np.ndarray) -> bool:
        did_move = False
        if not np.all(row == 0):
            for i in reversed(range(1, len(row))):
                if row[i] == 0:
                    pos_where_non_null = np.argwhere(row[:i] != 0)
                    if pos_where_non_null.size == 0:
                        return did_move
                    last_non_null = pos_where_non_null[-1][0]
                    row[: i + 1] = np.concatenate(
                        (np.zeros(i - last_non_null), row[: last_non_null + 1])
                    )
                    did_move = True
        return did_move
