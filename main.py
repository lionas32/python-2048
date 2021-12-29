from asciimatics.screen import Screen

from tile_map import TileMap
from renderer import Renderer
from input_handler import NormalInputHandler


def main(screen: Screen) -> None:
    tile_map = TileMap(4)
    input_handler = NormalInputHandler()
    renderer = Renderer(screen, tile_map)
    while True:
        renderer.render()
        direction = input_handler.get_direction(screen)
        tile_map.move_direction(direction)


if __name__ == "__main__":
    Screen.wrapper(main, unicode_aware=True)
