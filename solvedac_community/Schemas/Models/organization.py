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

__all__ = ["Organization"]


@dataclass
class Organization:
    organization_id: int
    name: str
    type: str
    rating: int
    user_count: int
    vote_count: int
    solved_count: int
    color: str

    def __init__(self, data: Dict[str, Union[str, int]]):
        self.organization_id: int = data["organizationId"]
        self.name: str = data["name"]
        self.type: str = data["type"]
        self.rating: int = data["rating"]
        self.user_count: int = data["userCount"]
        self.vote_count: int = data["voteCount"]
        self.solved_count: int = data["solvedCount"]
        self.color: str = data["color"]
