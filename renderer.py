from asciimatics.screen import Screen
from asciimatics.constants import COLOUR_GREEN, A_BOLD

from tile_map import TileMap


class Renderer:
    def __init__(self, screen: Screen, tile_map: TileMap) -> None:
        self.screen = screen
        self.tile_map = tile_map

    def render(self) -> None:
        self.screen.clear()
        for y, row in enumerate(self.tile_map.map):
            self.screen.print_at(str(row), 0, y + 1, COLOUR_GREEN, A_BOLD)
        self.screen.refresh()
