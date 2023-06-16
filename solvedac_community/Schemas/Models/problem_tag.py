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
from typing import Dict, List, Union

from .tag_display_name import TagDisplayName


@dataclass
class ProblemTag:
    key: str
    is_meta: bool
    boj_tag_id: int
    problem_count: int
    display_names: List[TagDisplayName]
    aliases: List[str]

    def __init__(self, data: Dict[str, Union[str, int, bool, dict, list]]):
        self.key: str = data["key"]
        self.is_meta: bool = data["isMeta"]
        self.boj_tag_id: int = data["bojTagId"]
        self.problem_count: int = data["problemCount"]
        self.display_names: List[TagDisplayName] = [TagDisplayName(d) for d in data["displayNames"]]
        self.aliases: List[str] = [d["alias"] for d in data["aliases"]]
