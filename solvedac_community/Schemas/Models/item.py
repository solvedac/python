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

__all__ = ["Item"]


@dataclass
class Item:
    item_id: str
    item_image_url: str
    inventory_max_units: int
    usable: bool
    display_name: str
    display_description: str

    def __init__(self, data: Dict[str, Union[str, int, bool]]):
        self.item_id: str = data["itemId"]
        self.item_image_url: str = data["itemImageUrl"]
        self.inventory_max_units: int = data["inventoryMaxUnits"]
        self.usable: bool = data["usable"]
        self.display_name: str = data["displayName"]
        self.display_description: str = data["displayDescription"]
