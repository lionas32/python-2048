from typing import Tuple
import numpy as np
import random

from constants import Direction


class TileMap:
    def __init__(self, size: int) -> None:
        self.size = size
        self.map = np.zeros((size, size))
        self._spawn_2_at_empty_pos()

    def _spawn_2_at_empty_pos(self) -> None:
        y, x = random.choice(np.argwhere(self.map == 0))
        if random.random() < 0.9:
            self.map[y, x] = 2
        else:
            self.map[y, x] = 4

    def move_direction(self, direction: Direction) -> int:
        did_move = False
        score = 0
        if direction == Direction.RIGHT:
            did_move, score = self._move_right()
        elif direction == Direction.LEFT:
            did_move, score = self._move_left()
        elif direction == Direction.UP:
            did_move, score = self._move_up()
        elif direction == Direction.DOWN:
            did_move, score = self._move_down()
        if did_move:
            self._spawn_2_at_empty_pos()
        return score

    def _move_left(self) -> Tuple[bool, int]:
        self.map = np.flip(self.map, axis=1)
        did_move, score = self._move_right()
        self.map = np.flip(self.map, axis=1)
        return did_move, score

    def _move_down(self) -> Tuple[bool, int]:
        self.map = np.transpose(self.map)
        did_move, score = self._move_right()
        self.map = np.transpose(self.map)
        return did_move, score

    def _move_up(self) -> Tuple[bool, int]:
        self.map = np.rot90(self.map, 1, (1, 0))
        did_move, score = self._move_right()
        self.map = np.rot90(self.map, 1, (0, 1))
        return did_move, score

    def _move_right(self) -> Tuple[bool, int]:
        did_move = False
        score = 0
        for row in self.map:
            if self._move_one_row(row):
                did_move = True
            did_move_after_combine, comb_score = self._combine_right(row)
            score += comb_score
            did_move = did_move or did_move_after_combine
        return did_move, score

    def _combine_right(self, row: np.ndarray) -> Tuple[bool, int]:
        did_move = False
        score = 0
        for i in reversed(range(1, len(row))):
            if row[i] == row[i - 1] and row[i] != 0:
                row[i] += row[i - 1]
                score += row[i]
                row[i - 1] = 0
                self._move_one_row(row)
                did_move = True
        return did_move, int(score)

    def _move_one_row(self, row: np.ndarray) -> bool:
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
