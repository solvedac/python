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

__all__ = ["Author"]


@dataclass
class Author:
    author_id: str
    role: str
    author_url: Union[str, None]
    handle: str
    twitter: Union[str, None]
    instagram: Union[str, None]
    display_name: str

    def __init__(self, data: Dict[str, Union[str, None]]):
        self.author_id: str = data["authorId"]
        self.role: str = data["role"]
        self.author_url: Union[str, None] = data["authorUrl"]
        self.handle: str = data["handle"]
        self.twitter: Union[str, None] = data["twitter"]
        self.instagram: Union[str, None] = data["instagram"]
        self.display_name: str = data["displayName"]
