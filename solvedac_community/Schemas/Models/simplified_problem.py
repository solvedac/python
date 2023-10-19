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

__all__ = ["SimplifiedProblem"]


@dataclass
class SimplifiedProblem:
    id: int
    title: str
    level: int
    solved: int
    caption: str
    description: str
    href: str

    def __init__(self, data: Dict[str, Union[int, str]]):
        self.id: int = data["id"]
        self.title: str = data["title"]
        self.level: int = data["level"]
        self.solved: int = data["solved"]
        self.caption: str = data["caption"]
        self.description: str = data["description"]
        self.href: str = data["href"]
