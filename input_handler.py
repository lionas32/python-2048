from asciimatics.event import KeyboardEvent
from asciimatics.screen import Screen

from constants import Direction


class NormalInputHandler:
    def __init__(self) -> None:
        self.valid_input = {
            ord("w"): Direction.UP,
            ord("s"): Direction.DOWN,
            ord("a"): Direction.LEFT,
            ord("d"): Direction.RIGHT,
            # ARROW KEYS (these should probably not be enabled by default, are probably OS dependent)
            -204: Direction.UP,
            -206: Direction.DOWN,
            -203: Direction.LEFT,
            -205: Direction.RIGHT,
        }

    def get_direction(self, screen: Screen) -> Direction:
        while True:
            screen.wait_for_input(50)
            ev = screen.get_event()
            if isinstance(ev, KeyboardEvent) and ev.key_code in self.valid_input:
                return self.valid_input[ev.key_code]
