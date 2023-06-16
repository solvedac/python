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

from datetime import datetime
from dataclasses import dataclass
from .auto_completion_data import SimplifiedUser
from .settings import Settings
from ..utils import get_datetime_from_string

from typing import Dict, Union, List


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


@dataclass
class AccountInfo:
    user: SimplifiedUser
    settings: Settings
    email: str
    aggred_on: Dict[str, str]
    emoticons: List[EmoticonInfo]
    notification_count: int
    last_solved_state_changed_at: datetime

    def __init__(self, data: Dict[str, Union[dict, list, int, str]]):
        self.user = SimplifiedUser(data["user"])
        self.settings = Settings(data["user"]["settings"])
        self.email = data["user"]["email"]
        self.aggred_on = data["aggredOn"]
        self.emoticons = [EmoticonInfo(dat) for dat in data["emoticons"]]
        self.notification_count = data["notificationCount"]
        self.last_solved_state_changed_at = get_datetime_from_string(data["lastSolvedStateChangedAt"])
