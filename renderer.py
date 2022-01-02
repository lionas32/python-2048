from typing import List
import re
from asciimatics.screen import Screen
from numpy import vectorize

from tile_map import TileMap
from score import Score


def num_to_bg_colour(num: int) -> int:
    BG_FALLBACK = 240
    if num == "2":
        return 223
    elif num == "4":
        return 216
    elif num == "8":
        return 209
    elif num == "16":
        return 208
    elif num == "32":
        return 202
    elif num == "64":
        return 196
    elif num.isdigit():
        return 220
    return BG_FALLBACK


def num_to_fg_colour(num: int) -> int:
    FG_FALLBACK = 15
    if num == "2":
        return 58
    elif num == "4":
        return 58
    elif num == "8":
        return 58
    elif num in ("16", "32", "64"):
        return 255
    elif num.isdigit():
        return 58
    return FG_FALLBACK


class Renderer:
    def __init__(
        self, screen: Screen, tile_map: TileMap, cell_width: int
    ) -> None:
        self.screen = screen
        self.tile_map = tile_map
        self.width = self.screen.width
        self.height = self.screen.height
        self.cell_width = cell_width
        # Positions, should maybe me moved into Score and Tilemap?
        self.map_x = screen.width // 2 - (tile_map.size * cell_width) // 2
        self.map_y = screen.height // 2 - tile_map.size // 2
        self.score_x = self.map_x
        self.score_y = screen.height // 2 + tile_map.size // 2 + 1
        self.highscore_x = self.map_x
        self.highscore_y = self.score_y + 1

    def _format_str(self, nums: List[int]):
        # TODO: Fix width, cell_width seems to grow from 3 and not 1
        list_nums = [
            str(int(num) if num != 0 else " ").center(self.cell_width)
            for num in nums
        ]
        str_nums = "‖".join(list_nums)
        return str_nums

    def reset_positions(self) -> None:
        self.map_x = (
            self.screen.width // 2
            - (self.tile_map.size * self.cell_width) // 2
        )
        self.map_y = self.screen.height // 2 - self.tile_map.size // 2
        self.score_x = self.map_x
        self.score_y = self.screen.height // 2 + self.tile_map.size // 2 + 1
        self.highscore_x = self.map_x
        self.highscore_y = self.score_y + 1

    def _print_row(self, nums: str, x: int, y: int) -> str:
        split_nums = re.findall("\d+", nums)
        i = 0
        curr_idx = 0
        while i < len(nums):
            char = nums[i]
            jump = 1
            if char.isdigit():
                char = nums[i : i + len(split_nums[curr_idx])]
                jump = len(split_nums[curr_idx])
                curr_idx += 1
            self.screen.print_at(
                char,
                x + i,
                y,
                bg=num_to_bg_colour(char),
                colour=num_to_fg_colour(char),
            )
            i += jump

    def _print_at(self, s: str, x: int, y: int):
        self.screen.print_at(s, x, y, bg=Screen.COLOUR_DEFAULT)

    def get_longest_int(self):
        lens = vectorize(lambda x: len(str(x)))
        longest_int = lens(self.tile_map.map).max()
        return longest_int

    def render_map(self) -> None:
        # TODO: Move this into a general rendering function
        longest_int = self.get_longest_int()
        if longest_int > self.cell_width:
            self.cell_width = longest_int
            self.reset_positions()
        for i, row in enumerate(self.tile_map.map):
            formatted_nums = self._format_str(row)
            self._print_row(formatted_nums, self.map_x, self.map_y + i)

    def render_score(self) -> None:
        self._print_at(
            f"Current score: {Score.score}", self.score_x, self.score_y
        )

    def render_highscore(self) -> None:
        self._print_at(
            f"Highscore: {Score.highscore}", self.highscore_x, self.highscore_y
        )
