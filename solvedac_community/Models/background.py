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
from typing import Dict, Union, Optional, List

from .author import Author


@dataclass()
class Background:
    background_id: str
    background_image_url: str
    fallback_background_image_url: Union[str, None]
    background_video_url: Union[str, None]
    unlocked_user_count: int
    display_name: str
    display_description: str
    conditions: Union[str, None]
    hidden_conditions: bool
    is_illust: bool
    authors: List[Author]

    def __init__(self, data: Dict[str, Union[str, int, bool, list]]):
        self.background_id: str = data["backgroundId"]
        self.background_image_url: str = data["backgroundImageUrl"]
        self.fallback_background_image_url: Union[str, None] = data["fallbackBackgroundImageUrl"]
        self.background_video_url: Union[str, None] = data["backgroundVideoUrl"]
        self.unlocked_user_count: int = data["unlockedUserCount"]
        self.display_name: str = data["displayName"]
        self.display_description: str = data["displayDescription"]
        self.conditions: Union[str, None] = data.get("conditions")
        self.hidden_conditions: bool = data["hiddenConditions"]
        self.is_illust: bool = data["isIllust"]
        self.authors: List[Author] = [Author(author) for author in data["authors"]]
