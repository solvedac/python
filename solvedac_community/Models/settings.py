# -*- coding: utf-8 -*-

"""
Copyright (c) 2023 DevRuby
MIT License
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NON INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
"""

from dataclasses import dataclass
from typing import Dict, Union


@dataclass
class Settings:
    screen_theme: str
    tag_display_language: str
    icon_scheme_solved: str
    icon_scheme_not_solved: str
    problem_sort_by: str
    twitter_post_handle: bool
    twitter_post_on_class_increase: bool
    twitter_post_on_problem_solve: bool
    twitter_post_on_rating_increase: bool
    twitter_post_on_tier_increase: bool

    def __init__(self, data: dict[str, str]):
        self.screen_theme = data.get("screenTheme", "white")
        self.tag_display_language = data.get("tagDisplayLanguage", "ko")
        self.icon_scheme_solved = data.get("iconSchemeSolved", "default")
        self.icon_scheme_not_solved = data.get("iconSchemeNotSolved", "default")
        self.problem_sort_by = data.get("problemSortBy", "id")
        self.twitter_post_handle = data.get("twitterPostHandle", "false") == "true"
        self.twitter_post_on_class_increase = data.get("twitter_post_on_class_increase", "false") == "true"
        self.twitter_post_on_problem_solve = data.get("twitter_post_on_problem_solve", "false") == "true"
        self.twitter_post_on_rating_increase = data.get("twitter_post_on_rating_increase", "false") == "true"
        self.twitter_post_on_tier_increase = data.get("twitter_post_on_tier_increase", "false") == "true"

