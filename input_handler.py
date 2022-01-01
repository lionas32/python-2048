from typing import Dict
from asciimatics.event import KeyboardEvent
from asciimatics.screen import Screen

from constants import Action


class NormalInputHandler:
    def __init__(self) -> None:
        self._valid_input = {
            ord("w"): Action.UP,
            ord("s"): Action.DOWN,
            ord("a"): Action.LEFT,
            ord("d"): Action.RIGHT,
            # Arrow keys
            Screen.KEY_UP: Action.UP,
            Screen.KEY_DOWN: Action.DOWN,
            Screen.KEY_LEFT: Action.LEFT,
            Screen.KEY_RIGHT: Action.RIGHT,
            # Exit
            ord("q"): Action.QUIT,
        }

    @property
    def valid_input(self) -> Dict[int, Action]:
        return self._valid_input

    def get_action(self, screen: Screen) -> Action:
        while True:
            screen.wait_for_input(50)
            ev = screen.get_event()
            if (
                isinstance(ev, KeyboardEvent)
                and ev.key_code in self.valid_input
            ):
                return self.valid_input[ev.key_code]
