from asciimatics.screen import Screen

from tile_map import TileMap
from renderer import Renderer
from input_handler import NormalInputHandler
from score import Score
from constants import Action


def main(screen: Screen) -> None:
    size = 4
    tile_map = TileMap(size=size)
    input_handler = NormalInputHandler()
    renderer = Renderer(screen, tile_map)
    tile_map_x = screen.width // 2 - (size * 5) // 2
    tile_map_y = screen.height // 2 - size // 2
    score_x = tile_map_x
    score_y = screen.height // 2 + size // 2 + 1
    while True:
        screen.clear_buffer(
            Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_DEFAULT
        )
        renderer.render_map(
            x=tile_map_x,
            y=tile_map_y,
        )
        renderer.render_score(
            x=score_x,
            y=score_y,
        )
        screen.refresh()
        direction = input_handler.get_direction(screen)
        if direction == Action.QUIT:
            return
        Score.add_points(tile_map.move_direction(direction))


if __name__ == "__main__":
    Screen.wrapper(main, unicode_aware=True)
