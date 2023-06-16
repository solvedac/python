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

from solvedac_community.Schemas.Models.auto_complete_text import AutoCompleteText
from solvedac_community.Schemas.Models.simplified_problem import SimplifiedProblem
from solvedac_community.Schemas.Models.simplified_tag import SimplifiedTag
from solvedac_community.Schemas.Models.simplified_user import SimplifiedUser


@dataclass
class AutoCompletionData:
    autocomplete: List[AutoCompleteText]
    problems: List[SimplifiedProblem]
    problem_count: int
    tags: List[SimplifiedTag]
    tag_count: int
    users: List[SimplifiedUser]
    user_count: int

    def __init__(self, data: Dict[str, Union[list, int]]):
        self.autocomplete: List[AutoCompleteText] = [AutoCompleteText(dat) for dat in data["autocomplete"]]
        self.problems: List[SimplifiedProblem] = [SimplifiedProblem(dat) for dat in data["problems"]]
        self.problem_count: int = data["problemCount"]
        self.tags: List[SimplifiedTag] = [SimplifiedTag(dat) for dat in data["tags"]]
        self.tag_count: int = data["tagCount"]
        self.users: List[SimplifiedUser] = [SimplifiedUser(dat) for dat in data["users"]]
        self.user_count: int = data["userCount"]
