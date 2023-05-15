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


@dataclass
class SolvedAcStatistics:
    problem_count: int
    problem_voted_count: int
    user_count: int
    contributor_count: int
    contribution_count: int

    def __init__(self, data: Dict[str, int]):
        self.problem_count: int = data["problemCount"]
        self.problem_voted_count: int = data["problemVotedCount"]
        self.user_count: int = data["userCount"]
        self.contributor_count: int = data["contributorCount"]
        self.contribution_count: int = data["contributionCount"]
