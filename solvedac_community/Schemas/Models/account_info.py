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
from datetime import datetime
from typing import Dict, Union, List

from solvedac_community.Schemas.Models.auto_completion_data import SimplifiedUser
from solvedac_community.Schemas.Models.emoticon_info import EmoticonInfo
from solvedac_community.Schemas.Models.settings import Settings
from solvedac_community.utils import get_datetime_from_string

__all__ = ["AccountInfo"]


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
