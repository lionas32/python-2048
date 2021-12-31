from typing import List
import re
from asciimatics.screen import Screen

from tile_map import TileMap
from score import Score


def num_to_bg_colour(num):
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


def num_to_fg_colour(num):
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
    def __init__(self, screen: Screen, tile_map: TileMap) -> None:
        self.screen = screen
        self.tile_map = tile_map
        self.width = self.screen.width
        self.height = self.screen.height

    def _format_str(self, nums: List[int]):
        list_nums = [
            str(int(num) if num != 0 else " ").center(5) for num in nums
        ]
        str_nums = "‖".join(list_nums)
        return str_nums

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

    def render_map(self, x: int, y: int) -> None:
        for i, row in enumerate(self.tile_map.map):
            formatted_nums = self._format_str(row)
            self._print_row(formatted_nums, x, y + i)

    def render_score(self, x: int, y: int) -> None:
        self._print_at(f"Current score: {Score.score}", x, y)

    def render_highscore(self, x: int, y: int) -> None:
        self._print_at(f"Highscore: {Score.highscore}", x, y)
