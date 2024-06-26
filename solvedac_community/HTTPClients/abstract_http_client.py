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

from abc import ABCMeta, abstractmethod
from typing import Optional, Dict

from solvedac_community.HTTPClients.httpclient import ResponseData, Route

__all__ = ["AbstractHTTPClient"]


class AbstractHTTPClient(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, solvedac_token: Optional[str] = None):
        pass

    @abstractmethod
    async def request(
        self, route: Route, headers: Optional[Dict[str, str]] = None, body: Optional[Dict[str, str]] = None
    ) -> ResponseData:
        pass
