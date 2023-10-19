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

__all__ = ["EmoticonInfo"]


@dataclass
class EmoticonInfo:
    emoticon_id: str
    emoticon_url: str
    display_name: str
    unlocked: bool

    def __init__(self, data: Dict[str, Union[str, bool]]):
        self.emoticon_id = data["emoticonId"]
        self.emoticon_url = data["emoticonUrl"]
        self.display_name = data["displayName"]
        self.unlocked = data["unlocked"]
