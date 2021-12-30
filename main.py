from asciimatics.screen import Screen

from tile_map import TileMap
from renderer import Renderer
from input_handler import NormalInputHandler


def main(screen: Screen) -> None:
    size = 4
    tile_map = TileMap(size=size)
    input_handler = NormalInputHandler()
    renderer = Renderer(screen, tile_map)
    while True:
        renderer.render_map(
            x=screen.width // 2 - (size * 5) // 2,
            y=screen.height // 2 - size // 2,
        )
        direction = input_handler.get_direction(screen)
        tile_map.move_direction(direction)


if __name__ == "__main__":
    Screen.wrapper(main, unicode_aware=True)
