from asciimatics.event import KeyboardEvent
from asciimatics.screen import Screen

from constants import Direction


class NormalInputHandler:
    def __init__(self) -> None:
        self._valid_input = {
            ord("w"): Direction.UP,
            ord("s"): Direction.DOWN,
            ord("a"): Direction.LEFT,
            ord("d"): Direction.RIGHT,
            # Arrow keys
            Screen.KEY_UP: Direction.UP,
            Screen.KEY_DOWN: Direction.DOWN,
            Screen.KEY_LEFT: Direction.LEFT,
            Screen.KEY_RIGHT: Direction.RIGHT,
        }

    @property
    def valid_input(self):
        return self._valid_input

    def get_direction(self, screen: Screen) -> Direction:
        while True:
            screen.wait_for_input(50)
            ev = screen.get_event()
            if (
                isinstance(ev, KeyboardEvent)
                and ev.key_code in self.valid_input
            ):
                return self.valid_input[ev.key_code]
