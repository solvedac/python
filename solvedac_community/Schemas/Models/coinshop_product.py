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

from solvedac_community.Schemas.Enums.price_unit import PriceUnit
from solvedac_community.Schemas.Models.item import Item


@dataclass()
class CoinshopProduct:
    sku_id: int
    item: Item
    units: int
    price: int
    price_units: PriceUnit
    item_use_time_limited: bool
    item_sell_time_limited: bool

    def __init__(self, data: Dict[str, Union[str, int, bool, dict]]):
        self.sku_id: int = data["skuId"]
        self.item: Item = Item(data["item"])
        self.units: int = data["units"]
        self.price: int = data["price"]
        self.price_units: PriceUnit = PriceUnit(data["priceUnit"])
        self.item_use_time_limited: bool = data["itemUseTimeLimited"]
        self.item_sell_time_limited: bool = data["itemSellTimeLimited"]
