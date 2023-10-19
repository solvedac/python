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

import datetime
from dataclasses import dataclass
from typing import Dict, Union

from solvedac_community.Schemas.Enums.class_decoration import ClassDecoration
from solvedac_community.Schemas.Enums.user_tier import UserTier
from solvedac_community.utils import get_datetime_from_string

__all__ = ["SimplifiedUser"]


@dataclass
class SimplifiedUser:
    handle: str
    bio: str
    badge_id: str
    background_id: str
    profile_image_url: Union[str, None]
    solved_count: int
    vote_count: int
    class_rating: int
    class_decoration: ClassDecoration
    rival_count: int
    tier: UserTier
    rating: int
    rating_by_problems_sum: int
    rating_by_class: int
    rating_by_solved_count: int
    rating_by_vote_count: int
    max_streak: int
    coins: int
    stardusts: int
    joined_at: datetime.datetime
    banned_until: datetime.datetime
    pro_until: datetime.datetime

    def __init__(self, data: Dict[str, Union[str, int, bool, None]]):
        self.handle: str = data["handle"]
        self.bio: str = data["bio"]
        self.badge_id: Union[str, None] = data.get("badge_id")
        self.background_id: str = data["backgroundId"]
        self.profile_image_url: Union[str, None] = data.get("profileImageUrl")
        self.solved_count: int = data["solvedCount"]
        self.vote_count: int = data["voteCount"]
        self.class_rating: int = data["class"]
        self.class_decoration: ClassDecoration = ClassDecoration(data["classDecoration"])
        self.rival_count: int = data["rivalCount"]
        self.reverse_rival_count: int = data["reverseRivalCount"]
        self.tier: UserTier = UserTier(data["tier"])
        self.rating: int = data["rating"]
        self.rating_by_problems_sum: int = data["ratingByProblemsSum"]
        self.rating_by_class: int = data["ratingByClass"]
        self.rating_by_solved_count: int = data["ratingBySolvedCount"]
        self.rating_by_vote_count: int = data["ratingByVoteCount"]
        self.max_streak: int = data["maxStreak"]
        self.coins: int = data["coins"]
        self.stardusts: int = data["stardusts"]
        self.joined_at: datetime.datetime = get_datetime_from_string(data["joinedAt"])
        self.banned_until: datetime.datetime = get_datetime_from_string(data["bannedUntil"])
        self.pro_until: datetime.datetime = get_datetime_from_string(data["proUntil"])
