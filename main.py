from asciimatics.screen import Screen
from game_manager import GameManager

from tile_map import TileMap
from input_handler import NormalInputHandler


def main(screen: Screen) -> None:
    size = 4
    tile_map = TileMap(size=size)
    input_handler = NormalInputHandler()
    game_manager = GameManager(tile_map, input_handler, screen)
    keep_running = True
    while keep_running:
        game_manager.render()
        keep_running = game_manager.run()


if __name__ == "__main__":
    Screen.wrapper(main, unicode_aware=True)
