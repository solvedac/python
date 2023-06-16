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

import asyncio
from typing import ClassVar, Optional, Union, Dict

import httpx

from solvedac_community.HTTPClients.abstract_http_client import AbstractHTTPClient
from solvedac_community.HTTPClients.httpclient import ResponseData, Route


class HttpxHTTPClient(AbstractHTTPClient):
    USER_AGENT: ClassVar[str] = "Mozilla/5.0"

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, loop: asyncio.AbstractEventLoop, solvedac_token: Optional[str] = None) -> None:
        self.loop: asyncio.AbstractEventLoop = loop
        self.lock: asyncio.Lock = asyncio.Lock()
        self.solvedac_token: Union[str, None] = solvedac_token

    async def request(self, route: Route, headers: Optional[Dict[str, str]] = None) -> ResponseData:
        if not headers:
            headers = {}

        default_header = {"User-Agent": self.USER_AGENT, "Accept": "application/json"}
        headers.update(default_header)

        async with self.lock:
            async with httpx.AsyncClient(
                cookies={"solvedacToken": self.solvedac_token} if self.solvedac_token else None
            ) as client:
                response: httpx.Response = await client.request(
                    method=route.method.name, url=route.url, headers=headers
                )
                status: int = response.status_code
                text: str = response.text
                return ResponseData(text, status)
