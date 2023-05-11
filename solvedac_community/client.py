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
import json
from typing import Optional

from .Models import *

from .httpclient import HTTPClient
from .httpclient import RequestMethod
from .httpclient import ResponseData
from .httpclient import Route


class Client:
    loop: asyncio.AbstractEventLoop
    http_client: HTTPClient

    def __init__(self, solvedac_token: Optional[str] = None) -> None:
        try:
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        except AttributeError:
            pass
        self.loop = asyncio.get_event_loop()
        self.http_client = HTTPClient(self.loop, solvedac_token)

    async def get_user(self, handle: str) -> User:
        response: ResponseData = await self.http_client.request(
            Route(RequestMethod.GET, f"/user/show", params={"handle": handle})
        )
        assert response.status == 200, "HTTP Response Status Code is not 200\nStatus Code : %d" % response.status
        json_data: dict = json.loads(response.response_data)
        return User(json_data)

    async def get_background(self, background_id: str) -> Background:
        response: ResponseData = await self.http_client.request(
            Route(
                RequestMethod.GET,
                f"/background/show",
                params={"backgroundId": background_id},
            )
        )
        assert response.status == 200, "HTTP Response Status Code is not 200\nStatus Code : %d" % response.status
        json_data: dict = json.loads(response.response_data)
        return Background(json_data)

    async def get_badge(self, badge_id: str) -> Badge:
        response: ResponseData = await self.http_client.request(
            Route(RequestMethod.GET, f"/badge/show", params={"badgeId": badge_id})
        )
        assert response.status == 200, "HTTP Response Status Code is not 200\nStatus Code : %d" % response.status
        json_data: dict = json.loads(response.response_data)
        return Badge(json_data)
