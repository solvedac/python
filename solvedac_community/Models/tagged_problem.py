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
from typing import Dict, Union, List

from .problem_level import ProblemLevel
from .problem_tag import ProblemTag


@dataclass
class TaggedProblem:
    problem_id: int
    title_ko: str
    is_solvable: bool
    is_partial: bool
    accepted_user_count: int
    level: ProblemLevel
    voted_user_count: int
    is_level_locked: bool
    average_tries: float
    tags: List[ProblemTag]

    def __init__(self, data: Dict[str, Union[int, str, bool, list]]):
        self.problem_id: int = data["problemId"]
        self.title_ko: str = data["titleKo"]
        self.is_solvable: bool = data["isSolvable"]
        self.is_partial: bool = data["isPartial"]
        self.accepted_user_count: int = data["acceptedUserCount"]
        self.level: ProblemLevel = ProblemLevel(data["level"])
        self.voted_user_count: int = data["votedUserCount"]
        self.is_level_locked: bool = data["isLevelLocked"]
        self.average_tries: float = data["averageTries"]
        self.tags: List[ProblemTag] = [ProblemTag(tag) for tag in data["tags"]]
