from asciimatics.event import Event, KeyboardEvent
import numpy as np
import random
from enum import Enum, auto
from asciimatics.screen import Screen
from asciimatics.constants import COLOUR_GREEN, A_BOLD


class Direction(Enum):
    LEFT = auto()
    RIGHT = auto()
    DOWN = auto()
    UP = auto()


valid_input = {
    ord("a"): Direction.LEFT,
    ord("d"): Direction.RIGHT,
    ord("s"): Direction.DOWN,
    ord("w"): Direction.UP,
}


class TileMap:
    def __init__(self, size) -> None:
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

    def combine_right(self, row) -> bool:
        did_move = False
        for i in reversed(range(1, len(row))):
            if row[i] == row[i - 1] and row[i] != 0:
                row[i] += row[i - 1]
                row[i - 1] = 0
                self.move_one_row(row)
                did_move = True
        return did_move

    def move_one_row(self, row) -> bool:
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


def main(screen: Screen) -> None:
    tile_map = TileMap(4)
    while True:
        screen.clear()
        for y, row in enumerate(tile_map.map):
            screen.print_at(str(row), 0, y + 1, COLOUR_GREEN, A_BOLD)
        screen.refresh()
        while not (direction := waiting_for_valid_input(screen)):
            pass
        tile_map.move_direction(direction)


def waiting_for_valid_input(screen: Screen) -> Direction:
    screen.wait_for_input(50)
    ev: Event = screen.get_event()
    if isinstance(ev, KeyboardEvent) and ev.key_code in valid_input:
        return valid_input[ev.key_code]
    else:
        return None


Screen.wrapper(main, unicode_aware=True)


if __name__ == "__init__":
    main()
