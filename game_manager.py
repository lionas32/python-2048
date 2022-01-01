from asciimatics.screen import Screen
from constants import Action

from input_handler import NormalInputHandler
from renderer import Renderer
from tile_map import TileMap
from score import Score


class GameManager:
    def __init__(
        self,
        tilemap: TileMap,
        input_handler: NormalInputHandler,
        screen: Screen,
    ) -> None:
        self.tilemap = tilemap
        self.renderer = Renderer(screen, tilemap, cell_width=5)
        self.input_handler = input_handler

    def render(self) -> None:
        self.renderer.screen.clear_buffer(
            Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_DEFAULT
        )
        self.renderer.render_map()
        self.renderer.render_score()
        self.renderer.render_highscore()
        self.renderer.screen.refresh()

    def perform_action(self, action: Action) -> Action:
        if action == Action.QUIT:
            Score.overwrite_highscore()
            return action
        else:
            score = self.tilemap.move_direction(action)
            Score.add_points(score)
            return action

    def run(self) -> bool:
        action = self.input_handler.get_action(self.renderer.screen)
        new_action = self.perform_action(action)
        if new_action == Action.QUIT:
            return False
        return True
