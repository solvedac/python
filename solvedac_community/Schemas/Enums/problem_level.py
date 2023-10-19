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

from enum import Enum
from enum import auto

__all__ = ["ProblemLevel"]


class ProblemLevel(Enum):
    def __str__(self):
        name = ["Bronze", "Silver", "Gold", "Platinum", "Diamond", "Ruby"]
        numb = ["V", "IV", "III", "II", "I"]
        n, m = divmod(self.value + 4, 5)
        if n == 0:
            return "Unrated"
        return " ".join((name[n - 1], numb[m]))

    def __repr__(self):
        name = ["Bronze", "Silver", "Gold", "Platinum", "Diamond", "Ruby"]
        numb = ["V", "IV", "III", "II", "I"]
        n, m = divmod(self.value + 4, 5)
        if n == 0:
            return "Unrated"
        return " ".join((name[n - 1], numb[m]))

    Unrated = 0
    Bronze5 = auto()
    Bronze4 = auto()
    Bronze3 = auto()
    Bronze2 = auto()
    Bronze1 = auto()
    Silver5 = auto()
    Silver4 = auto()
    Silver3 = auto()
    Silver2 = auto()
    Silver1 = auto()
    Gold5 = auto()
    Gold4 = auto()
    Gold3 = auto()
    Gold2 = auto()
    Gold1 = auto()
    Platinum5 = auto()
    Platinum4 = auto()
    Platinum3 = auto()
    Platinum2 = auto()
    Platinum1 = auto()
    Diamond5 = auto()
    Diamond4 = auto()
    Diamond3 = auto()
    Diamond2 = auto()
    Diamond1 = auto()
    Ruby5 = auto()
    Ruby4 = auto()
    Ruby3 = auto()
    Ruby2 = auto()
    Ruby1 = auto()
