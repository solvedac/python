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
from typing import Dict

from solvedac_community.Schemas.Enums.badge_category import BadgeCategory
from solvedac_community.Schemas.Enums.badge_tier import BadgeTier


@dataclass
class Badge:
    badge_id: str
    badge_image_url: str
    display_name: str
    display_description: str
    badge_tier: BadgeTier
    badge_category: BadgeCategory

    def __init__(self, data: Dict[str, str]):
        self.badge_id: str = data["badgeId"]
        self.badge_image_url: str = data["badgeImageUrl"]
        self.display_name: str = data["displayName"]
        self.display_description: str = data["displayDescription"]
        self.badge_tier: BadgeTier = BadgeTier(data["badgeTier"])
        self.badge_category: BadgeCategory = BadgeCategory(data["badgeCategory"])
